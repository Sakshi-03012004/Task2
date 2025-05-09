# main.py

import anagram
import CRUD
import email_validation
import login_credentials
import max_frequency
import prime

def main():
    while True:
        print("\n==== Task2 Menu ====")
        print("1. Anagram Checker")
        print("2. CRUD Operations")
        print("3. Email Validation")
        print("4. Login Credential Checker")
        print("5. Max Frequency Finder")
        print("6. Prime Number Checker")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            anagram.run()
        elif choice == '2':
            CRUD.run()
        elif choice == '3':
            email_validation.run()
        elif choice == '4':
            login_credentials.run()
        elif choice == '5':
            max_frequency.run()
        elif choice == '6':
            prime.run()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
