import unittest
import logging
import time

log = logging.getLogger(__name__)


def DigitalRoots(n: int) -> int:
    str_n = str(n)
    length_n = len(str_n)
    while length_n > 1:
        n = sum(map(int, str(n)))
        str_n = str(n)
        length_n = len(str_n)
    return n

def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

def digital_root2(n):
    return n % 9 or n and 9


class TestDigitalRoots(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")

    def test_digital_roots_1(self):
        start_time = time.time()
        log.debug(DigitalRoots(12345))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(DigitalRoots(12345), 6, 'Not equal 6')

    def test_digital_roots_6(self):
        start_time = time.time()
        log.debug(digital_root(12345))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root(12345), 6, 'Not equal 6')

    def test_digital_roots_11(self):
        start_time = time.time()
        log.debug(digital_root2(12345))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root2(12345), 6, 'Not equal 6')

    def test_digital_roots_2(self):
        start_time = time.time()
        log.debug(DigitalRoots(16))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(DigitalRoots(16), 7, 'Not equal 7')

    def test_digital_roots_7(self):
        start_time = time.time()
        log.debug(digital_root(16))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root(16), 7, 'Not equal 7')

    def test_digital_roots_12(self):
        start_time = time.time()
        log.debug(digital_root2(16))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root2(16), 7, 'Not equal 7')

    def test_digital_roots_3(self):
        start_time = time.time()
        log.debug(DigitalRoots(942))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(DigitalRoots(942), 6, 'Not equal 6')

    def test_digital_roots_8(self):
        start_time = time.time()
        log.debug(digital_root(942))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root(942), 6, 'Not equal 6')

    def test_digital_roots_13(self):
        start_time = time.time()
        log.debug(digital_root2(942))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root2(942), 6, 'Not equal 6')

    def test_digital_roots_4(self):
        start_time = time.time()
        log.debug(DigitalRoots(132189))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(DigitalRoots(132189), 6, 'Not equal 6')

    def test_digital_roots_9(self):
        start_time = time.time()
        log.debug(digital_root(132189))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root(132189), 6, 'Not equal 6')

    def test_digital_roots_14(self):
        start_time = time.time()
        log.debug(digital_root2(132189))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root2(132189), 6, 'Not equal 6')

    def test_digital_roots_5(self):
        start_time = time.time()
        log.debug(DigitalRoots(493193))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(DigitalRoots(493193), 2, 'Not equal 2')

    def test_digital_roots_15(self):
        start_time = time.time()
        log.debug(digital_root2(493193))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root2(493193), 2, 'Not equal 2')

    def test_digital_roots_10(self):
        start_time = time.time()
        log.debug(digital_root(493193))
        log.debug('time execution: %s' % (time.time() - start_time))
        self.assertEqual(digital_root(493193), 2, 'Not equal 2')

if __name__ == '__main__':
    unittest.main()
