package main

import (
	"fmt"
	"math"
)

func FlippingBits64(n int64) int64 {
	return ((int64(math.Pow(2, 64)) - 1) - n)
}

func FlippingBits(n int64) int64 {
	return (int64(math.Pow(2, 32)) - 1) - n
}

func main() {
	fmt.Println(FlippingBits(10))
	fmt.Println(FlippingBits(100))
}
