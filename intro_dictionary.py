walmart_inventory = {}

walmart_inventory[1001] = {"name": "Laptop", "price": 999.99, "stock": 50}
walmart_inventory[1002] = {"name": "Smartphone", "price": 499.99, "stock": 200}
walmart_inventory[1003] = {"name": "Headphones", "price": 199.99, "stock": 150}

print("Walmart Inventory:", walmart_inventory)

walmart_inventory[1002]["price"] = 379.99
print("Updated Inventory:", walmart_inventory)


