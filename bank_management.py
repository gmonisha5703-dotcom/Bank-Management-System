accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account Already Exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }

    print("Account Created Successfully!")


def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Available Balance:", accounts[acc_no]["balance"])
    else:
        print("Account Not Found!")


def deposit_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:
            accounts[acc_no]["balance"] += amount
            print("Money Deposited Successfully!")
        else:
            print("Enter a Valid Amount!")
    else:
        print("Account Not Found!")


def withdraw_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            print("Enter a Valid Amount!")
        elif amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print("Money Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")


def view_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("\nAccount Details")
        print("Account Number:", acc_no)
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Account Not Found!")


def main():
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Account Details")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            check_balance()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            view_account()
        elif choice == "6":
            print("Thank You for Using Our Bank!")
            break
        else:
            print("Invalid Choice!")


main()
