package main

import "fmt"

func Factorial(num uint) uint64 {
	var factorial uint64 = 1
	var i uint
	for i = 1; i <= num; i++ {
		factorial *= uint64(i)
	}
	return factorial
}

func FactorialRecursion(num uint) uint64 {
	if num < 1 {
		return 1
	}
	return uint64(num) * FactorialRecursion(num-1)
}

func main() {
	fmt.Println(Factorial(5))
	fmt.Println(Factorial(1))
	fmt.Println(Factorial(0))

	fmt.Println(FactorialRecursion(5))
	fmt.Println(FactorialRecursion(1))
	fmt.Println(FactorialRecursion(0))
}
