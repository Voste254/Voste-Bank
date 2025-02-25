import json
import random

class Bank:
    CUSTOMER_FILE = "customers.json"

    def __init__(self):
        self.customers = self.load_customers()
        self.welcome()

    def load_customers(self):
        try:
            with open(self.CUSTOMER_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_customers(self):
        with open(self.CUSTOMER_FILE, "w") as file:
            json.dump(self.customers, file, indent=4)

    def welcome(self):
        print("\n********************************")
        print("WELCOME TO VOSTE BANK")
        print("1. Log in\n2. Sign up")
        choice = input("Enter an option: ").strip()
        if choice == '1':
            self.login()
        elif choice == '2':
            self.signup()
        else:
            print("Invalid option!")
            self.welcome()

    def signup(self):
        print("\n*********** SIGN UP ***********")
        name = input("Enter your name: ").strip()
        password = input("Enter your password: ").strip()
        account_num = random.randint(100000, 999999)
        self.customers[str(account_num)] = {"name": name, "password": password, "balance": 10000}
        self.save_customers()
        print("\n********************************")
        print(f"Hi {name}, your account has been created successfully.")
        print(f"Your account number is {account_num}")
        self.next_step()

    def login(self):
        print("\n********** LOG IN **********")
        account_num = input("Enter your account number: ").strip()
        password = input("Enter your password: ").strip()
        
        if account_num in self.customers and self.customers[account_num]["password"] == password:
            print(f"\nLogin successful! Welcome back, {self.customers[account_num]['name']}.")
            self.next_step()
        else:
            print("\nInvalid credentials. Please try again or sign up.")
            self.welcome()

    def next_step(self):
        choice = input("\nEnter (N) to go to the next step or (H) to return to home page: ").strip().upper()
        if choice == "N":
            self.transactions()
        elif choice == "H":
            self.welcome()
        else:
            print("Invalid input!")
            self.next_step()

    def transactions(self):
        print("\n****** TRANSACTIONS ******")
        print("1. Deposit cash\n2. Withdraw cash\n3. Transfer cash")
        
if __name__ == "__main__":
    Bank()
