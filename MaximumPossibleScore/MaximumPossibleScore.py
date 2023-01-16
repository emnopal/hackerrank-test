import math
from typing import List, Tuple

# from iterating the array
def GetMaximumScoreFirstWay(arr: List[int], k: int) -> Tuple[List[int], int]:
    k_init = 0
    arr_index = 0
    arr_score = 0

    while k_init <= k:
        try:
            if math.ceil(arr[arr_index]/3) > 1:
                arr_score += arr[arr_index]
                arr[arr_index] = math.ceil(arr[arr_index]/3)
            else:
                arr_index += 1
                k_init += 1
        except IndexError:
            break

    return arr, arr_score

# from choosing element inside array
def GetMaximumScoreSecondWay(arr: List[int], k: int) -> Tuple[List[int], int]:
    score = 0
    for _ in range(k):
        choice = int(input())
        score += choice
        arr = [math.ceil(choice/3) if x==choice else x for x in arr]
        print("score = ",score, "and arr = " ,arr)
    return arr, score

if __name__ == '__main__':

    arr = [20, 4, 3, 1, 9]
    arr_result, arr_score = GetMaximumScoreFirstWay(arr, 4)
    print(arr_result, arr_score)

    arr = [4, 5, 18, 1]
    arr_result, arr_score = GetMaximumScoreFirstWay(arr, 3)
    print(arr_result, arr_score)

    arr = [1,1,1]
    arr_result, arr_score = GetMaximumScoreFirstWay(arr, 2)
    print(arr_result, arr_score)

    # arr = [20, 4, 3, 1, 9]
    # arr_result, arr_score = GetMaximumScoreSecondWay(arr, 4)
    # print(arr_result, arr_score)

    # arr = [4, 5, 18, 1]
    # arr_result, arr_score = GetMaximumScoreSecondWay(arr, 3)
    # print(arr_result, arr_score)

    arr = [1,1,1]
    arr_result, arr_score = GetMaximumScoreSecondWay(arr, 2)
    print(arr_result, arr_score)
