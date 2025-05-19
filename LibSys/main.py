from libsys import LibSys

def main():
    print("Welcome to LibSys (Library Management System)")
    print("-------------------------------------------")
    libsys = LibSys()

    while True:
        print("\nLibSys Menu")
        print("-----------")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Register Borrower")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Display Books")
        print("7. Check Account")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            libsys.add_book()
        elif choice == "2":
            libsys.search_book()
        elif choice == "3":
            libsys.register_borrower()
        elif choice == "4":
            libsys.borrow_book()
        elif choice == "5":
            libsys.return_book()
        elif choice == "6":
            libsys.display_books()
        elif choice == "7":
            libsys.check_account()
        elif choice == "8":
            print("Exiting LibSys. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
