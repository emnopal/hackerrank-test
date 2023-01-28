import unittest
import logging

log = logging.getLogger(__name__)


def EasiestFactorial(num: int) -> int:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def FactorialRecursion(num: int) -> int:
    if num < 1:
        return 1
    return num * FactorialRecursion(num - 1)


def FactorialRecursionOneLine(num: int) -> int:
    return 1 if num < 1 else num * FactorialRecursion(num - 1)


class TestFactorial(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")

    def test_EasiestFactorial_normal(self):
        log.debug(EasiestFactorial(5))
        self.assertEqual(
            EasiestFactorial(5), 1*2*3*4*5,
            "Should equal 120"
        )

    def test_FactorialRecursion_normal(self):
        log.debug(FactorialRecursion(5))
        self.assertEqual(
            FactorialRecursion(5), 1*2*3*4*5,
            "Should equal 120"
        )

    def test_FactorialRecursionOneLine_normal(self):
        log.debug(FactorialRecursionOneLine(5))
        self.assertEqual(
            FactorialRecursionOneLine(5), 1*2*3*4*5,
            "Should equal 120"
        )

    def test_EasiestFactorial_one(self):
        log.debug(EasiestFactorial(1))
        self.assertEqual(
            EasiestFactorial(1), 1,
            "Should equal 1"
        )

    def test_FactorialRecursion_one(self):
        log.debug(FactorialRecursion(1))
        self.assertEqual(
            FactorialRecursion(1), 1,
            "Should equal 1"
        )

    def test_FactorialRecursionOneLine_one(self):
        log.debug(FactorialRecursionOneLine(1))
        self.assertEqual(
            FactorialRecursionOneLine(1), 1,
            "Should equal 1"
        )

    def test_EasiestFactorial_zero(self):
        log.debug(EasiestFactorial(0))
        self.assertEqual(
            EasiestFactorial(0), 1,
            "Should equal 1"
        )

    def test_FactorialRecursion_zero(self):
        log.debug(FactorialRecursion(0))
        self.assertEqual(
            FactorialRecursion(0), 1,
            "Should equal 1"
        )

    def test_FactorialRecursionOneLine_zero(self):
        log.debug(FactorialRecursionOneLine(0))
        self.assertEqual(
            FactorialRecursionOneLine(0), 1,
            "Should equal 1"
        )

    def test_EasiestFactorial_bigNum(self):
        log.debug(EasiestFactorial(20))
        self.assertEqual(
            EasiestFactorial(20), 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20,
            "Should equal 2432902008176640000"
        )

    def test_FactorialRecursion_bigNum(self):
        log.debug(FactorialRecursion(20))
        self.assertEqual(
            FactorialRecursion(20), 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20,
            "Should equal 2432902008176640000"
        )

    def test_FactorialRecursionOneLine_bigNum(self):
        log.debug(FactorialRecursionOneLine(20))
        self.assertEqual(
            FactorialRecursionOneLine(20), 1*2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20,
            "Should equal 2432902008176640000"
        )


if __name__ == '__main__':
    unittest.main()
