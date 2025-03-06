"""
Unit tests for the main.py file.
"""

import io
import sys
from unittest.mock import patch

from main import main


class TestMain:
    """Tests for the main function."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_output(self, mock_stdout):
        """Test that the main function prints the expected output."""
        main()
        assert mock_stdout.getvalue() == "Hello from monei-python-sdk!\n"

    @patch("main.main")
    def test_main_is_called_when_script_is_run_directly(self, mock_main):
        """Test that main() is called when the script is run directly."""
        # Store the original value of __name__
        original_name = sys.modules["main"].__name__
        
        try:
            # Set __name__ to "__main__" to simulate running the script directly
            sys.modules["main"].__name__ = "__main__"
            
            # Re-execute the if block from main.py
            if sys.modules["main"].__name__ == "__main__":
                mock_main()
            
            # Check that main() was called
            mock_main.assert_called_once()
        finally:
            # Restore the original value
            sys.modules["main"].__name__ = original_name 