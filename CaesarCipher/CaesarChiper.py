import random
import unittest
import logging

log = logging.getLogger(__name__)


def CaesarChiper(
    text: str,
    shift: int = 4,
    method: str = 'encrypt',
    char_unicode: str = 'latin'
) -> str:

    if char_unicode == 'latin':
        BASIC_LATIN = "".join(map(chr, range(0x0020, 0x007e+1)))
        LATIN_SUPPLEMENT = "".join(map(chr, range(0x00a0, 0x00ff+1)))
        LATIN_EXTENDED_A = "".join(map(chr, range(0x0100, 0x017f+1)))
        LATIN_EXTENDED_B = "".join(map(chr, range(0x0180, 0x024f+1)))
        IPA_EXTENSION = "".join(map(chr, range(0x0250, 0x02af+1)))
        LATIN_EXTENDED_ADDITIONAL = "".join(map(chr, range(0x1e00, 0x1eff+1)))
        ALL_POSSIBLE_LATIN_CHARS = BASIC_LATIN + LATIN_SUPPLEMENT + LATIN_EXTENDED_A + LATIN_EXTENDED_B + IPA_EXTENSION + LATIN_EXTENDED_ADDITIONAL
    else:
        raise NotImplementedError

    result = ''

    for char in text:
        if char in ALL_POSSIBLE_LATIN_CHARS:
            char_idx = ALL_POSSIBLE_LATIN_CHARS.find(char)

            if method == 'decrypt':
                method_idx = char_idx - shift
            else:
                method_idx = char_idx + shift

            # handle array index out of range
            if method_idx >= len(ALL_POSSIBLE_LATIN_CHARS):
                method_idx -= len(ALL_POSSIBLE_LATIN_CHARS)
            elif method_idx < 0:
                method_idx += len(ALL_POSSIBLE_LATIN_CHARS)

            result += ALL_POSSIBLE_LATIN_CHARS[method_idx]
        else:
            result += char

    return result

class TestCaesarChiper(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")
        self.decryptedStr = "Hello babe, how are you?. I'm on the way at home, i'll be at home at 8:30 PM"
        self.encryptedStr = "m«²²µE¨§¨«QE®µ½E§¸«E¿µ»dSEnL³Eµ´Eº®«E½§¿E§ºE®µ³«QE¯L²²E¨«E§ºE®µ³«E§ºE]_XUEur"
        self.shift = 37

    def test_CaesarChiper_encrypt(self):
        log.debug(CaesarChiper(self.decryptedStr, self.shift))
        self.assertEqual(
            CaesarChiper(self.decryptedStr, self.shift),
            self.encryptedStr,
            f'Not equal'
        )

    def test_CaesarChiper_decrypt(self):
        log.debug(CaesarChiper(self.encryptedStr, self.shift, 'decrypt'))
        self.assertEqual(
            CaesarChiper(self.encryptedStr, self.shift, 'decrypt'),
            self.decryptedStr,
            f'Not equal'
        )

    def test_CaesarChiper_encrypt_no_latin(self):
        self.assertRaises(
            NotImplementedError,
            CaesarChiper,
            self.decryptedStr, self.shift, 'decrypt', 'arabic'
        )

    def test_CaesarChiper_decrypt_no_latin(self):
        self.assertRaises(
            NotImplementedError,
            CaesarChiper,
            self.decryptedStr, self.shift, 'decrypt', 'arabic'
        )

if __name__ == '__main__':
    unittest.main()
