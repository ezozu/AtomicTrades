# test_atomictrades.py
"""
Tests for AtomicTrades module.
"""

import unittest
from atomictrades import AtomicTrades

class TestAtomicTrades(unittest.TestCase):
    """Test cases for AtomicTrades class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AtomicTrades()
        self.assertIsInstance(instance, AtomicTrades)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AtomicTrades()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
