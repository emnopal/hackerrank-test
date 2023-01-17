def EasiestFactorial(num: int) -> int:
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
    return factorial

def FactorialRecursion(num: int) -> int:
    if num < 1:
        return 1
    return num * FactorialRecursion(num-1)

def FactorialRecursionOneLine(num: int) -> int:
    return 1 if num < 1 else num * FactorialRecursion(num-1)

if __name__ == '__main__':
    print(EasiestFactorial(5))
    print(FactorialRecursion(5))
    print(FactorialRecursionOneLine(5))

    print(EasiestFactorial(1))
    print(FactorialRecursion(1))
    print(FactorialRecursionOneLine(1))

    print(EasiestFactorial(0))
    print(FactorialRecursion(0))
    print(FactorialRecursionOneLine(0))
