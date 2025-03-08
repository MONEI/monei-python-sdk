import unittest
from datetime import datetime
from copy import deepcopy
import io
import uuid

from Monei.model_utils import (
    convert_js_args_to_python_args,
    cached_property,
    OpenApiModel,
    ModelSimple,
    ModelNormal,
    ModelComposed,
    change_keys_js_to_python,
    deserialize_primitive,
    model_to_dict,
    is_type_nullable,
    is_valid_type,
    get_simple_class,
    check_allowed_values,
    none_type,
    file_type,
)
from Monei.exceptions import ApiAttributeError, ApiValueError, ApiTypeError


class TestModelUtils(unittest.TestCase):
    """ModelUtils unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_convert_js_args_to_python_args(self):
        """Test convert_js_args_to_python_args decorator."""

        # Create a test class with the decorator
        class TestClass:
            @convert_js_args_to_python_args
            def __init__(self, _self=None, camelCase=None, snake_case=None):
                self._self = _self
                self.camel_case = camelCase
                self.snake_case = snake_case

        # Test with spec_property_naming=False (default)
        instance = TestClass(camelCase="value1", snake_case="value2")
        self.assertEqual(instance.camel_case, "value1")
        self.assertEqual(instance.snake_case, "value2")
        self.assertIsNone(instance._self)

        # Test with spec_property_naming=True
        instance = TestClass(
            _self="self_value",
            camelCase="value1",
            snake_case="value2",
            _spec_property_naming=True,
        )
        self.assertEqual(instance.camel_case, "value1")
        self.assertEqual(instance.snake_case, "value2")
        self.assertEqual(instance._self, "self_value")

    def test_cached_property(self):
        """Test cached_property decorator."""

        class TestClass:
            call_count = 0

            @cached_property
            def cached_value(self):
                self.call_count += 1
                return f"value_{self.call_count}"

        instance = TestClass()

        # First call should compute the value
        value1 = instance.cached_value
        self.assertEqual(value1, "value_1")
        self.assertEqual(instance.call_count, 1)

        # Second call should return the cached value
        value2 = instance.cached_value
        self.assertEqual(value2, "value_1")
        self.assertEqual(instance.call_count, 1)  # Call count should not increase

    def test_model_simple(self):
        """Test ModelSimple class."""
        # Create a simple model instance
        model = ModelSimple()

        # Test __setitem__ and __getitem__
        model["key1"] = "value1"
        self.assertEqual(model["key1"], "value1")

        # Test get method
        self.assertEqual(model.get("key1"), "value1")
        self.assertEqual(model.get("key2", "default"), "default")

        # Test __contains__
        self.assertTrue("key1" in model)
        self.assertFalse("key2" in model)

        # Test to_str
        self.assertIn("key1", model.to_str())
        self.assertIn("value1", model.to_str())

    def test_model_normal(self):
        """Test ModelNormal class."""

        # Create a normal model class
        class TestModel(ModelNormal):
            openapi_types = {"name": str, "age": int}
            attribute_map = {"name": "name", "age": "age"}

            def __init__(self, name=None, age=None):
                self._name = None
                self._age = None
                self.name = name
                self.age = age

        # Create an instance
        model = TestModel(name="John", age=30)

        # Test __setitem__ and __getitem__
        model["name"] = "Jane"
        self.assertEqual(model["name"], "Jane")

        # Test get method
        self.assertEqual(model.get("name"), "Jane")
        self.assertEqual(model.get("unknown", "default"), "default")

        # Test __contains__
        self.assertTrue("name" in model)
        self.assertTrue("age" in model)
        self.assertFalse("unknown" in model)

        # Test to_dict
        model_dict = model.to_dict()
        self.assertEqual(model_dict, {"name": "Jane", "age": 30})

        # Test to_str
        model_str = model.to_str()
        self.assertIn("Jane", model_str)
        self.assertIn("30", model_str)

    def test_deserialize_primitive(self):
        """Test deserialize_primitive function."""
        # Test deserializing a string
        result = deserialize_primitive("test", str, ["path", "to", "item"])
        self.assertEqual(result, "test")

        # Test deserializing an integer
        result = deserialize_primitive("123", int, ["path", "to", "item"])
        self.assertEqual(result, 123)

        # Test deserializing a float
        result = deserialize_primitive("123.45", float, ["path", "to", "item"])
        self.assertEqual(result, 123.45)

        # Test deserializing a boolean
        result = deserialize_primitive("true", bool, ["path", "to", "item"])
        self.assertTrue(result)

        # Test deserializing a date
        result = deserialize_primitive("2023-01-01", datetime, ["path", "to", "item"])
        self.assertEqual(result.year, 2023)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 1)

        # Test deserializing None
        result = deserialize_primitive(None, none_type, ["path", "to", "item"])
        self.assertIsNone(result)

        # Test deserializing to an unsupported type
        with self.assertRaises(ApiTypeError):
            deserialize_primitive("test", dict, ["path", "to", "item"])

    def test_change_keys_js_to_python(self):
        """Test change_keys_js_to_python function."""

        # Create a test class with attribute_map
        class TestClass:
            attribute_map = {
                "snake_case": "snakeCase",
                "another_snake": "anotherSnake",
                "normal": "normal",
            }

        # Test converting keys from JavaScript to Python
        js_dict = {
            "snakeCase": "value1",
            "anotherSnake": "value2",
            "normal": "value3",
            "unmapped": "value4",
        }

        python_dict = change_keys_js_to_python(js_dict, TestClass)

        # Check that keys were properly converted
        self.assertEqual(python_dict["snake_case"], "value1")
        self.assertEqual(python_dict["another_snake"], "value2")
        self.assertEqual(python_dict["normal"], "value3")
        self.assertEqual(
            python_dict["unmapped"], "value4"
        )  # Unmapped keys should remain unchanged

    def test_is_type_nullable(self):
        """Test is_type_nullable function."""
        # Test with nullable types
        self.assertTrue(is_type_nullable(none_type))
        self.assertTrue(is_type_nullable((str, none_type)))
        self.assertTrue(is_type_nullable((int, str, none_type)))

        # Test with non-nullable types
        self.assertFalse(is_type_nullable(str))
        self.assertFalse(is_type_nullable((int, str)))
        self.assertFalse(is_type_nullable(list))

    def test_is_valid_type(self):
        """Test is_valid_type function."""
        # Test with valid types
        self.assertTrue(is_valid_type(str, [str]))
        self.assertTrue(is_valid_type(str, [int, str, bool]))
        self.assertTrue(is_valid_type(none_type, [str, none_type]))

        # Test with invalid types
        self.assertFalse(is_valid_type(str, [int]))
        self.assertFalse(is_valid_type(str, [int, bool]))
        self.assertFalse(is_valid_type(str, []))

    def test_get_simple_class(self):
        """Test get_simple_class function."""
        # Test with simple types
        self.assertEqual(get_simple_class("test"), str)
        self.assertEqual(get_simple_class(123), int)
        self.assertEqual(get_simple_class(123.45), float)
        self.assertEqual(get_simple_class(True), bool)
        self.assertEqual(get_simple_class(None), none_type)

        # Test with complex types
        self.assertEqual(get_simple_class([1, 2, 3]), list)
        self.assertEqual(get_simple_class({"key": "value"}), dict)
        self.assertEqual(get_simple_class(set([1, 2, 3])), set)

        # Test with file type
        file_obj = io.StringIO("test")
        self.assertEqual(get_simple_class(file_obj), file_type)

    def test_check_allowed_values(self):
        """Test check_allowed_values function."""
        # Test with allowed values
        allowed_values = {"enum_value": ["value1", "value2", "value3"]}

        # Should not raise an exception
        check_allowed_values(
            allowed_values, ["path", "to", "item"], {"enum_value": "value1"}
        )

        # Should raise an exception for invalid value
        with self.assertRaises(ApiValueError):
            check_allowed_values(
                allowed_values, ["path", "to", "item"], {"enum_value": "invalid"}
            )

        # Test with multiple values
        allowed_values = {
            "enum_value": ["value1", "value2", "value3"],
            "status": ["active", "inactive"],
        }

        # Should not raise an exception
        check_allowed_values(
            allowed_values,
            ["path", "to", "item"],
            {"enum_value": "value2", "status": "active"},
        )

        # Should raise an exception for invalid value
        with self.assertRaises(ApiValueError):
            check_allowed_values(
                allowed_values,
                ["path", "to", "item"],
                {"enum_value": "value2", "status": "unknown"},
            )

    def test_model_to_dict(self):
        """Test model_to_dict function."""

        # Create a test model
        class TestModel(ModelNormal):
            openapi_types = {"name": str, "age": int, "tags": list}
            attribute_map = {"name": "name", "age": "age", "tags": "tags"}

            def __init__(self, name=None, age=None, tags=None):
                self._name = None
                self._age = None
                self._tags = None
                self.name = name
                self.age = age
                self.tags = tags

        # Create a nested model
        class NestedModel(ModelNormal):
            openapi_types = {"user": TestModel, "active": bool}
            attribute_map = {"user": "user", "active": "active"}

            def __init__(self, user=None, active=None):
                self._user = None
                self._active = None
                self.user = user
                self.active = active

        # Create instances
        user = TestModel(name="John", age=30, tags=["tag1", "tag2"])
        nested = NestedModel(user=user, active=True)

        # Test model_to_dict with simple model
        user_dict = model_to_dict(user)
        self.assertEqual(
            user_dict, {"name": "John", "age": 30, "tags": ["tag1", "tag2"]}
        )

        # Test model_to_dict with nested model
        nested_dict = model_to_dict(nested)
        self.assertEqual(
            nested_dict,
            {
                "user": {"name": "John", "age": 30, "tags": ["tag1", "tag2"]},
                "active": True,
            },
        )

        # Test with serialize=False
        user_dict_no_serialize = model_to_dict(user, serialize=False)
        self.assertEqual(
            user_dict_no_serialize,
            {"name": "John", "age": 30, "tags": ["tag1", "tag2"]},
        )


if __name__ == "__main__":
    unittest.main()
