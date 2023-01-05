from collections import defaultdict
from typing import List, Dict

def RemainderSorting(strArr: List[str]) -> List[str]:

    arr: defaultdict[int, List[str]] = defaultdict(list)
    for ele in strArr:
        arr[len(ele)%3].append(ele)

    arr_sorted_value: Dict[int, List[str]] = {}
    for key, value in arr.items():
        arr_sorted_value[key] = sorted(value)

    arr_sorted_key = dict(sorted(arr_sorted_value.items()))

    arr_sorted_final = [ele for ele_list in list(arr_sorted_key.values()) for ele in ele_list]

    return arr_sorted_final

test = RemainderSorting(["Colorado", "Utah", "Montana", "Wisconsin", "Oregon", "Maine"])
print(test)
