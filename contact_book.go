package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

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

func addContact(contacts []Contact, name, phone, email string) []Contact {
	contacts = append(contacts, Contact{name, phone, email})
	fmt.Printf("Contact '%s' added.\n", name)
	return contacts
}

func removeContact(contacts []Contact, name string) []Contact {
	for i, c := range contacts {
		if strings.EqualFold(c.Name, name) {
			contacts = append(contacts[:i], contacts[i+1:]...)
			fmt.Printf("Contact '%s' removed.\n", c.Name)
			return contacts
		}
	}
	fmt.Printf("Contact '%s' not found.\n", name)
	return contacts
}

func searchContact(contacts []Contact, query string) {
	query = strings.ToLower(query)
	found := false
	fmt.Printf("\n%-20s %-15s %-25s\n", "Name", "Phone", "Email")
	fmt.Println("-----------------------------------------------------------")
	for _, c := range contacts {
		if strings.Contains(strings.ToLower(c.Name), query) ||
			strings.Contains(strings.ToLower(c.Email), query) ||
			strings.Contains(c.Phone, query) {
			fmt.Printf("%-20s %-15s %-25s\n", c.Name, c.Phone, c.Email)
			found = true
		}
	}
	if !found {
		fmt.Println("No matching contacts found.")
	}
}

func prompt(reader *bufio.Reader, label string) string {
	fmt.Print(label)
	text, _ := reader.ReadString('\n')
	return strings.TrimSpace(text)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	contacts := []Contact{
		{"Alice Johnson", "555-1234", "alice@example.com"},
		{"Bob Smith", "555-5678", "bob@example.com"},
	}

	menu := `
=== Contact Book ===
1. View All Contacts
2. Add Contact
3. Remove Contact
4. Search Contact
5. Exit
`
	for {
		fmt.Print(menu)
		choice := prompt(reader, "Choose an option: ")

		switch choice {
		case "1":
			displayContacts(contacts)
		case "2":
			name := prompt(reader, "Name  : ")
			phone := prompt(reader, "Phone : ")
			email := prompt(reader, "Email : ")
			contacts = addContact(contacts, name, phone, email)
		case "3":
			name := prompt(reader, "Enter name to remove: ")
			contacts = removeContact(contacts, name)
		case "4":
			query := prompt(reader, "Search (name/phone/email): ")
			searchContact(contacts, query)
		case "5":
			fmt.Println("Goodbye!")
			return
		default:
			fmt.Println("Invalid option. Choose 1-5.")
		}
	}
}
