package main

import (
	"fmt"
	"strconv"
	"strings"
)

func timeConversion(s string) string {
	s_split := strings.Split(s, ":")
	if strings.Contains(strings.ToLower(s_split[len(s_split)-1]), "am") {
		s_split[len(s_split)-1] = strings.Replace(strings.ToLower(s_split[len(s_split)-1]), "am", "", -1)
		if strings.Contains(s_split[0], "12") {
			s_split[0] = "00"
		}
	} else {
		s_split[len(s_split)-1] = strings.Replace(strings.ToLower(s_split[len(s_split)-1]), "pm", "", -1)
		if !strings.Contains(s_split[0], "12") {
			s_split_first_ele_int, err := strconv.Atoi(strings.TrimLeft(s_split[0], "0"))
			if err == nil {
				s_split[0] = strconv.Itoa(s_split_first_ele_int + 12)
			}
		}
	}
	s_final := strings.Join(s_split, ":")
	return s_final
}

func main() {
	fmt.Println(timeConversion("12:00:00am"))
	fmt.Println(timeConversion("07:05:45PM"))
}
