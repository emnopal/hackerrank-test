package main

import (
	"fmt"
	"strconv"
	"testing"
)

type Numeric interface {
	int | int64 | uint | uint64 | float32 | float64
}

func ConvertStringToArr(s string) []string {
	char := []rune(s)
	chars := make([]string, 0)
	for i := 0; i < len(char); i++ {
		chars = append(chars, string(char[i]))
	}
	return chars
}

func TestConvertStringToArr(t *testing.T) {
	str := "Hello World"
	arr := ConvertStringToArr(str)
	fmt.Println(arr)
	fmt.Println(arr[0])
	fmt.Println(arr[len(arr)-1])
}

func ConvertStrArrToInt(arrStr []string) (result []int64) {
	arrNumStr := make([]int64, 0)
	for i := 0; i < len(arrStr); i++ {
		numStr, err := strconv.Atoi(arrStr[i])
		if err == nil {
			arrNumStr = append(arrNumStr, int64(numStr))
		}
	}
	result = arrNumStr
	return
}

func SumNumericArr[T Numeric](arr []T) (result T) {
	result = 0
	for i := 0; i < len(arr); i++ {
		result += arr[i]
	}
	return
}

func TestConvertStrArrToIntAndSumNumericArr(t *testing.T) {
	num := 123456
	strNum := strconv.Itoa(num)
	strNumArr := ConvertStringToArr(strNum)
	fmt.Println(strNumArr)
	intNumArr := ConvertStrArrToInt(strNumArr)
	fmt.Println(intNumArr)
	sumStrNumArrInt := SumNumericArr(intNumArr)
	fmt.Println(sumStrNumArrInt) // 21
}

func DigitalRoots(num int64) int64 {
	strNum := strconv.Itoa(int(num))
	strNumArr := ConvertStringToArr(strNum)
	lengthStrNumArr := len(strNumArr)
	for lengthStrNumArr > 1 {
		intNumArr := ConvertStrArrToInt(strNumArr)
		num = SumNumericArr(intNumArr)
		strNum = strconv.Itoa(int(num))
		strNumArr = ConvertStringToArr(strNum)
		lengthStrNumArr = len(strNumArr)
	}
	return num
}

func TestDigitalRoots(t *testing.T) {
	fmt.Println(DigitalRoots(12345))  // 6
	fmt.Println(DigitalRoots(16))     // 7
	fmt.Println(DigitalRoots(942))    // 6
	fmt.Println(DigitalRoots(132189)) // 6
	fmt.Println(DigitalRoots(493193)) // 2
}
