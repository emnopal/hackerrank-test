import random


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
        return NotImplementedError

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

if __name__ == '__main__':
    print(CaesarChiper("Hello babe, how are you?. I'm on the way at home, i'll be at home at 8:30 PM", 37))
    print(CaesarChiper("m«²²µE¨§¨«QE®µ½E§¸«E¿µ»dSEnL³Eµ´Eº®«E½§¿E§ºE®µ³«QE¯L²²E¨«E§ºE®µ³«E§ºE]_XUEur", 37, method='decrypt'))
