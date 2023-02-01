import unittest
import logging
from functools import reduce

log = logging.getLogger(__name__)


def factorialGenerator(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def factorialGeneratorOneLine(n):
    return 1 if n < 1 else reduce(lambda x,y: x*y, range(1, n+1))


def trailingZeros(n, f):

    trailing_zeros = f(n)

    result = 0

    while True:
        if not trailing_zeros % 10 == 0:
            break
        result += 1
        trailing_zeros //= 10  # `//` can handle big number but `/` can't

    return result


def trailingZerosFactorial(n):
    factorial = 1
    result = 0

    for i in range(1, n + 1):
        factorial *= i

    while True:
        if not factorial % 10 == 0:
            break
        result += 1
        factorial //= 10  # `//` can handle big number but `/` can't

    return result


def trailingZerosFactorialReduce(n):
    factorial = 1 if n < 1 else reduce(lambda x,y: x*y, range(1, n+1))
    result = 0

    while True:
        if not factorial % 10 == 0:
            break
        result += 1
        factorial //= 10  # `//` can handle big number but `/` can't

    return result


class FactorialTrailing(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() Result: %(message)s")

    # Factorial Generator

    def test_factorialGenerator_zero(self):
        log.debug(factorialGenerator(0))
        self.assertEqual(
            factorialGenerator(0), 1,
            "Should equal 1"
        )

    def test_factorialGenerator_one(self):
        log.debug(factorialGenerator(1))
        self.assertEqual(
            factorialGenerator(1), 1,
            "Should equal 1"
        )

    def test_factorialGenerator_small(self):
        log.debug(factorialGenerator(5))
        self.assertEqual(
            factorialGenerator(5), 120,
            "Should equal 120"
        )

    def test_factorialGenerator_medium(self):
        log.debug(factorialGenerator(12))
        self.assertEqual(
            factorialGenerator(12), 479001600,
            "Should equal 479001600"
        )

    def test_factorialGenerator_big(self):
        log.debug(factorialGenerator(20))
        self.assertEqual(
            factorialGenerator(20), 2432902008176640000,
            "Should equal 2432902008176640000"
        )

    def test_factorialGenerator_huge(self):
        log.debug(factorialGenerator(50))
        self.assertEqual(
            factorialGenerator(50), 30414093201713378043612608166064768844377641568960512000000000000,
            "Should equal 30414093201713378043612608166064768844377641568960512000000000000"
        )

    # Factorial Generator One Line

    def test_factorialGeneratorOneLine_zero(self):
        log.debug(factorialGeneratorOneLine(0))
        self.assertEqual(
            factorialGeneratorOneLine(0), 1,
            "Should equal 1"
        )

    def test_factorialGeneratorOneLine_one(self):
        log.debug(factorialGeneratorOneLine(1))
        self.assertEqual(
            factorialGeneratorOneLine(1), 1,
            "Should equal 1"
        )

    def test_factorialGeneratorOneLine_small(self):
        log.debug(factorialGeneratorOneLine(5))
        self.assertEqual(
            factorialGeneratorOneLine(5), 120,
            "Should equal 120"
        )

    def test_factorialGeneratorOneLine_medium(self):
        log.debug(factorialGeneratorOneLine(12))
        self.assertEqual(
            factorialGeneratorOneLine(12), 479001600,
            "Should equal 479001600"
        )

    def test_factorialGeneratorOneLine_big(self):
        log.debug(factorialGeneratorOneLine(20))
        self.assertEqual(
            factorialGeneratorOneLine(20), 2432902008176640000,
            "Should equal 2432902008176640000"
        )

    def test_factorialGeneratorOneLine_huge(self):
        log.debug(factorialGeneratorOneLine(50))
        self.assertEqual(
            factorialGeneratorOneLine(50), 30414093201713378043612608166064768844377641568960512000000000000,
            "Should equal 30414093201713378043612608166064768844377641568960512000000000000"
        )

    # Trailing Zeros with Factorial

    def test_trailingZeros_zero(self):
        log.debug(trailingZeros(0, factorialGenerator))
        self.assertEqual(
            trailingZeros(0, factorialGenerator), 0,
            "Should equal 0"
        )

    def test_trailingZeros_one(self):
        log.debug(trailingZeros(1, factorialGenerator))
        self.assertEqual(
            trailingZeros(1, factorialGenerator), 0,
            "Should equal 0"
        )

    def test_trailingZeros_small(self):
        log.debug(trailingZeros(5, factorialGenerator))
        self.assertEqual(
            trailingZeros(5, factorialGenerator), 1,
            "Should equal 1"
        )

    def test_trailingZeros_medium(self):
        log.debug(trailingZeros(12, factorialGenerator))
        self.assertEqual(
            trailingZeros(12, factorialGenerator), 2,
            "Should equal 2"
        )

    def test_trailingZeros_big(self):
        log.debug(trailingZeros(20, factorialGenerator))
        self.assertEqual(
            trailingZeros(20, factorialGenerator), 4,
            "Should equal 4"
        )

    def test_trailingZeros_huge(self):
        log.debug(trailingZeros(50, factorialGenerator))
        self.assertEqual(
            trailingZeros(50, factorialGenerator), 12,
            "Should equal 12"
        )

    # Trailing Zeros with OneLineFactorial

    def test_trailingZerosOneLine_zero(self):
        log.debug(trailingZeros(0, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(0, factorialGeneratorOneLine), 0,
            "Should equal 0"
        )

    def test_trailingZerosOneLine_one(self):
        log.debug(trailingZeros(1, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(1, factorialGeneratorOneLine), 0,
            "Should equal 0"
        )

    def test_trailingZerosOneLine_small(self):
        log.debug(trailingZeros(5, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(5, factorialGeneratorOneLine), 1,
            "Should equal 1"
        )

    def test_trailingZerosOneLine_medium(self):
        log.debug(trailingZeros(12, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(12, factorialGeneratorOneLine), 2,
            "Should equal 2"
        )

    def test_trailingZerosOneLine_big(self):
        log.debug(trailingZeros(20, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(20, factorialGeneratorOneLine), 4,
            "Should equal 4"
        )

    def test_trailingZerosOneLine_huge(self):
        log.debug(trailingZeros(50, factorialGeneratorOneLine))
        self.assertEqual(
            trailingZeros(50, factorialGeneratorOneLine), 12,
            "Should equal 12"
        )

    # Trailing Zeros without function wrapper

    def test_trailingZerosNoFuncWrapper_zero(self):
        log.debug(trailingZerosFactorial(0))
        self.assertEqual(
            trailingZerosFactorial(0), 0,
            "Should equal 0"
        )

    def test_trailingZerosNoFuncWrapper_one(self):
        log.debug(trailingZerosFactorial(1))
        self.assertEqual(
            trailingZerosFactorial(1), 0,
            "Should equal 0"
        )

    def test_trailingZerosNoFuncWrapper_small(self):
        log.debug(trailingZerosFactorial(5))
        self.assertEqual(
            trailingZerosFactorial(5), 1,
            "Should equal 1"
        )

    def test_trailingZerosNoFuncWrapper_medium(self):
        log.debug(trailingZerosFactorial(12))
        self.assertEqual(
            trailingZerosFactorial(12), 2,
            "Should equal 2"
        )

    def test_trailingZerosNoFuncWrapper_big(self):
        log.debug(trailingZerosFactorial(20))
        self.assertEqual(
            trailingZerosFactorial(20), 4,
            "Should equal 4"
        )

    def test_trailingZerosNoFuncWrapper_huge(self):
        log.debug(trailingZerosFactorial(50))
        self.assertEqual(
            trailingZerosFactorial(50), 12,
            "Should equal 12"
        )

    # Trailing Zeros with OneLineFactorial without Function Wrapper

    def test_trailingZerosOneLineNoFuncWrapper_zero(self):
        log.debug(trailingZerosFactorialReduce(0))
        self.assertEqual(
            trailingZerosFactorialReduce(0), 0,
            "Should equal 0"
        )

    def test_trailingZerosOneLineNoFuncWrapper_one(self):
        log.debug(trailingZerosFactorialReduce(1))
        self.assertEqual(
            trailingZerosFactorialReduce(1), 0,
            "Should equal 0"
        )

    def test_trailingZerosOneLineNoFuncWrapper_small(self):
        log.debug(trailingZerosFactorialReduce(5))
        self.assertEqual(
            trailingZerosFactorialReduce(5), 1,
            "Should equal 1"
        )

    def test_trailingZerosOneLineNoFuncWrapper_medium(self):
        log.debug(trailingZerosFactorialReduce(12))
        self.assertEqual(
            trailingZerosFactorialReduce(12), 2,
            "Should equal 2"
        )

    def test_trailingZerosOneLineNoFuncWrapper_big(self):
        log.debug(trailingZerosFactorialReduce(20))
        self.assertEqual(
            trailingZerosFactorialReduce(20), 4,
            "Should equal 4"
        )

    def test_trailingZerosOneLineNoFuncWrapper_huge(self):
        log.debug(trailingZerosFactorialReduce(50))
        self.assertEqual(
            trailingZerosFactorialReduce(50), 12,
            "Should equal 12"
        )


if __name__ == '__main__':
    unittest.main()
