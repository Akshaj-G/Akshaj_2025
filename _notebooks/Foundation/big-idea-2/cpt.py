accounts = []

def create_account():
    """Prompts user to create a new account with a name and initial deposit"""
    name = input("Enter your name to create an account: ").strip()
    
    for account in accounts:
        if account['name'].lower() == name.lower():
            print("❌ Account with this name already exists.")
            return
    
    try:
        initial_deposit = float(input("Enter your initial deposit amount: "))
    except ValueError:
        print("❌ Invalid deposit amount. Please enter a number.")
        return

    if initial_deposit < 0:
        print("❌ Initial deposit cannot be negative.")
        return

    account = {
        'name': name,
        'balance': initial_deposit
    }
    accounts.append(account)
    print(f"✅ Account for {name} created successfully with an initial deposit of {initial_deposit}.")

def check_balance(name):
    """Prints the current balance of the given account"""
    for account in accounts:
        if account['name'].lower() == name.lower():
            print(f"✅ {name}, your current balance is: ${account['balance']:.2f}")
            return
    print("❌ Account not found.")

def deposit(name):
    """Deposits money into the specified account"""
    for account in accounts:
        if account['name'].lower() == name.lower():
            try:
                amount = float(input(f"Enter amount to deposit into {name}'s account: "))
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
                return
            
            if amount < 0:
                print("❌ Deposit amount cannot be negative.")
                return

            account['balance'] += amount
            print(f"✅ Successfully deposited ${amount:.2f} into {name}'s account.")
            return
    print("❌ Account not found.")

def withdraw(name):
    """Withdraws money from the specified account"""
    for account in accounts:
        if account['name'].lower() == name.lower():
            try:
                amount = float(input(f"Enter amount to withdraw from {name}'s account: "))
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
                return
            
            if amount < 0:
                print("❌ Withdrawal amount cannot be negative.")
                return
            if amount > account['balance']:
                print("❌ Insufficient balance.")
                return

            account['balance'] -= amount
            print(f"✅ Successfully withdrew ${amount:.2f} from {name}'s account.")
            return
    print("❌ Account not found.")

def main_menu():
    """Displays the main menu and lets the user choose actions"""
    while True:
        print("\n=== Banking System ===")
        print("1. Create New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            create_account()
        elif choice == '2':
            name = input("Enter your account name: ").strip()
            check_balance(name)
        elif choice == '3':
            name = input("Enter your account name: ").strip()
            deposit(name)
        elif choice == '4':
            name = input("Enter your account name: ").strip()
            withdraw(name)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


main_menu()
