from typing import List, Optional

numeric = int | float

class SortAlgorithm:
    def __init__(self, listNum: List[numeric]):
        self.arr = listNum
        self.first_index = 0
        self.last_index = len(self.arr) - 1

    def _quickSort(self, listNum: List[numeric], first_index: int, last_index: int) -> None:
        if first_index < last_index:
            pivot = listNum[last_index]
            idx = first_index - 1
            for i in range(first_index, last_index):
                if listNum[i] < pivot:
                    idx += 1
                    listNum[idx], listNum[i] = listNum[i], listNum[idx]
            listNum[idx+1], listNum[last_index] = listNum[last_index], listNum[idx+1]
            partition_index = idx + 1
            self._quickSort(listNum, first_index, partition_index-1)
            self._quickSort(listNum, partition_index+1, last_index)

    def quickSort(self) -> None:
        self._quickSort(self.arr, self.first_index, self.last_index)

arr = [10, 7, 8, 9, 1, 5]
sortAlgo = SortAlgorithm(arr)
sortAlgo.quickSort()

print(arr)
