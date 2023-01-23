// TODO: https://www.google.com/search?q=handling+big+number+in+golang&oq=handling+big+number+in+golang

package main

import (
	"fmt"
	"math/big"
	// "math"
)

// handling small factorial
// func factorialGenerator(n uint64) (factorial uint64) {
// 	factorial = 1
// 	var i uint64
// 	for i = 1; i <= n; i++ {
// 		factorial *= i
// 	}
// 	return
// }

// handling big factorial
func bigFactorialGenerator(n int64) (factorial *big.Int) {
	factorial = new(big.Int)
	factorial.MulRange(1, n)
	return
}

func trailingZeros(n int64) (result *big.Int) {
	factorial := bigFactorialGenerator(n)
	result = big.NewInt(0)

	for {
		if !(factorial.Mod(factorial, big.NewInt(10)) == big.NewInt(0)) {
			break
		} 
		result = result.Add(result, big.NewInt(1))
		fmt.Println(result)
		factorial = factorial.Div(factorial, big.NewInt(10))
		fmt.Println(factorial)
	}

	return
}

func main() {
	fmt.Println(bigFactorialGenerator(40))
	fmt.Println(trailingZeros(40))
	// fmt.Println(bigFactorialGenerator(40))
}