# Contact Book

contacts = {}

while True:
    print("==== Contact Book ====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View contact")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your Name: ")
        number = input("Enter contact number: ")
        contacts[name] = number
        print("Contact added successfully")

    elif choice == "2":
        search_name = input("Enter name to search: ")

        if search_name in contacts:
            print("number :", contacts[search_name])
    
        else:
            print("Contact Not Found")
            print("Thank you for using contact book")
            break

    elif choice == "3":
        if len(contacts) == 0:
            print("No contact available")
    
        else:
            print("Saved contact")
            for name, number in contacts.items():
                print(name, ":", number)
        
                print("Thank you for using contact book")
                break

else:
    print("Invalid choice! Please try Again")
        