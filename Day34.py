balance = 10000
pin = 1234
def menu():
    global balance
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("available balance is:", balance)
        elif choice == 2:
            d = int(input("enter the amount to withdraw:"))
            if d > balance:
                print("insufficient balance")
            else:
                balance -= d
                print("you have withdrawn:", d)
                print("updated balance is:", balance)
        elif choice == 3:
             a = int(input("enter the amount to deposit:"))
             balance += a
             print("you have deposited:", a)
             print("updated balance is:", balance)

        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
def check_pin():
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        print("Login Successful")
        menu()
    else:
        print("Incorrect PIN. Access denied.")
check_pin()
