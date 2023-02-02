import unittest
import logging

log = logging.getLogger(__name__)


def reverseCipher(text: str) -> str:
    return text[::-1]

class TestReverseCipher(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")
        self.decryptedStr = "Hello babe, how are you?. I'm on the way at home, i'll be at home at 8:30 PM"
        self.encryptedStr = "MP 03:8 ta emoh ta eb ll'i ,emoh ta yaw eht no m'I .?uoy era woh ,ebab olleH"

    def test_ReverseCipher_encrypt(self):
        log.debug(reverseCipher(self.decryptedStr))
        self.assertEqual(
            reverseCipher(self.decryptedStr),
            self.encryptedStr,
            f'Not equal'
        )

    def test_ReverseCipher_decrypt(self):
        log.debug(reverseCipher(self.encryptedStr))
        self.assertEqual(
            reverseCipher(self.encryptedStr),
            self.decryptedStr,
            f'Not equal'
        )

if __name__ == '__main__':
    unittest.main()


print(reverseCipher('Hello babe, how are you?. I\'m on the way at home, i\'ll be at home at 8:30 PM'))
print(reverseCipher('MP 03:8 ta emoh ta eb ll\'i ,emoh ta yaw eht no m\'I .?uoy era woh ,ebab olleH'))
