import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    A test class for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up a SimpleCalculator instance before each test.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the addition method of SimpleCalculator.
        """
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test zero
        self.assertEqual(self.calc.add(0, 0), 0)
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """
        Test the subtraction method of SimpleCalculator.
        """
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Test large numbers
        self.assertEqual(self.calc.subtract(2000000, 1000000), 1000000)

    def test_multiplication(self):
        """
        Test the multiplication method of SimpleCalculator.
        """
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        # Test zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)

    def test_division(self):
        """
        Test the division method of SimpleCalculator.
        """
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Test division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        # Test division resulting in a fraction
        self.assertEqual(self.calc.divide(5, 2), 2.5)

if __name__ == "__main__":
    unittest.main()
