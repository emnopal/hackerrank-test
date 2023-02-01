BASIC_LATIN = "".join(map(chr, range(0x0020, 0x007e+1)))
LATIN_SUPPLEMENT = "".join(map(chr, range(0x00a0, 0x00ff+1)))
LATIN_EXTENDED_A = "".join(map(chr, range(0x0100, 0x017f+1)))
LATIN_EXTENDED_B = "".join(map(chr, range(0x0180, 0x024f+1)))
IPA_EXTENSION = "".join(map(chr, range(0x0250, 0x02af+1)))
LATIN_EXTENDED_ADDITIONAL = "".join(map(chr, range(0x1e00, 0x1eff+1)))
ALL_POSSIBLE_LATIN_CHARS = BASIC_LATIN + LATIN_SUPPLEMENT + LATIN_EXTENDED_A + LATIN_EXTENDED_B + IPA_EXTENSION + LATIN_EXTENDED_ADDITIONAL
