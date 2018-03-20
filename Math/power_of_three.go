package main

// Given an integer, write a function to determine if it is a power of three.
//
// Follow up:
// Could you do it without using any loop / recursion?
// 判断一个数是不是3的x次方

func isPowerOfThree(n int) bool {
	if n < 1 {
		return false
	}
	for n%3 == 0 {
		n = n / 3
	}
	return n == 1
}
