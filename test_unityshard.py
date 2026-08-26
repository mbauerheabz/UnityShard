# test_unityshard.py
"""
Tests for UnityShard module.
"""

import unittest
from unityshard import UnityShard

class TestUnityShard(unittest.TestCase):
    """Test cases for UnityShard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UnityShard()
        self.assertIsInstance(instance, UnityShard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UnityShard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
