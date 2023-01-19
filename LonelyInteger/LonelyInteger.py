from collections import defaultdict
from functools import reduce
from typing import List

def LonelyIntegerFirst(integer_list: List[int]) -> int:
    for i in range(len(integer_list)):
        count = 0
        for j in range(len(integer_list)):
            if integer_list[i] == integer_list[j]:
                count += 1
        if count == 1:
            return integer_list[i]

def LonelyIntegerSecond(integer_list: List[int]) -> int:
    return reduce(lambda x, y : x ^ y, integer_list)

def LonelyIntegerThird(integer_list: List[int]) -> int:
    ans = 0
    for i in range(len(integer_list)):
        ans ^= integer_list[i]
    return ans

def LonelyIntegerFourth(integer_list: List[int]) -> int:
    return list(filter(lambda x: integer_list.count(x)==1, integer_list))[0]

def LonelyIntegerFifth(integer_list: List[int]) -> int:
    for i in set(integer_list):
        if integer_list.count(i) == 1:
            return i

def LonelyIntegerSixth(integer_list: List[int]) -> int:
    a = defaultdict(list)
    for i in integer_list:
        a[i].append(i)
    return [k for k, v in dict(a).items() if len(v) == 1][0]

def LonelyIntegerSeventh(integer_list: List[int]) -> int:
    for i in integer_list:
        if integer_list.count(i) == 1:
            return i

print(LonelyIntegerFirst([1,2,3,4,3,2,1]))
print(LonelyIntegerSecond([1,2,3,4,3,2,1]))
print(LonelyIntegerThird([1,2,3,4,3,2,1]))
print(LonelyIntegerFourth([1,2,3,4,3,2,1]))
print(LonelyIntegerFifth([1,2,3,4,3,2,1]))
print(LonelyIntegerSixth([1,2,3,4,3,2,1]))
print(LonelyIntegerSeventh([1,2,3,4,3,2,1]))
