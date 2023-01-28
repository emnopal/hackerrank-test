package main

import (
	"fmt"
	"testing"
)

func Factorial(num uint) uint64 {
	var factorial uint64 = 1
	var i uint
	for i = 1; i <= num; i++ {
		factorial *= uint64(i)
	}
	return factorial
}

func TestFactorial(t *testing.T) {
	fmt.Println(Factorial(0))
	fmt.Println(Factorial(1))
	fmt.Println(Factorial(5))
	fmt.Println(Factorial(20))
}

func FactorialRecursion(num uint) uint64 {
	if num < 1 {
		return 1
	}
	return uint64(num) * FactorialRecursion(num-1)
}

func TestFactorialRecursion(t *testing.T) {
	fmt.Println(FactorialRecursion(0))
	fmt.Println(FactorialRecursion(1))
	fmt.Println(FactorialRecursion(5))
	fmt.Println(FactorialRecursion(20))
}
