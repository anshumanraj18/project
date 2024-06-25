import json
import sys
from tabulate import tabulate

DATA_FILE = 'customers.json'

def main():
    table = [["1", 'View All Customers info (List)'],
             ["2", 'Add Or Remove customer'],
             ["3", 'Update Customer Balance'],
             ["4", 'Search Customer by Name'],
             ["5", 'Exit']]
    headers = ["Option", "Task"]
    print("WELCOME !!")
    while True:
        print(tabulate(table, headers, tablefmt="outline"))
        user = input("CHOOSE AN OPTION: ").strip()

        if user == "1":
            view_customers()
        elif user == "2":
            add_or_remove_customer()
        elif user == "3":
            update_customer_balance()
        elif user == "4":
            search_customer()
        elif user == "5":
            sys.exit(0)
        else:
            print("Invalid option. Please try again.")

def save_customers(customers):
    """Save customer data to the file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(customers, file, indent=4)

def load_customers():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def view_customers():
    customers = load_customers()
    if not customers:
        print("Empty List !!!  please Add Customer to see Records ....")
    else:
        table = [[idx + 1, customer['name'], customer['balance'], customer['contact']] for idx, customer in enumerate(customers)]
        headers = ["Index", "Customers Name", "Customer Balance", "Customers contact"]
        print(tabulate(table, headers, tablefmt="pretty"))

def add_or_remove_customer():
    customers = load_customers()
    choice = input("Do you want to add or remove a customer? (add/remove): ").strip().lower()

    if choice == 'add':
        name = input("Enter customer's name: ").strip().capitalize()
        for customer in customers:
            if name.lower() == customer['name'].lower():
                print("Name Already in Use! Try another Name ..")
                return
        balance = float(input("Enter initial balance: ").strip())
        contact = input("Enter customer Contact Number: ")
        customers.append({'name': name, 'balance': balance, 'contact': contact})
        save_customers(customers)
        print(f"Customer {name} added with initial Debt balance of {balance}.")

    elif choice == 'remove':
        name = input("Enter the name of the customer to remove: ").strip()
        customers = [customer for customer in customers if customer['name'].lower() != name.lower()]
        save_customers(customers)
        print(f"Customer {name} removed.")

    else:
        print("Invalid choice. Please choose 'add' or 'remove'.")

def update_customer_balance():
    customers = load_customers()
    name = input("Enter the name of the customer to update: ").strip()
    for customer in customers:
        if customer['name'].lower() == name.lower():
            ask = input("Do you Want to (ADD / REDUCE) ? : ").strip().lower()
            if ask == "add":
                amount = float(input("Enter the amount to Add Debt: ").strip())
                customer['balance'] += amount
                save_customers(customers)
                print(f"Customer {name}'s balance updated to {customer['balance']}.")
                return
            elif ask == "reduce":
                amount = float(input("Enter the amount to Reduce Debt: ").strip())
                customer['balance'] -= amount
                save_customers(customers)
                print(f"Customer {name}'s balance updated to {customer['balance']}.")
                return
            else:
                print("Invalid Input!!")
                return
    print("Customer not found.")

def search_customer():
    customers = load_customers()
    name = input("Enter the name of the customer to search: ").strip()
    found_customers = [customer for customer in customers if name.lower() in customer['name'].lower()]

    if found_customers:
        table = [[idx + 1, customer['name'], customer['balance']] for idx, customer in enumerate(found_customers)]
        headers = ["Index", "Customer Name", "Debt Balance"]
        print(tabulate(table, headers, tablefmt="pretty"))
    else:
        print("No customers found with that name.")

if __name__ == "__main__":
    x = input("ENTER 4 DIGIT PASSWORD TO CONTINUE: ").strip()
    password = "0000"  # Default password
    if x == password:
        main()
    else:
        print("Wrong Password! Try again...")
