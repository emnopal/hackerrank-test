def DigitalRoots(n: int) -> int:
    str_n = list(str(n))
    length_n = len(str_n)
    while length_n > 1:
        n = sum(map(int, list(str(n))))
        str_n = list(str(n))
        length_n = len(str_n)
    return n

print(DigitalRoots(12345)) # 6
print(DigitalRoots(16)) # 7
print(DigitalRoots(942)) # 6
print(DigitalRoots(132189)) # 6
print(DigitalRoots(493193)) # 2
