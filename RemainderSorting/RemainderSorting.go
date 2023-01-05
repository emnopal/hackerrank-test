package main

import (
	"fmt"
	"sort"
)

func RemainderSorting(strArr []string) []string {

	// group strArr based on remainder then store it to the map
	arrRemainderInit := make(map[int][]string)
	for _, str := range strArr {
		arrRemainderInit[len(str)%3] = append(arrRemainderInit[len(str)%3], str)
	}

	// sort the map based on key
	// create an array to store the key as array then sort it
	remainderKeys := make([]int, 0, len(arrRemainderInit))
	for k := range arrRemainderInit {
		remainderKeys = append(remainderKeys, k) // fill remainderKeys
	}
	sort.Ints(remainderKeys) // sort the array

	// restore the map from sorted key (which is array)
	// then sort the value, which is array of string
	arrRemainder := make(map[int][]string)
	for _, k := range remainderKeys {
		sort.Strings(arrRemainderInit[k])
		arrRemainder[k] = append(arrRemainder[k], arrRemainderInit[k]...)
	}

	// get the sorted value only
	remainderValue := make([][]string, 0)
	for _, v := range arrRemainder {
		remainderValue = append(remainderValue, v)
	}

	// flatten the array to get a result
	finalValue := make([]string, 0)
	for _, val := range remainderValue {
		finalValue = append(finalValue, val...)
	}

	return finalValue

}

func main() {
	strArr := []string{"Colorado", "Utah", "Montana", "Wisconsin", "Oregon", "Maine"}
	strArrResult := RemainderSorting(strArr)
	fmt.Println(strArrResult)
}
