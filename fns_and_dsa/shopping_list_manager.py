import os
import json

FILENAME = "shopping_list.txt"

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def load_shopping_list():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_shopping_list(shopping_list):
    with open(FILENAME, "w") as file:
        json.dump(shopping_list, file, indent=2)

def add_item(shopping_list):
    name = input("Enter item name: ").strip().lower()
    if not name:
        print("Item name cannot be empty.")
        return
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    for item in shopping_list:
        if item['name'] == name:
            item['quantity'] += quantity
            print(f"Updated '{name}' quantity to {item['quantity']}.")
            return

    shopping_list.append({"name": name, "quantity": quantity})
    print(f"Added '{name}' x{quantity} to the shopping list.")

def remove_item(shopping_list):
    name = input("Enter item name to remove: ").strip().lower()
    for item in shopping_list:
        if item['name'] == name:
            shopping_list.remove(item)
            print(f"Removed '{name}' from the shopping list.")
            return
    print(f"Item '{name}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is currently empty.")
        return
    print("\nCurrent Shopping List:")
    for idx, item in enumerate(shopping_list, start=1):
        print(f"{idx}. {item['name'].capitalize()} x{item['quantity']}")

def main():
    shopping_list = load_shopping_list()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            save_shopping_list(shopping_list)
            print("Shopping list saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
