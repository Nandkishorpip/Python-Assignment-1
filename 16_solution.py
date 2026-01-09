import json
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.load_expenses()

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)
        print(f"Added {amount} to {category}.")

    def view_total_for_category(self, category):
        if category in self.expenses:
            total = sum(self.expenses[category])
            print(f"Total for {category}: {total}")
        else:
            print(f"No expenses found for category: {category}")

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)
        print("Expenses saved successfully.")

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
            print("Expenses loaded successfully.")
        except FileNotFoundError:
            print("No saved expenses found. Starting fresh.")

    def view_all_expenses(self):
        if self.expenses:
            for category, amounts in self.expenses.items():
                total = sum(amounts)
                print(f"{category}: {total} (Details: {amounts})")
        else:
            print("No expenses recorded.")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Total for a Category")
        print("3. View All Expenses")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
        elif choice == "2":
            category = input("Enter category: ")
            tracker.view_total_for_category(category)
        elif choice == "3":
            tracker.view_all_expenses()
        elif choice == "4":
            tracker.save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
