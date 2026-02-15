package main

import "fmt"

func main() {
	var num1, num2 float64
	var operator string
	fmt.Print("Enter the first number: ")
	fmt.Scan(&num1)
	fmt.Print("Enter operator: ")
	fmt.Scan(&operator)
	fmt.Print("Enter the second number: ")
	fmt.Scan(&num2)

	if operator == "+" {
		fmt.Println("Result: ", num1+num2)
	} else if operator == "-" {
		fmt.Println("Result: ", num1-num2)
	} else if operator == "*" {
		fmt.Println("Result: ", num1*num2)
	} else if operator == "/" {
		if num2 != 0 {
			fmt.Println("Result: ", num1/num2)
		} else {
			fmt.Println("Cannot divide by zero")
		}
	} else {
		fmt.Println("Invalid operator")
	}
}
