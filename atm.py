# ATM Machine Simulation

class ATMMachine:
    def __init__(self, balance=100000):  
        self.balance = balance

    def check_balance(self):
        print(f"\nYour current balance is: Rs{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nYou've successfully deposited Rs{amount:.2f}.")
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"\nYou've successfully withdrawn Rs{amount:.2f}.")
        elif amount > self.balance:
            print("\nInsufficient balance!")
        else:
            print("\nWithdrawal amount must be positive.")

    def atm_menu(self):
        while True:
            print("\n--- ATM Machine ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            try:
                choice = int(input("\nSelect an option: "))

                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    amount = float(input("Enter deposit amount: Rs"))
                    self.deposit(amount)
                elif choice == 3:
                    amount = float(input("Enter withdrawal amount: Rs"))
                    self.withdraw(amount)
                elif choice == 4:
                    print("\nThank you for using the ATM. Goodbye!")
                    break
                else:
                    print("\nInvalid option. Please select a valid option.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")


atm = ATMMachine()
atm.atm_menu()
