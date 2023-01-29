package main

import (
	"fmt"
	"strconv"
	"testing"
)

type Number interface {
	int | int64 | uint | uint64 | float32 | float64
}

type Text interface {
	string
}

func ConvertStrToArr(s string) (chars []string) {
	char := []rune(s)
	for i := 0; i < len(char); i++ {
		chars = append(chars, string(char[i]))
	}
	return
}

func TestConvertToArr(t *testing.T) {
	str1 := "Hello World"
	fmt.Println(ConvertStrToArr(str1))
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

func TestCombinationText(t *testing.T) {
	str1 := "loremipsum"
	arrStr1 := ConvertStrToArr(str1)
	fmt.Println(Combinations(arrStr1, 3))
}

func TestCombinationNums(t *testing.T) {
	num1 := 12345
	str1 := strconv.Itoa(num1)
	arrStr1 := ConvertStrToArr(str1)
	fmt.Println(Combinations(arrStr1, 3))
}

func TestCombinationArrNums(t *testing.T) {
	num1 := []int{1, 2, 3, 4, 5, 6}
	fmt.Println(Combinations(num1, 3))
}

func TestCombinationArrText(t *testing.T) {
	num1 := []string{"a", "b", "c", "d", "e"}
	fmt.Println(Combinations(num1, 3))
}

func FindSubset(arr []int64) [][]int64 {
	combArr := make([][]int64, 0)
	var i int64
	for i = 0; i <= int64(len(arr)); i++ {
		combArr = append(combArr, Combinations(arr, i)...)
	}
	return combArr
}

func TestFindSubset(t *testing.T) {
	arr := []int64{4, 5, 6, 7}
	fmt.Println(FindSubset(arr))
}
