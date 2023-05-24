<?php

namespace Anagram {

    function strToArraySort(string $str): array {
        $strArr = str_split($str);
        sort($strArr);
        return $strArr;
    }

    function isAnagramSimple(string $strA, string $strB): bool {
        return strToArraySort($strA) === strToArraySort($strB);
    }

    echo var_dump(isAnagramSimple('hydroxydeoxycorticosterones', 'hydroxydesoxycorticosterone'));
    echo var_dump(isAnagramSimple('false', 'self'));
}
