package main

import (
	"fmt"
)

// Given numRows, generate the first numRows of Pascal's triangle.
//
// For example, given numRows = 5,
// Return
//
// [
//      [1],
//     [1,1],
//    [1,2,1],
//   [1,3,3,1],
//  [1,4,6,4,1]
// ]

func generate(numRows int) [][]int {
	if numRows == 0 {
		return [][]int{}
	}

	if numRows == 1 {
		return [][]int{
			{1},
		}
	}

	if numRows == 2 {
		return [][]int{
			{1},
			{1, 1},
		}
	}
	row := []int{1}
	rows := generate(numRows - 1)
	lastRow := rows[len(rows)-1]
	i := 0
	for {
		value := lastRow[i] + lastRow[i+1]
		row = append(row, value)
		i += 1
		if i == len(lastRow)-1 {
			break
		}
	}
	row = append(row, 1)
	rows = append(rows, row)
	return rows
}

func main() {
	fmt.Println(generate(3))
	fmt.Println(generate(4))
	fmt.Println(generate(5))
}
