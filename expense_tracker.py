import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    description = input("Enter description: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    save_expenses(expenses)
    print("\n✅ Expense Added Successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.\n")
        return
    print("\n--- Expense List ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['amount']} - {e['category']} ({e['description']})")
    print()

def total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"\n💰 Total Expenses: {total}\n")

def main():
    expenses = load_expenses()
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")

if __name__ == "__main__":
    main()
