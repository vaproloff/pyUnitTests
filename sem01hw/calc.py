import unittest


class Calculator:

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            raise ValueError('Divider cannot be zero')
        return a / b

    @staticmethod
    def calculate_discount(amount: int, discount: int) -> float:
        if amount < 0:
            raise ValueError("Amount can't be negative number")
        if not 0 <= discount <= 100:
            raise ValueError('Discount should be in limits: [0, 100]')
        return amount * (1 - discount / 100)


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ...

    @classmethod
    def tearDownClass(cls):
        ...

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        self.calculator = None

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, self.calculator.divide, 1, 0)

    @unittest.skip('Этот тест отключен')
    def test_disabled(self):
        self.fail('Этот тест не будет выполнен')

    def test_with_subtests(self):
        for i in [0, 1, 2, 3]:
            with self.subTest(i=i):
                self.assertEqual(self.calculator.add(2, i), 2 + i)

    def test_assert_true(self):
        self.assertTrue(self.calculator.add(2, 2) == 4)

    def test_assert_false(self):
        self.assertFalse(self.calculator.add(2, 2) == 5)

    def test_assert_not_none(self):
        self.assertIsNotNone(self.calculator)

    def test_assert_is_none(self):
        self.calculator = None
        self.assertIsNone(self.calculator)

    def test_assert_array_equals(self):
        expected = [1, 2, 3]
        actual = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_assert_array_is(self):
        expected = [1, 2, 3]
        # actual = [1, 2, 3]
        # self.assertIs(expected, actual)
        actual = expected
        self.assertIs(expected, actual)

    def test_discount(self):
        self.assertEqual(self.calculator.calculate_discount(200, 10), 180)

    def test_discount_bad_amount(self):
        self.assertRaises(ValueError, self.calculator.calculate_discount, -10, 0)

    def test_discount_bad_tax(self):
        self.assertRaises(ValueError, self.calculator.calculate_discount, 0, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
