
import json

def add_expense(expenses, description, amount):
    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description}, Amount: {amount}")

def get_total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print("Expenses:")
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data['initial_budget'], data['expenses']
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return default values if the file doesn't exist or is empty/corrupted
#
def save_budget_data(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    print("Welcome to the Budget App")
    initial_budget = float(input("Please enter your initial budget: "))
    # filepath = 'budget_data.json'  # Define the path to your JSON file
    # initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget
    expenses = []

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting Budget App. Goodbye!")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()