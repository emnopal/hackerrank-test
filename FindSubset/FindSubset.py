from itertools import combinations, chain

def FindSubsetOne(arr):
    comb_arr = []
    for i in range(len(arr)+1):
        comb_arr.append(combinations(arr, i))
    return list(map(lambda x: list(x), chain.from_iterable(comb_arr)))

def FindSubsetOneAlt(arr):
    comb_arr = []
    for i in range(len(arr)+1):
        comb_arr.append(map(lambda x: list(x), combinations(arr, i)))
    return [comb for iter_comb in comb_arr for comb in iter_comb]

def FindSubsetTwo(arr):
    return list(map(lambda x: list(x), chain.from_iterable([combinations(arr, i) for i in range(len(arr) + 1)])))

def combinations_alt(lst, n):
    if n==0:
        return [[]]

    l=[]

    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i+1:]
        for p in combinations_alt(remLst, n-1):
            l.append([m]+p)
    return l

def FindSubsetThree(arr):
    comb_arr = []
    for i in range(len(arr)+1):
        comb_arr.append(combinations_alt(arr, i))
    return [comb for iter_comb in comb_arr for comb in iter_comb]

if __name__ == '__main__':
    arr = [4,5,6]
    print(FindSubsetOne(arr))
    print(FindSubsetOneAlt(arr))
    print(FindSubsetTwo(arr))
    print(FindSubsetThree(arr))

