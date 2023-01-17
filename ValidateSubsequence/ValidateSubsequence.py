from typing import List

def ValidateSubsequenceFirst(arr: List[int], subArr: List[int]) -> bool:
    return subArr == [i for i in arr for j in subArr if i == j]

def ValidateSubsequenceSecond(arr: List[int], subArr: List[int]) -> bool:
    subseq = 0
    for i in arr:
        for j in subArr:
            if i == j:
                subseq += 1
    return subseq == len(subArr)

def ValidateSubsequenceThird(arr: List[int], subArr: List[int]) -> bool:
    return set(subArr).issubset(set(arr))

def ValidateSubsequenceFour(arr: List[int], subArr: List[int]) -> bool:
    subArrIndex = 0
    arrIndex = 0
    while subArrIndex < len(subArr) and arrIndex < len(arr):
        if subArr[subArrIndex] == arr[arrIndex]:
            subArrIndex += 1
        arrIndex += 1
    return subArrIndex == len(subArr)

if __name__ == '__main__':
    print(ValidateSubsequenceFirst([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    print(ValidateSubsequenceSecond([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    print(ValidateSubsequenceThird([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
    print(ValidateSubsequenceFour([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
