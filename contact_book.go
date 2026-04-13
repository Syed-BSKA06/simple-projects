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

func addContact(contacts []Contact, name, phone, email string) []Contact {
	contacts = append(contacts, Contact{name, phone, email})
	fmt.Printf("Contact '%s' added.\n", name)
	return contacts
}

func removeContact(contacts []Contact, name string) []Contact {
	for i, c := range contacts {
		if c.Name == name {
			contacts = append(contacts[:i], contacts[i+1:]...)
			fmt.Printf("Contact '%s' removed.\n", name)
			return contacts
		}
	}
	fmt.Printf("Contact '%s' not found.\n", name)
	return contacts
}

func main() {
	contacts := []Contact{
		{"Alice Johnson", "555-1234", "alice@example.com"},
		{"Bob Smith", "555-5678", "bob@example.com"},
	}
	displayContacts(contacts)
	contacts = addContact(contacts, "Charlie Brown", "555-9999", "charlie@example.com")
	contacts = removeContact(contacts, "Bob Smith")
	displayContacts(contacts)
}
