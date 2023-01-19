package main

import (
	"fmt"
	"regexp"
	"strings"
)

func IsPalindromeFirst(str string) bool {
	rePattern := regexp.MustCompile(`\W+`)
	cleanStr := strings.ToLower(rePattern.ReplaceAllString(str, ""))
	strRune := []rune(cleanStr)
	for i, j := 0, len(strRune)-1; i < j; i, j = i+1, j-1 {
		strRune[i], strRune[j] = strRune[j], strRune[i]
	}
	reverseStr := string(strRune)
	return cleanStr == reverseStr
}

func IsPalindromeSecond(str string) bool {
	rePattern := regexp.MustCompile(`\W+`)
	cleanStr := strings.ToLower(rePattern.ReplaceAllString(str, ""))
	reverseStr := ""
	for _, v := range cleanStr {
		reverseStr = string(v) + reverseStr
	}
	return cleanStr == reverseStr
}

func IsPalindromeThird(str string) bool {
	rePattern := regexp.MustCompile(`\W+`)
	cleanStr := strings.ToLower(rePattern.ReplaceAllString(str, ""))
	reverseStr := []byte{}
	for i := len(cleanStr) - 1; i >= 0; i-- {
		reverseStr = append(reverseStr, cleanStr[i])
	}
	return cleanStr == string(reverseStr)
}

func main() {
	fmt.Println(IsPalindromeFirst("Red roses run no risk, sir, on Nurse's order"))
	fmt.Println(IsPalindromeSecond("Red roses run no risk, sir, on Nurse's order"))
	fmt.Println(IsPalindromeThird("Red roses run no risk, sir, on Nurse's order"))
}
