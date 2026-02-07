account = {
    "owner": "User",
    "balance": 0.0,
    "transactions": []
}

def show_balance():
    balance = account["balance"]
    print(f"Current balance: ${balance:.2f} ")

def deposit():
    amount_str = input("Enter amount to deposit: ")
    if not amount_str.replace(".","", 1).isdigit():
        print("Invalid amount. Please enter a number.")
        return


def withdraw():
    pass

def show_transactions():
    pass

def menu():
    print("1. Show balance\n2. Deposit\n3. Withdraw\n4. Transactions\n5. Exit")

while True:
    menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        show_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        show_transactions()
    elif choice == 5:
        break
    else:
        print("Not a valid choice.")
