package main

import (
	"fmt"
)

type Number interface {
	int | int64 | uint | uint64 | float32 | float64
}

type Text interface {
	string
}

func Combinations[T Number | Text](arr []T, n int64) [][]T {
	combination := make([][]T, 0)
	if n == 0 {
		tempArr := make([]T, 0)
		combination = append(combination, tempArr)
		return combination
	}
	for i := 0; i < len(arr); i++ {
		m := arr[i]
		remLst := arr[i+1:]
		for _, s := range Combinations(remLst, n-1) {
			tempArr := make([]T, 0)
			tempArr = append(tempArr, m)
			combination = append(combination, append(tempArr, s...))
		}
	}
	return combination
}

func FindSubset(arr []int64) [][]int64 {
	combArr := make([][]int64, 0)
	var i int64
	for i = 0; i <= int64(len(arr)); i++ {
		combArr = append(combArr, Combinations(arr, i)...)
	}
	return combArr
}

func main() {
	arr := []int64{4, 5, 6, 7}
	fmt.Println(FindSubset(arr))
}
