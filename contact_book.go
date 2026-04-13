package main

import "fmt"

type Contact struct {
	Name  string
	Phone string
	Email string
}

func displayContacts(contacts []Contact) {
	if len(contacts) == 0 {
		fmt.Println("No contacts found.")
		return
	}
	fmt.Printf("\n%-20s %-15s %-25s\n", "Name", "Phone", "Email")
	fmt.Println("-----------------------------------------------------------")
	for _, c := range contacts {
		fmt.Printf("%-20s %-15s %-25s\n", c.Name, c.Phone, c.Email)
	}
}

func main() {
	contacts := []Contact{
		{"Alice Johnson", "555-1234", "alice@example.com"},
		{"Bob Smith", "555-5678", "bob@example.com"},
	}
	displayContacts(contacts)
}
