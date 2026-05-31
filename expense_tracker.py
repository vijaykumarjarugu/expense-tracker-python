expenses = []
def add_expense():
    amount = float(input("Enter expense amount: ₹"))
    category = input("Enter category (Food/Travel/Bills/Shopping): ")
    expenses.append({
        "amount": amount,
        "category": category
    })
    print("Expense added successfully!\n")
def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\n----- All Expenses -----")
    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']} - {expense['category']}"
        )
    print()
def view_summary():
    if not expenses:
        print("No expenses to summarize.\n")
        return
    total = sum(expense["amount"] for expense in expenses)
    print("\n----- Expense Summary -----")
    print(f"Total Expenses: ₹{total}")
    categories = {}
    for expense in expenses:
        category = expense["category"]
        if category in categories:
            categories[category] += expense["amount"]
        else:
            categories[category] = expense["amount"]
    print("\nCategory-wise Spending:")
    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")
    print()
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice!\n")