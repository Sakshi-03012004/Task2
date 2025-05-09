import anagram
import crud
import email_validation
import login_credentials
import max_frequency
import prime

def display_menu():
    print("\n=== Task 2 Program Launcher ===")
    print("1. Anagram Checker")
    print("2. CRUD Operations")
    print("3. Email Validation")
    print("4. Login Credentials Validator")
    print("5. Maximum Frequency Finder")
    print("6. Prime Number Checker")
    print("7. Exit")
    return input("Select an option (1-7): ")

def main():
    while True:
        choice = display_menu()
        
        if choice == "1":
            print("\nRunning Anagram Checker...")
            anagram.anagram()  # Adjust function name if different
        elif choice == "2":
            print("\nRunning CRUD Operations...")
            crud.crud()  # Adjust function name if different
        elif choice == "3":
            print("\nRunning Email Validation...")
            email_validation.email_validation()  # Adjust function name if different
        elif choice == "4":
            print("\nRunning Login Credentials Validator...")
            login_credentials.login_credentials()  # Adjust function name if different
        elif choice == "5":
            print("\nRunning Maximum Frequency Finder...")
            max_frequency.max_frequency()  # Adjust function name if different
        elif choice == "6":
            print("\nRunning Prime Number Checker...")
            prime.prime()  # Adjust function name if different
        elif choice == "7":
            print("\nExiting Program. Goodbye!")
            break
        else:
            print("\nInvalid option! Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()