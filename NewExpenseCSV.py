import os
import csv
from datetime import datetime
from collections import defaultdict

class NewExpenseCSV:
    def __init__(self):
        self.file_name = 'expenses.csv'
        
    def add_expenses(self):
        
        #Input on date
        date_input = input("Enter the date of the expense in (MM/DD/YYYY) format: ")
        try:
            datetime.strptime(date_input, '%m/%d/%Y')
        except ValueError:
            print("Invalid date format. Please try again!")
            return
        
        #Input on the price amount
        price_amount = float(input("Enter the amount of the expense: $"))
        try:
            price_amount = float(price_amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return
        
        # Working input description
        description = input("Enter a description of the expense: ")
        if description == '':
            description = 'No description'
        
        #assigning categories of each prices
        category = input("Enter the category of the expense: ")
        if category == '':
            category = 'No category name is given'
        
        #writing in the file in each row
        with open(self.file_name, 'a', newline='') as file:
            expense = csv.writer(file)
            expense.writerow([date_input, price_amount, description, category])
        print("Expense added successfully!")
        

    def view_expenses(self):
        #Checking if the CSV file does exists
        if not os.path.exists(self.file_name):
            print("No expenses to show")
            return
        #reads and displayes all the expenses
        # This has a list that shows each time the row is added
        with open(self.file_name, 'r') as file:
            
            reader = csv.reader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses to show")
            else:
                #Iterate through row from expenses list
                #using i as index and each title that are assoiceated with value
                for i, row in enumerate(expenses, start=1):
                    # assign each key to a row for loop
                    date_input, price_amount, description, category = row
                    print(f"{i}. Date: {date_input}, Amount: {price_amount}, Description: {description}, Category: {category}")

    def delete_expense(self):
        try:
            expense_number = int(input("Enter the expense number you want to delete: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        with open(self.file_name, 'r') as file:
            expenses = list(csv.reader(file))
            #if user select 1 and that exists in the file
            if 0 < expense_number <= len(expenses):
                del expenses[expense_number - 1]
                #then delete that file with minus 1, because list indices are zero-based
                with open(self.file_name, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(expenses)
                print("Expense deleted successfully!")
            else:
                print("Invalid expense number")
    def search_expense(self):
        if not os.path.exists(self.file_name):
            print("no expense Exists")
        
        #user input on date or catergory or description to find the record
        expense_search = input("Enter either Date ( mm/dd/yyyy) or category or description in the search ").lower()
        
        with open(self.file_name, 'r') as file:
            search_file = list(csv.reader(file))
            
            result = [row for row in search_file if expense_search in row[0].lower() or expense_search in row[2].lower() or expense_search in row[3].lower()]
            if not result:
                print("No match expenses found")
            else:
                for i, row in enumerate(result, start=1):
                    date_input, price_amount, description, category = row
                    print(f"{i}, Date:{date_input}, Amount: {price_amount}, Description:{description}, Catagory: {category}")
        
    def show_summary(self):
        if not os.path.exists(self.file_name):
            print("No expenses to show")
            return
        #opens a file from path and checks if there is any file
        with open(self.file_name, 'r') as file:
            file_reader = list(csv.reader(file))
            if not file_reader:
                print("No expenses to show")
                return
            #sets a dictrary of category_totals as empty
            #so each catergory can fill wtih the total amount
            category_totals = {}
            total_expense = 0.0
            #sets Expense time in empty list.
            #as user input datetime, It starts to add it in the expense time list
            expense_time = []
            
            for row in file_reader:
                date, amount, description, category = row
                try:
                    amount = float(amount)
                except ValueError:
                    print(f"Invalid amount '{amount}' in the file. Skipping this entry.")
                    continue
                #this is for all total expenses rom all the categories
                total_expense += amount
                expense_time.append(datetime.strptime(date, '%m/%d/%Y'))
                
                #Checking category in category_totals exsits in dictionary
                    #if category exsits update the amount within the category
                    #if not just add the new catergory in the dictionary
                
                if category in category_totals:
                
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
                
                
            
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
                
            print(f"Total expenses: ${total_expense:.2f}")
            print(f"Description : {description}")

def main():
    expense_tracker = NewExpenseCSV()
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Delete an expense")
        print("4. Show summary")
        print("5. Search")
        print("6. Exit")
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
            expense_tracker.search_expense()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()