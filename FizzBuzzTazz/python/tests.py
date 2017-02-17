import unittest

from fizzbuzztazz import fizzBuzzTazz


class FizzBuzzTazzTest(unittest.TestCase):
    def test_none(self):
        self.assertEqual("", fizzBuzzTazz(0))

    def test_no_match(self):
        self.assertEqual("", fizzBuzzTazz(1))
        self.assertEqual("", fizzBuzzTazz(2))
        self.assertEqual("", fizzBuzzTazz(4))

    def test_Fizz(self):
        self.assertEqual("Fizz", fizzBuzzTazz(3))
        self.assertEqual("Fizz", fizzBuzzTazz(6))

    def test_Buzz(self):
        self.assertEqual("Buzz", fizzBuzzTazz(5))
        self.assertEqual("Buzz", fizzBuzzTazz(10))

    def test_Tazz(self):
        self.assertEqual("Tazz", fizzBuzzTazz(7))
        self.assertEqual("Tazz", fizzBuzzTazz(14))

    def test_FizzBuzz(self):
        self.assertEqual("FizzBuzz", fizzBuzzTazz(15))
        self.assertEqual("FizzBuzz", fizzBuzzTazz(30))

    def test_FizzTazz(self):
        self.assertEqual("FizzTazz", fizzBuzzTazz(21))
        self.assertEqual("FizzTazz", fizzBuzzTazz(42))

    def test_BuzzTazz(self):
        self.assertEqual("BuzzTazz", fizzBuzzTazz(35))
        self.assertEqual("BuzzTazz", fizzBuzzTazz(70))

    def test_FizzBuzzTazz(self):
        self.assertEqual("FizzBuzzTazz", fizzBuzzTazz(105))
        self.assertEqual("FizzBuzzTazz", fizzBuzzTazz(210))

class FizzBuzzTazzPart2Test(unittest.TestCase):

    def test_Mozz(self):
        self.assertEqual("Mozz", fizzBuzzTazz(11))
        self.assertEqual("Mozz", fizzBuzzTazz(22))

    def test_FizzMozz(self):
        self.assertEqual("FizzMozz", fizzBuzzTazz(33))
        self.assertEqual("FizzMozz", fizzBuzzTazz(66))

    def test_BuzzMozz(self):
        self.assertEqual("BuzzMozz", fizzBuzzTazz(55))
        self.assertEqual("BuzzMozz", fizzBuzzTazz(110))

    def test_TazzMozz(self):
        self.assertEqual("TazzMozz", fizzBuzzTazz(77))
        self.assertEqual("TazzMozz", fizzBuzzTazz(154))

    def test_FizzBuzzMozz(self):
        self.assertEqual("FizzBuzzMozz", fizzBuzzTazz(165))
        self.assertEqual("FizzBuzzMozz", fizzBuzzTazz(330))

    def test_FizzTazzMozz(self):
        self.assertEqual("FizzTazzMozz", fizzBuzzTazz(231))
        self.assertEqual("FizzTazzMozz", fizzBuzzTazz(462))

    def test_BuzzTazzMozz(self):
        self.assertEqual("BuzzTazzMozz", fizzBuzzTazz(385))
        self.assertEqual("BuzzTazzMozz", fizzBuzzTazz(770))

    def test_FizzBuzzTazzMozz(self):
        self.assertEqual("FizzBuzzTazzMozz", fizzBuzzTazz(1155))
        self.assertEqual("FizzBuzzTazzMozz", fizzBuzzTazz(2310))

class FizzBuzzTazzPart3Test(unittest.TestCase):

    def test_Vezz(self):
        self.assertEqual("Vezz", fizzBuzzTazz(13))
        self.assertEqual("Vezz", fizzBuzzTazz(26))

    def test_FizzVezz(self):
        self.assertEqual("FizzVezz", fizzBuzzTazz(39))
        self.assertEqual("FizzVezz", fizzBuzzTazz(78))

    def test_BuzzVezz(self):
        self.assertEqual("BuzzVezz", fizzBuzzTazz(65))
        self.assertEqual("BuzzVezz", fizzBuzzTazz(130))

    def test_TazzVezz(self):
        self.assertEqual("TazzVezz", fizzBuzzTazz(91))
        self.assertEqual("TazzVezz", fizzBuzzTazz(182))

    def test_MozzVezz(self):
        self.assertEqual("MozzVezz", fizzBuzzTazz(143))
        self.assertEqual("MozzVezz", fizzBuzzTazz(286))

    def test_FizzBuzzVezz(self):
        self.assertEqual("FizzBuzzVezz", fizzBuzzTazz(195))
        self.assertEqual("FizzBuzzVezz", fizzBuzzTazz(390))

    def test_FizzTazzVezz(self):
        self.assertEqual("FizzTazzVezz", fizzBuzzTazz(273))
        self.assertEqual("FizzTazzVezz", fizzBuzzTazz(546))

    def test_FizzMozzVezz(self):
        self.assertEqual("FizzMozzVezz", fizzBuzzTazz(429))
        self.assertEqual("FizzMozzVezz", fizzBuzzTazz(858))

    def test_BuzzTazzVezz(self):
        self.assertEqual("BuzzTazzVezz", fizzBuzzTazz(455))
        self.assertEqual("BuzzTazzVezz", fizzBuzzTazz(910))

    def test_BuzzMozzVezz(self):
        self.assertEqual("BuzzMozzVezz", fizzBuzzTazz(715))
        self.assertEqual("BuzzMozzVezz", fizzBuzzTazz(1430))

    def test_TazzMozzVezz(self):
        self.assertEqual("TazzMozzVezz", fizzBuzzTazz(1001))
        self.assertEqual("TazzMozzVezz", fizzBuzzTazz(2002))

    def test_FizzBuzzTazzVezz(self):
        self.assertEqual("FizzBuzzTazzVezz", fizzBuzzTazz(1365))
        self.assertEqual("FizzBuzzTazzVezz", fizzBuzzTazz(2730))

    def test_FizzBuzzMozzVezz(self):
        self.assertEqual("FizzBuzzMozzVezz", fizzBuzzTazz(2145))
        self.assertEqual("FizzBuzzMozzVezz", fizzBuzzTazz(4290))

    def test_FizzTazzMozzVezz(self):
        self.assertEqual("FizzTazzMozzVezz", fizzBuzzTazz(3003))
        self.assertEqual("FizzTazzMozzVezz", fizzBuzzTazz(6006))

    def test_BuzzTazzMozzVezz(self):
        self.assertEqual("BuzzTazzMozzVezz", fizzBuzzTazz(5005))
        self.assertEqual("BuzzTazzMozzVezz", fizzBuzzTazz(10010))

    def test_FizzBuzzTazzMozzVezz(self):
        self.assertEqual("FizzBuzzTazzMozzVezz", fizzBuzzTazz(15015))
        self.assertEqual("FizzBuzzTazzMozzVezz", fizzBuzzTazz(30030))


if __name__ == '__main__':
    unittest.main()
