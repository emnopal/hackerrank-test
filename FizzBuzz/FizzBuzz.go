package main

import (
	"fmt"
	"strings"
)

func FizzBuzz(maxLoop int) string {
	var fizzBuzz string
	for i := 1; i <= maxLoop; i++ {
		if i%3 == 0 && i%5 == 0 {
			fizzBuzz += " FizzBuzz "
		} else if i%3 == 0 {
			fizzBuzz += " Fizz "
		} else if i%5 == 0 {
			fizzBuzz += " Buzz "
		} else {
			fizzBuzz += fmt.Sprintf(" %d ", i)
		}
	}
	return strings.Trim(fizzBuzz, " ")
}

func main() {
	fmt.Println(FizzBuzz(100))
}
