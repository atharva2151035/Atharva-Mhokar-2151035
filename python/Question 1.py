class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            print("Item already exists. Updating quantity and price.")
            self.update_item(item_name, quantity, price)
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
            print(f"Added {item_name} to the inventory.")

    def update_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] = quantity
            self.inventory[item_name]['price'] = price
            print(f"Updated {item_name} in the inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Removed {item_name} from the inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    def generate_report(self):
        print("Current Inventory Report:")
        for item_name, item_data in self.inventory.items():
            quantity = item_data['quantity']
            price = item_data['price']
            print(f"{item_name}: Quantity - {quantity}, Price - ${price:.2f}")

if __name__ == "__main__":
    inventory_system = InventoryManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Add new item")
        print("2. Update item")
        print("3. Remove item")
        print("4. Generate report")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory_system.add_item(item_name, quantity, price)

        elif choice == '2':
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory_system.update_item(item_name, quantity, price)

        elif choice == '3':
            item_name = input("Enter item name to remove: ")
            inventory_system.remove_item(item_name)

        elif choice == '4':
            inventory_system.generate_report()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please select a valid option.")
