import pytest


@pytest.mark.unit
def test_mock_example():
    """A simple test example that doesn't rely on problematic models."""
    # This is just a placeholder test to demonstrate the test setup
    assert True


@pytest.mark.requires_api
def test_skip_example():
    """This test will be skipped when SKIP_GENERATED_TESTS is set."""
    # This test would be skipped in CI or when SKIP_GENERATED_TESTS is set
    assert True
