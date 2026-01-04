# test_airdropclaimer.py
"""
Tests for AirdropClaimer module.
"""

import unittest
from airdropclaimer import AirdropClaimer

class TestAirdropClaimer(unittest.TestCase):
    """Test cases for AirdropClaimer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AirdropClaimer()
        self.assertIsInstance(instance, AirdropClaimer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AirdropClaimer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
