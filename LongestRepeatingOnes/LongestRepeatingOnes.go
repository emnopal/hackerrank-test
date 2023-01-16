package main

import (
	"fmt"
	"strconv"
)

func LongestRepeatingOnes(str string) uint {
	var num_final uint = 0
	var num_final_temp uint = 0

	for _, char := range str {
		if num, err := strconv.Atoi(string(char)); err == nil {
			if num == 1 {
				num_final_temp += 1
				if num_final_temp > num_final {
					num_final = num_final_temp
				}
			} else {
				num_final_temp = 0
			}
		}
	}

	return num_final
}

func main() {
	result := LongestRepeatingOnes("11100101010000001111111010101010")
	fmt.Println(result) // 7
}
