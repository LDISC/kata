import unittest

from equation import calculate_x


class EquationTest(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(0, calculate_x("x = 0"))
        self.assertEqual(1, calculate_x("x = 1"))
        self.assertEqual(2, calculate_x("x = 2"))

    def test_easy_negative(self):
        self.assertEqual(-1, calculate_x("x = -1"))
        self.assertEqual(-2, calculate_x("x = -2"))
    
    def test_more_than_ten(self):
        self.assertEqual(10, calculate_x("x = 10"))
        self.assertEqual(-10, calculate_x("x = -10"))

    def test_float(self):
        self.assertEqual(1.5, calculate_x("x = 1.5"))
        self.assertEqual(-1.5, calculate_x("x = -1.5"))
    
    def test_multiply(self):
        self.assertEqual(1.5, calculate_x("2x = 3"))
        self.assertEqual(1, calculate_x("3x = 3"))
        self.assertEqual(1, calculate_x("10x = 10"))
    
    def test_multiply_negative(self):
        self.assertEqual(-1, calculate_x("-3x = 3"))
#        self.assertEqual(-1, calculate_x("-x = 1"))

if __name__ == '__main__':
    unittest.main()
