import unittest
import logging

log = logging.getLogger(__name__)


def VeryBasicExponential(x, n):
    total = 1
    for _ in range(n):
        total *= x
    return total


def RecursionExponential(x, n):
    if n < 0:
        return RecursionExponential(1 / x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 1:
        return x * RecursionExponential(x * x, (n - 1) / 2)
    return RecursionExponential(x * x, n / 2)


# Exponential by Squaring

def AuxiliaryMemoryRecursionExponential(y, x, n):
    if n < 0:
        return AuxiliaryMemoryRecursionExponential(y, 1 / x, -n)
    if n == 0:
        return y
    if n % 2 == 1:
        return AuxiliaryMemoryRecursionExponential(x * y, x * x, (n - 1) / 2)
    return AuxiliaryMemoryRecursionExponential(y, x * x, n / 2)


def ConstantAuxiliaryMemoryRecursionExponential(x, n):
    return AuxiliaryMemoryRecursionExponential(1, x, n)


def IterativeConstantAuxiliaryMemoryRecursionExponential(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n /= 2
        else:
            y *= x
            x *= x
            n = (n - 1) / 2
    return x * y


class TestExponential(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")

    def test_VeryBasicExponential_negative(self):
        log.debug(VeryBasicExponential(36, -1))
        self.assertEqual(
            VeryBasicExponential(36, -1), 1,
            "Should equal 1, since this function doesn't support negative integer"
        )

    def test_RecursionExponential_negative(self):
        log.debug(RecursionExponential(36, -1))
        self.assertEqual(
            RecursionExponential(36, -1), 36**-1,
            "Not equal to 0.027777777777777776"
        )

    def test_ConstantAuxiliaryMemoryRecursionExponential_negative(self):
        log.debug(ConstantAuxiliaryMemoryRecursionExponential(36, -1))
        self.assertEqual(
            ConstantAuxiliaryMemoryRecursionExponential(36, -1), 36**-1,
            "Not equal to 0.027777777777777776"
        )

    def test_IterativeConstantAuxiliaryMemoryRecursionExponential_negative(self):
        log.debug(IterativeConstantAuxiliaryMemoryRecursionExponential(36, -1))
        self.assertEqual(
            IterativeConstantAuxiliaryMemoryRecursionExponential(36, -1), 36**-1,
            "Not equal to 0.027777777777777776"
        )

    def test_VeryBasicExponential_zero(self):
        log.debug(VeryBasicExponential(36, 0))
        self.assertEqual(
            VeryBasicExponential(36, 0), 36**0,
            "Should equal 1"
        )

    def test_RecursionExponential_zero(self):
        log.debug(RecursionExponential(36, 0))
        self.assertEqual(
            RecursionExponential(36, 0), 36**0,
            "Should equal 1"
        )

    def test_ConstantAuxiliaryMemoryRecursionExponential_zero(self):
        log.debug(ConstantAuxiliaryMemoryRecursionExponential(36, 0))
        self.assertEqual(
            ConstantAuxiliaryMemoryRecursionExponential(36, 0), 36**0,
            "Should equal 1"
        )

    def test_IterativeConstantAuxiliaryMemoryRecursionExponential_zero(self):
        log.debug(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 0))
        self.assertEqual(
            IterativeConstantAuxiliaryMemoryRecursionExponential(36, 0), 36**0,
            "Should equal 1"
        )

    def test_VeryBasicExponential_one(self):
        log.debug(VeryBasicExponential(36, 1))
        self.assertEqual(
            VeryBasicExponential(36, 1), 36**1,
            "Should equal 36"
        )

    def test_RecursionExponential_one(self):
        log.debug(RecursionExponential(36, 1))
        self.assertEqual(
            RecursionExponential(36, 1), 36**1,
            "Should equal 36"
        )

    def test_ConstantAuxiliaryMemoryRecursionExponential_one(self):
        log.debug(ConstantAuxiliaryMemoryRecursionExponential(36, 1))
        self.assertEqual(
            ConstantAuxiliaryMemoryRecursionExponential(36, 1), 36**1,
            "Should equal 36"
        )

    def test_IterativeConstantAuxiliaryMemoryRecursionExponential_one(self):
        log.debug(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 1))
        self.assertEqual(
            IterativeConstantAuxiliaryMemoryRecursionExponential(36, 1), 36**1,
            "Should equal 36"
        )

    def test_VeryBasicExponential_even(self):
        log.debug(VeryBasicExponential(36, 12))
        self.assertEqual(
            VeryBasicExponential(36, 12), 36**12,
            "Should equal 4738381338321616896"
        )

    def test_RecursionExponential_even(self):
        log.debug(RecursionExponential(36, 12))
        self.assertEqual(
            RecursionExponential(36, 12), 36**12,
            "Should equal 4738381338321616896"
        )

    def test_ConstantAuxiliaryMemoryRecursionExponential_even(self):
        log.debug(ConstantAuxiliaryMemoryRecursionExponential(36, 12))
        self.assertEqual(
            ConstantAuxiliaryMemoryRecursionExponential(36, 12), 36**12,
            "Should equal 4738381338321616896"
        )

    def test_IterativeConstantAuxiliaryMemoryRecursionExponential_even(self):
        log.debug(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 12))
        self.assertEqual(
            IterativeConstantAuxiliaryMemoryRecursionExponential(36, 12), 36**12,
            "Should equal 4738381338321616896"
        )

    def test_VeryBasicExponential_odd(self):
        log.debug(VeryBasicExponential(36, 13))
        self.assertEqual(
            VeryBasicExponential(36, 13), 36**13,
            "Should equal 170581728179578208256"
        )

    def test_RecursionExponential_odd(self):
        log.debug(RecursionExponential(36, 13))
        self.assertEqual(
            RecursionExponential(36, 13), 36**13,
            "Should equal 170581728179578208256"
        )

    def test_ConstantAuxiliaryMemoryRecursionExponential_odd(self):
        log.debug(ConstantAuxiliaryMemoryRecursionExponential(36, 13))
        self.assertEqual(
            ConstantAuxiliaryMemoryRecursionExponential(36, 13), 36**13,
            "Should equal 170581728179578208256"
        )

    def test_IterativeConstantAuxiliaryMemoryRecursionExponential_odd(self):
        log.debug(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 13))
        self.assertEqual(
            IterativeConstantAuxiliaryMemoryRecursionExponential(36, 13), 36**13,
            "Should equal 170581728179578208256"
        )


if __name__ == '__main__':
    unittest.main()
