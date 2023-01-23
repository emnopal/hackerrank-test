def factorialGenerator(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

def trailingZeros(n, f=None):
    if not f:
        trailingZeros = n
    else:
        trailingZeros = f(n)

    result = 0

    while True:
        if not trailingZeros % 10 == 0:
            break
        result += 1
        trailingZeros //= 10 # `//` can handle big number but `/` can't

    return result

def trailingZerosFactorial(n):
    factorial = 1
    result = 0

    for i in range(1, n+1):
        factorial *= i

    while True:
        if not factorial % 10 == 0:
            break
        result += 1
        factorial //= 10 # `//` can handle big number but `/` can't

    return result


if __name__ == '__main__':
    # print(trailingZeros(120, f=factorialGenerator))
    # print(trailingZerosFactorial(120))
    print(factorialGenerator(40))
    print(trailingZerosFactorial(40))
