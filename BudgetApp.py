budget = 1000

while True:
    print("1. View Balance")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance: $" + str(budget))
    elif choice == "2":
        income = float(input("Enter the income amount: $"))
        budget += income
        print("Income added successfully!")
    elif choice == "3":
        expense = float(input("Enter the expense amount: $"))
        if expense > budget:
            print("Insufficient funds!")
        else:
            budget -= expense
            print("Expense added successfully!")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting the budget application.")
