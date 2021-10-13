import unittest

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for arg in ('string', 1.5):
            with self.subTest(x=arg):
                with self.assertRaises(TypeError):
                    factorize(arg)

    def test_negative(self):
        for arg in (-1, -10, -100):
            with self.subTest(x=arg):
                with self.assertRaises(ValueError):
                    factorize(arg)

    def test_zero_and_one_cases(self):
        for arg, res in (0, 1), ((0, ), (1, )):
            with self.subTest(x=arg):
                self.assertCountEqual(factorize(arg), res)

    def test_simple_numbers(self):
        arguments = answers = (3, 13, 29)
        for arg, res in arguments, answers:
            with self.subTest(x=arg):
                self.assertCountEqual(factorize(arg), res)

    def test_two_simple_multipliers(self):
        arguments = (6, 26, 121)
        answers = ((2, 3), ((2, 13)), (11, 11))
        for arg, res in arguments, answers:
            with self.subTest(x=arg):
                self.assertCountEqual(factorize(arg), res)

    def test_many_multipliers(self):
        arguments = (1001, 9699690)
        answers = ((7, 11, 13), ((2, 3, 5, 7, 11, 13, 17, 19)))
        for arg, res in arguments, answers:
            with self.subTest(x=arg):
                self.assertCountEqual(factorize(arg), res)


# def factorize(x):
#     """ 
#     Factorize positive integer and return its factors.
#     :type x: int,>=0
#     :rtype: tuple[N],N>0
#     """
#     pass

