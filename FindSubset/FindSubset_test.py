import unittest
import logging
from itertools import combinations, chain
from typing import List, TypeVar

log = logging.getLogger(__name__)

Numeric = TypeVar("Numeric", int, float)
Text = TypeVar("Text", str, None)


def FindSubsetOne(arrNum: List[Numeric]) -> List[List[Numeric]]:
    comb_arr = []
    for i in range(len(arrNum) + 1):
        comb_arr.append(combinations(arrNum, i))
    return list(map(lambda x: list(x), chain.from_iterable(comb_arr)))


def FindSubsetOneAlt(arrNum: List[Numeric]) -> List[List[Numeric]]:
    comb_arr = []
    for i in range(len(arrNum) + 1):
        comb_arr.append(map(lambda x: list(x), combinations(arrNum, i)))
    return [comb for iter_comb in comb_arr for comb in iter_comb]


def FindSubsetTwo(arrNum: List[Numeric]) -> List[List[Numeric]]:
    return list(map(lambda x: list(x), chain.from_iterable([combinations(arrNum, i) for i in range(len(arrNum) + 1)])))


def combinations_alt(lst: List[Numeric | Text], n: int) -> List[List[Numeric | Text]]:
    if n == 0:
        return [[]]

    combList = []

    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1:]
        for p in combinations_alt(remLst, n - 1):
            combList.append([m] + p)
    return combList


def FindSubsetThree(arrNum: List[Numeric]) -> List[List[Numeric]]:
    comb_arr = []
    for i in range(len(arrNum) + 1):
        comb_arr.append(combinations_alt(arrNum, i))
    return [comb for iter_comb in comb_arr for comb in iter_comb]


class TestFindSubset(unittest.TestCase):

    def setUp(self):
        loglevel = logging.DEBUG
        logging.basicConfig(level=loglevel, format="%(filename)s:%(lineno)s:%(funcName)20s() %(message)s")
        self.arrNum = [4, 5, 6]
        self.arrNumResult = [[], [4], [5], [6], [4, 5], [4, 6], [5, 6], [4, 5, 6]]

    def test_FindSubsetOne(self):
        log.debug(FindSubsetOne(self.arrNum))
        self.assertEqual(FindSubsetOne(self.arrNum), self.arrNumResult, f'Should be {self.arrNumResult}')

    def test_FindSubsetOneAlt(self):
        log.debug(FindSubsetOneAlt(self.arrNum))
        self.assertEqual(FindSubsetOneAlt(self.arrNum), self.arrNumResult, f'Should be {self.arrNumResult}')

    def test_FindSubsetTwo(self):
        log.debug(FindSubsetTwo(self.arrNum))
        self.assertEqual(FindSubsetTwo(self.arrNum), self.arrNumResult, f'Should be {self.arrNumResult}')

    def test_FindSubsetThree(self):
        log.debug(FindSubsetThree(self.arrNum))
        self.assertEqual(FindSubsetThree(self.arrNum), self.arrNumResult, f'Should be {self.arrNumResult}')


if __name__ == '__main__':
    unittest.main()
