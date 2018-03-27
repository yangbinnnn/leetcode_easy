package main

// Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
//
// Example 1
//
// Input: [3,0,1]
// Output: 2
// Example 2
//
// Input: [9,6,4,2,3,5,7,0,1]
// Output: 8
//
// Note:
// Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

func missingNumber(nums []int) int {
	// [x]
	if len(nums) == 0 {
		return 0
	}
	min := nums[0]
	max := nums[0]
	sum := nums[0]
	for _, v := range nums[1:] {
		if v < min {
			min = v
		}
		if v > max {
			max = v
		}
		sum += v
	}
	// [x, 1, 2, 3, ...]
	if min != 0 {
		return 0
	}
	diff := (1+max)*max/2 - sum
	// [0, 1, 2, x]
	if diff == 0 {
		return max + 1
	}
	// [0, 1, x, 3]
	return diff
}
