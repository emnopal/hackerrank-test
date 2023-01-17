def FizzBuzzFirst(max_loop: int) -> str:
    fizz_buzz = ""
    for i in range(1, max_loop+1):
        if i%3 == 0 and i%5 == 0:
            fizz_buzz += " FizzBuzz "
        elif i%3 == 0:
            fizz_buzz += " Fizz "
        elif i%5 == 0:
            fizz_buzz += " Buzz "
        else:
            fizz_buzz += f" {str(i)} "
    return fizz_buzz.strip()

def FizzBuzzOneLine(max_loop: int) -> str:
    return "".join([" FizzBuzz " if i%3 == 0 and i%5 == 0 else (" Fizz " if i%3 == 0 else (" Buzz " if i%5 == 0 else (f" {str(i)} "))) for i in range(1, max_loop+1)]).strip()

if __name__ == '__main__':
    print(FizzBuzzFirst(100))
    print(FizzBuzzOneLine(100))
