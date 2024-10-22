def display_budget(expenses):
    total_expenses = sum(expenses.values())
    print("\nExpenses:")
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")

def main():
    expenses = {}
    
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Reset Budget")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: "))
                if category in expenses:
                    expenses[category] += amount
                else:
                    expenses[category] = amount
                print(f'Expense added: {category} - ${amount:.2f}')
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == '2':
            display_budget(expenses)
        elif choice == '3':
            expenses.clear()
            print("Budget reset.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()