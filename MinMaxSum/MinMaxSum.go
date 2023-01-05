package main

import (
	"fmt"
	"sort"
)

func sumArr(arr []int64) int64 {
	var res int64 = 0
	for i := 0; i < len(arr); i++ {
		res += arr[i]
	}
	return res
}

func sumFourArr(arr []int64) []int64 {
	firstArr, restArr := arr[0], arr[1:]
	var tempFirstArr int64
	var sumAllArr []int64

	for i := 0; i < len(arr); i++ {
		tempFirstArr = firstArr
		firstArr, restArr = restArr[0], append(restArr, tempFirstArr)
		restArr = restArr[1:]
		sumAllArr = append(sumAllArr, sumArr(restArr))
	}

	sort.Slice(sumAllArr, func(i, j int) bool { return sumAllArr[i] < sumAllArr[j] })

	fmt.Println(sumAllArr[0], sumAllArr[len(arr)-1])

	return sumAllArr
}

func main() {
	// a := []int64{1, 2, 3, 4, 5}
	a := []int64{256741038, 623958417, 467905213, 714532089, 938071625}
	sumResult := sumFourArr(a)
	fmt.Println(sumResult)
}
