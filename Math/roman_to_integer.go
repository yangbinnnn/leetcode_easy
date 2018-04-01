package main

import "fmt"

//  Author: yangbin
//  Created: 04/01/2018

//  Given a roman numeral, convert it to an integer.
//  Input is guaranteed to be within the range from 1 to 3999.

func romanToInt(s string) int {
	res := 0
	for i := len(s) - 1; i >= 0; i-- {
		switch s[i] {
		case 'I':
			k := 1
			if res >= 5 {
				k = -1
			}
			res += k
		case 'V':
			res += 5
		case 'X':
			k := 1
			if res >= 50 {
				k = -1
			}
			res += 10 * k
		case 'L':
			res += 50
		case 'C':
			k := 1
			if res >= 500 {
				k = -1
			}
			res += 100 * k
		case 'D':
			res += 500
		case 'M':
			res += 1000
		}
	}
	return res
}

func main() {
	// 4
	fmt.Println(romanToInt("IV"))

	// 10
	fmt.Println(romanToInt("X"))

	// 17
	fmt.Println(romanToInt("XVII"))

	// 621
	fmt.Println(romanToInt("DCXXI"))

	fmt.Println(romanToInt("MDCCCLXXXIV"))
}
