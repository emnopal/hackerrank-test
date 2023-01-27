def VeryBasicExponental(x, n):
    total = 1
    for _ in range(n):
        total *= x
    return total

def RecursionExponential(x, n):
    if n < 0:
        return RecursionExponential(1/x, -n)
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 1:
        return x * RecursionExponential(x*x, (n-1)/2)
    return RecursionExponential(x*x, n/2)

# Exponential by Squaring

def AuxiliaryMemoryRecursionExponential(y, x, n):
    if n < 0:
        return AuxiliaryMemoryRecursionExponential(y, 1/x, -n)
    if n == 0:
        return y
    if n % 2 == 1:
        return AuxiliaryMemoryRecursionExponential(x*y, x*x, (n-1)/2)
    return AuxiliaryMemoryRecursionExponential(y, x*x, n/2)

def ConstantAuxiliaryMemoryRecursionExponential(x, n):
    return AuxiliaryMemoryRecursionExponential(1, x, n)

def IterativeConstantAuxiliaryMemoryRecursionExponential(x, n):
    if n < 0:
        x = 1/x
        n = -n
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n /= 2
        else:
            y *= x
            x *= x
            n = (n-1)/2
    return x * y


if __name__ == '__main__':
    print(VeryBasicExponental(36, -1)) # 1
    print(RecursionExponential(36, -1)) # 0.027777777777777776
    print(ConstantAuxiliaryMemoryRecursionExponential(36, -1)) # 0.027777777777777776
    print(IterativeConstantAuxiliaryMemoryRecursionExponential(36, -1)) # 0.027777777777777776

    print(VeryBasicExponental(36, 0)) # 1
    print(RecursionExponential(36, 0)) # 1
    print(ConstantAuxiliaryMemoryRecursionExponential(36, 0)) # 1
    print(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 0)) # 1

    print(VeryBasicExponental(36, 1)) # 36
    print(RecursionExponential(36, 1)) # 36
    print(ConstantAuxiliaryMemoryRecursionExponential(36, 1)) # 36
    print(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 1)) # 36

    print(VeryBasicExponental(36, 12)) # 4738381338321616896
    print(RecursionExponential(36, 12)) # 4738381338321616896
    print(ConstantAuxiliaryMemoryRecursionExponential(36, 12)) # 4738381338321616896
    print(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 12)) # 4738381338321616896

    print(VeryBasicExponental(36, 13)) # 170581728179578208256
    print(RecursionExponential(36, 13)) # 170581728179578208256
    print(ConstantAuxiliaryMemoryRecursionExponential(36, 13)) # 170581728179578208256
    print(IterativeConstantAuxiliaryMemoryRecursionExponential(36, 13)) # 170581728179578208256

    # print(VeryBasicExponental(100, 300)) # 10^600
    # print(RecursionExponential(100, 300)) # 10^600
    # print(ConstantAuxiliaryMemoryRecursionExponential(100, 300)) # 10^600
    # print(IterativeConstantAuxiliaryMemoryRecursionExponential(100, 300)) # 10^600
