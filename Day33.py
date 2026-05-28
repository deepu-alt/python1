balance = 10000
pin = 11423

def check_balance():
    print("Your balance is:", balance)

def withdraw():
    global balance

    amount = int(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print("You have withdrawn:", amount)

def deposit():
    global balance

    amount = int(input("Enter amount to deposit: "))

    balance += amount
    print("You have deposited:", amount)

def menu():

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            withdraw()

        elif choice == 3:
            deposit()

        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("Login Successful")
        menu()
    else:
        print("Incorrect PIN. Access denied.")

if __name__ == "__main__":
    main()