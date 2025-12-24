# start building expense tracker version 1.0

import os
from datetime import date

# file to store the expenses
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.txt")

# defining lists to store details
expense_date = []
expense_category = []
expense_amount = []
expense_note = []

# defining categories of expenses
categories = ["Food", "Travel", "Rents", "Utilities", "Other"]

# greeting welcome messsage for users
print("\nWelcome to Expense Tracker v1.0")

# Load expenses from the text file into lists
def load_expenses():

    if os.path.exists(EXPENSES_FILE):

        with open(EXPENSES_FILE, 'r') as f:

            for line in f:
                line = line.strip()

                if line:  # Skip empty lines
                    # Split by comma [date,category,amount,description]
                    parts = line.split(',')

                    if len(parts) == 4:
                        # appends the list with values
                        expense_date.append(parts[0])
                        expense_category.append(parts[1])
                        expense_amount.append(parts[2])
                        expense_note.append(parts[3])

        print("Loaded all previous data from the file..\n")
    else:
        print("Unable to fetch previous data, starting a new file..\n")
                                                
# updating the expenses from list to text file
def update_expenses():

    with open(EXPENSES_FILE, 'w') as f:
        for ex_date, category, amount, note in zip(expense_date,expense_category,expense_amount,expense_note):
            f.write(f"{ex_date},{category},{amount},{note}\n")

# menu for adding expenses
def add_expenses_menu():

    while True:

        print("\n======= ADD MENU =======")
        print("\n1. Add an Expense.")
        print("2. Return to Main Menu.")

        while True:
            choice = input("\nEnter your choice(1-2): ")

            if choice == "1":
                add_expenses()
                break

            elif choice == "2":
                display_menu()
                return

            else:
                print("Please enter a valid choice!")

# adding expenses
def add_expenses():

    day = date.today()      # getting current date using datetime module
    day = day.strftime("%Y-%m-%d")
    print(f"\nDate: {day}\n")

    for i,option in enumerate(categories):    
        print(f"{i+1}. {option}")         # this will print the categories with index

    while True:

        choice = input("\nChoose an expense category (1-5): ")    # the user is prompted for decision

        if choice in ('1','2','3','4','5'):
            # if choice is valid, category is selected
            category = categories[int(choice)-1]
            print(f"{category} category selected.\n")
            break
        
        else:
            # when choice is invalid
            print("Please enter a valid category!")
    
    while True: 
        amount = input("Enter the amount: ")    # getting the amount expended

        try:        # validating the amount
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue 

            break

        except Exception:
            print("Please enter a valid amount!")
        
    note = input("Describe your expense in short: ")     # short description of expense for eg. Lunch, Tickets, etc.

    # updating the lists with new values
    expense_date.append(day)
    expense_category.append(category)
    expense_amount.append(amount)
    expense_note.append(note)

    # updating the file
    update_expenses()

    print(f"\n✓ Expense added successfully!\n")

    input("Press Enter to return")

# display all expenses stored
def view_expenses():

    if not expense_date:
        print("\nNo data of expenditure available.\n")
        return
    
    print("\n" + "="*65)
    print(f"{'#':<5} {'Date':<15} {'Category':<15} {'Amount':<15} {'Note':<15}")
    print("="*65)

    for i, (ex_date, category, amount, note) in enumerate(zip(expense_date, expense_category, expense_amount, expense_note), 1):
        print(f"{i:<5} {ex_date:<15} {category:<15} ₹ {amount:<13} {note:<15}")

    print("="*65 + "\n")
    
    input("Press Enter to return")
    display_menu()

# calculating total expenses
def calculate_total():
    
    number = len(expense_amount)
    total = 0
    
    for expense in expense_amount:
        total += float(expense)

    return number, total

# showing total expenses
def total_expenses():

    number, total = calculate_total()
    print("\n------ TOTAL EXPENSES ------")
    print(f"Number of expenses: {number}")
    print(f"Total amount spent: ₹{round(total, 2)}")
    print("----------------------------")

    input("\nPress Enter to return")
    display_menu()

# main menu of the application
def display_menu():
    
    print("\n======= MAIN MENU ========")
    print("\n1. Add an expense.")
    print("2. View all expenses.")
    print("3. Check your total expense.")
    print("4. Exit.")

# main loop of the application
def main():
    
    load_expenses()     # load the expenses from expenses.txt
    display_menu()      # display the main menu

    while True:

        choice = input("\nChoose an option(1-4): ")

        if choice == "1":
            add_expenses_menu()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Exiting the application..")
            break

        else:
            print("Sorry! Please choose a valid option.")

    print("\nThank you for using our application!\n")

main()