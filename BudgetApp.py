class BudgetApp:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, description="Income"):
        if amount > 0:
            self.balance += amount
            self.transactions.append({"type": "Income", "amount": amount, "description": description})
            print(f"Added income: ${amount:.2f}")
        else:
            print("Income must be a positive value!")

    def add_expense(self, amount, category="General", description="Expense"):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append({"type": "Expense", "amount": amount, "category": category, "description": description})
                print(f"Added expense: ${amount:.2f} for {category}")
            else:
                print("Insufficient balance to record this expense!")
        else:
            print("Expense amount must be a positive value!")

    def view_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}\n")

    def view_transactions(self):
        if self.transactions:
            print("\nTransaction History:")
            for i, t in enumerate(self.transactions, start=1):
                if t["type"] == "Income":
                    print(f"{i}. {t['type']}: ${t['amount']:.2f} - {t['description']}")
                else:
                    print(f"{i}. {t['type']}: ${t['amount']:.2f} - {t['category']} ({t['description']})")
        else:
            print("\nNo transactions recorded yet!")

    def run(self):
        print("\nWelcome to the Budget App!")
        while True:
            print("\nChoose an option:")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. View Transactions")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                try:
                    amount = float(input("Enter the income amount: $"))
                    description = input("Enter a description for the income (optional): ") or "Income"
                    self.add_income(amount, description)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "2":
                try:
                    amount = float(input("Enter the expense amount: $"))
                    category = input("Enter the category of the expense (e.g., Food, Rent, Transport): ")
                    description = input("Enter a description for the expense (optional): ") or "Expense"
                    self.add_expense(amount, category, description)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                self.view_balance()
            elif choice == "4":
                self.view_transactions()
            elif choice == "5":
                print("\nThank you for using the Budget App! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    app = BudgetApp()
    app.run()
