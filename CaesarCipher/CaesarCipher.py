import unittest
import logging

log = logging.getLogger(__name__)


def SimplestCaesarCipher(text: str, shift: int = 4, method: str = 'encrypt'):
    result = ""

    if method == 'decrypt':
        shift *= -1

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")
        self.decryptedStr = "Hello babe, how are you?. I'm on the way at home, i'll be at home at 8:30 PM"
        self.encryptedStr = "Tqxxa nmnq, tai mdq kag?. U'y az ftq imk mf tayq, u'xx nq mf tayq mf 8:30 BY"
        self.shift = 12

    def test_SimplestCaesarCipher_encrypt(self):
        log.debug(SimplestCaesarCipher(self.decryptedStr, self.shift))
        self.assertEqual(
            SimplestCaesarCipher(self.decryptedStr, self.shift),
            self.encryptedStr,
            f'Not equal'
        )

    def test_SimplestCaesarCipher_decrypt(self):
        log.debug(SimplestCaesarCipher(self.encryptedStr, self.shift, 'decrypt'))
        self.assertEqual(
            SimplestCaesarCipher(self.encryptedStr, self.shift, 'decrypt'),
            self.decryptedStr,
            f'Not equal'
        )

if __name__ == '__main__':
    unittest.main()
