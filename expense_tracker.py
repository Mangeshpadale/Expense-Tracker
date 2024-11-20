# Define the main menu interface
def display_menu():
    print("\n--- Welcome to the Personal Expense Tracker ---")
    print("1. Add a New Expense")
    print("2. View Summary by Date")
    print("3. View Summary by Category")
    print("4. Exit")

# Add a new expense
def add_expense():
    try:
        date = input("Enter Date (DD/MM/YY): ")
        category = input("Enter Category (food/transport/entertainment): ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))

        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{description},{amount}\n")

        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter numeric values for the amount.")

# View summary by date
def view_summary_by_date():
    date = input("Enter Date (DD/MM/YY): ")
    total = 0
    print(f"\nExpenses on {date}:")

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                expense_date, category, description, amount = line.strip().split(",")
                if expense_date == date:
                    print(f"- {category} - {description} - ${amount}")
                    total += float(amount)
        print(f"Total Expenses on {date}: $ {total:.2f}")
    except FileNotFoundError:
        print("No expense records found.")
    except ValueError:
        print("Error reading expense file.")

# View summary by category
def view_summary_by_category():
    category = input("Enter Category (food/transport/entertainment): ")
    total = 0.0

    print(f"Expenses for {category}:")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                expense_date, expense_category, description, amount = line.strip().split(",")
                if expense_category == category:
                    print(f"- {expense_date}: {description} - ${amount}")
                    total += float(amount)
        print(f"Total {category} Expenses: $ {total:.2f}")
    except FileNotFoundError:
        print("No expense records found.")
    except ValueError:
        print("Error reading expense file.")

# Exit option
def exit_program():
    print("Your expenses have been saved. Goodbye!")
    exit()

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary_by_date()
        elif choice == "3":
            view_summary_by_category()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice! Please select from 1-4.")

# Entry point
if __name__ == "__main__":
    main()
