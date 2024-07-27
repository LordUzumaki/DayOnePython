import os

class Expense:
    def __init__(self):
        self.date = ""
        self.amount = ""
        self.description = ""

    def add_expenses(self):
        self.date = input("Enter the date of the expense in (MM/DD/YYYY) format: ")
        self.amount = input("Enter the amount of the expense: ")
        self.description = input("Enter a description of the expense: ")
        if self.description == '':
            self.description = 'No description'

        with open('expenses.txt', 'a') as file:
            file.write(f"{self.date}, {self.amount}, {self.description}\n")
        print("Expense added successfully!")

    def view_expenses(self):
        if not os.path.exists('expenses.txt'):
            print("No expenses to show")
            return
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses to show")
            else:
                for i, line in enumerate(expenses, start=1):
                    date, amount, description = line.strip().split(',')
                    print(f"{i}. Date: {date}, Amount: {amount}, Description: {description}")

    def delete_expense(self):
        self.view_expenses()
        expense_number = int(input("Enter the expense number you want to delete:"))
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()
        if 0 < expense_number <= len(expenses):
            del expenses[expense_number - 1]
            with open('expenses.txt', 'w') as file:
                file.writelines(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number")

    def show_summary(self):
        if not os.path.exists('expenses.txt'):
            print("No expenses to show")
            return
        with open('expenses.txt', 'r') as file:
            expenses = file.readlines()
            if not expenses:
                print("No expenses to show")
            else:
                total_expense = sum(float(expense.strip().split(',')[1]) for expense in expenses)
                print(f"Total expenses: ${total_expense:.2f}")
                print(f"Average expense: ${total_expense/len(expenses):.2f}")

def main():
    expense_tracker = Expense()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            expense_tracker.add_expenses()
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            expense_tracker.delete_expense()
        elif choice == '4':
            expense_tracker.show_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
