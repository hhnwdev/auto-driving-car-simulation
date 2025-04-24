import builtins
import importlib.util
import unittest
from unittest import mock
import os

class TestMainBlock(unittest.TestCase):
    def test_entry_point_main_called(self):
        # Path to your test file
        path = os.path.join(os.path.dirname(__file__), 'test_simulation_unittest.py')

        # Load the module as if it were being run as __main__
        spec = importlib.util.spec_from_file_location("__main__", path)
        module = importlib.util.module_from_spec(spec)

        with mock.patch("unittest.main") as mock_main:
            # Inject a fake '__main__'
            builtins.__name__ = "__main__"
            spec.loader.exec_module(module)

            # Assert unittest.main was called
            mock_main.assert_called_once()

        # Restore builtins.__name__ just in case (to avoid side effects)
        builtins.__name__ = "builtins"