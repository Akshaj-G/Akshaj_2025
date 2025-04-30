# List that stores all the accounts. Each account is a dictionary with "name" and "balance", to store the information of all the users
accounts = []

# Creates a new bank account
def create_account():
   name = input("Enter your name to create an account: ").strip()
  
 # Makes sure accounts with the same name don't exist 
   for account in accounts:
       if account['name'].lower() == name.lower():
           print("❌ Account with this name already exists.")
           return
  
  # Asks the user for his intial deposit and handles errors with invalid inputs
   try:
       initial_deposit = float(input("Enter your initial deposit amount: "))
   except ValueError:
       print("❌ Invalid deposit amount. Please enter a number.")
       return

# Makes sure that the deposit is not negative
   if initial_deposit < 0:
       print("❌ Initial deposit cannot be negative.")
       return

# Creation of the dictionary which gets added to the list
   account = {
       'name': name,
       'balance': initial_deposit
   }
   accounts.append(account)
   print(f"✅ Account for {name} created successfully with an initial deposit of {initial_deposit}.")

# The function that is used to check balance of the user
def check_balance(name):
    # Searches for the account with the given name
   for account in accounts:
       if account['name'].lower() == name.lower():
           # Prints the user's balance
           print(f"✅ {name}, your current balance is: ${account['balance']:.2f}")
           return
   print("❌ Account not found.")

# Function for the user to deposit money
def deposit(name):
    # Searchs for the account with the given name
   for account in accounts:
       if account['name'].lower() == name.lower():
           try:
               # Asks for the amount of deposit and makes sure it isn't an error
               amount = float(input(f"Enter amount to deposit into {name}'s account: "))
           except ValueError:
               print("❌ Invalid amount. Please enter a valid number.")
               return
          # Makes sure that it isn't an negative deposit
           if amount < 0:
               print("❌ Deposit amount cannot be negative.")
               return

         # Changes the account balance based on the deposit 
           account['balance'] += amount
           print(f"✅ Successfully deposited ${amount:.2f} into {name}'s account.")
           return
   print("❌ Account not found.")

# Function for the user to withdraw money
def withdraw(name):
    # Searchs for the account with the given name
   for account in accounts:
       if account['name'].lower() == name.lower():
           try:
               # Asks for the amount of withdrawal and makes sure it isn't an error
               amount = float(input(f"Enter amount to withdraw from {name}'s account: "))
           except ValueError:
               print("❌ Invalid amount. Please enter a valid number.")
               return
          
          # Makes sure that it isn't an negative amount
           if amount < 0:
               print("❌ Withdrawal amount cannot be negative.")
               return
           # Prevents the withdrawal of unexisting funds
           if amount > account['balance']:
               print("❌ Insufficient balance.")
               return

         # Changes the account balance based on the withdrawal 
           account['balance'] -= amount
           print(f"✅ Successfully withdrew ${amount:.2f} from {name}'s account.")
           return
   print("❌ Account not found.")

# User interactions in the terminal
def main_menu():
   while True:
       # Displayed options
       print("\n=== Banking System ===")
       print("1. Create New Account")
       print("2. Check Balance")
       print("3. Deposit Money")
       print("4. Withdraw Money")
       print("5. Exit")

       # User Inputs
       choice = input("Choose an option (1-5): ").strip()

       # The process of corresponding function being called based upon the user input
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



# Starts the system
main_menu()