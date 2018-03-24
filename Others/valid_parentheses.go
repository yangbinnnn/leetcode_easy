package main

import (
	"fmt"
)

type Stack struct {
	top  *Element
	size int
}

type Element struct {
	value interface{}
	next  *Element
}

func (s *Stack) Len() int {
	return s.size
}

func (s *Stack) Push(value interface{}) {
	s.top = &Element{value, s.top}
	s.size++
}

func (s *Stack) Pop() (value interface{}) {
	if s.size > 0 {
		value, s.top = s.top.value, s.top.next
		s.size--
		return
	}
	return nil
}

func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}
	stack := new(Stack)
	for _, c := range s {
		if c == '(' {
			stack.Push(')')
		} else if c == '[' {
			stack.Push(']')
		} else if c == '{' {
			stack.Push('}')
		} else {
			if stack.Len() == 0 || stack.Pop() != c {
				return false
			}
		}
	}
	return stack.Len() == 0
}

func main() {
	fmt.Println(isValid("[[]]"))
}
