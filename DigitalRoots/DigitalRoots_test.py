import unittest
import logging

log = logging.getLogger(__name__)


def DigitalRoots(n: int) -> int:
    str_n = list(str(n))
    length_n = len(str_n)
    while length_n > 1:
        n = sum(map(int, list(str(n))))
        str_n = list(str(n))
        length_n = len(str_n)
    return n


class TestDigitalRoots(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")

    def test_digital_roots_1(self):
        log.debug(DigitalRoots(12345))
        self.assertEqual(DigitalRoots(12345), 6, 'Not equal 6')

    def test_digital_roots_2(self):
        log.debug(DigitalRoots(16))
        self.assertEqual(DigitalRoots(16), 7, 'Not equal 7')

    def test_digital_roots_3(self):
        log.debug(DigitalRoots(942))
        self.assertEqual(DigitalRoots(942), 6, 'Not equal 6')

    def test_digital_roots_4(self):
        log.debug(DigitalRoots(132189))
        self.assertEqual(DigitalRoots(132189), 6, 'Not equal 6')

    def test_digital_roots_5(self):
        log.debug(DigitalRoots(493193))
        self.assertEqual(DigitalRoots(493193), 2, 'Not equal 2')


if __name__ == '__main__':
    unittest.main()
