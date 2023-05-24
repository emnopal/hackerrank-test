from typing import Dict


def isAnagramSimple(strA: str, strB: str) -> bool:
    return sorted(strA) == sorted(strB)

def isAnagramSimple2(strA: str, strB: str) -> bool:

    def str_word_to_dict(str_word: str) -> Dict[str, int]:
        str_dict: Dict[str, int] = {}
        for word in str_word:
            if word in str_dict:
                str_dict[word] += 1
            str_dict[word] = 1
        return str_dict

    strA_word = str_word_to_dict(strA)
    strB_word = str_word_to_dict(strB)

    for word in strA_word:
        if word not in strB_word:
            return False
        if strA_word[word] != strB_word[word]:
            return False

    return True

if __name__ == '__main__':
    print(isAnagramSimple('hydroxydeoxycorticosterones', 'hydroxydesoxycorticosterone')) # true
    print(isAnagramSimple('undefinability', 'unidentifiably')) # true
    print(isAnagramSimple('thermonastically', 'hematocrystallin')) # true
    print(isAnagramSimple('false', 'self')) # true
    print(isAnagramSimple2('hydroxydeoxycorticosterones', 'hydroxydesoxycorticosterone')) # true
    print(isAnagramSimple2('undefinability', 'unidentifiably')) # true
    print(isAnagramSimple2('thermonastically', 'hematocrystallin')) # true
    print(isAnagramSimple2('false', 'self')) # true
