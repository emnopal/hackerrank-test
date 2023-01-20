def Flipping32BitsFirst(n: int) -> int:
    bits = f'{n:032b}'
    bits_reverse = ''
    for i in bits:
        if i == '0':
            bits_reverse += '1'
        else:
            bits_reverse += '0'
    return int(bits_reverse, 2)

def Flipping32BitsFirstAlt(n: int) -> int:
    bits = f'{n:032b}'
    bits_reverse = ''
    for i in bits:
        if i == '0':
            bits_reverse += '1'
        else:
            bits_reverse += '0'
    return eval("0b" + bits_reverse)

def Flipping32BitsSecond(n: int) -> int:
    bits = f'{n:032b}'
    bits = bits.replace("0", "n").replace("1", "0").replace("n", "1")
    return int(bits, 2)

def Flipping32BitsSecondAlt(n: int) -> int:
    bits = f'{n:032b}'
    bits = bits.replace("0", "n").replace("1", "0").replace("n", "1")
    return eval("0b" + bits)

def Flipping32BitsThird(n: int) -> int:
    return ~n & ((2**32)-1)

def Flipping32BitsForth(n: int) -> int:
    return ((2**32)-1) - n

def Flipping32BitsFifth(n: int) -> int:
    return int(~n & 0xFFFFFFFF)

def Flipping32BitsSixth(n: int) -> int:
    bins = bin(n)[2:]
    bins32 = "".join("0" for _ in range(32 - len(bins)))
    bins = "".join(bins32 + bins)
    bins_invert = "".join("0" if b == "1" else "1" for b in bins)
    return int(bins_invert, 2)

print(Flipping32BitsFirst(0))
print(Flipping32BitsFirstAlt(0))
print(Flipping32BitsSecond(0))
print(Flipping32BitsSecondAlt(0))
print(Flipping32BitsThird(0))
print(Flipping32BitsForth(0))
print(Flipping32BitsFifth(0))
print(Flipping32BitsSixth(0))
