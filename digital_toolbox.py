"""
Engineering Breakdown
items() and isinstance(): We use .items() to unpack both the category name and its internal dictionary.
The isinstance(items, dict) check paired with continue ensures that if a stray piece of data
(like a simple string) accidentally gets into the inventory, our script won't crash.

The "Faulty" Threshold (break): The moment faulty_count hits 2, the inner loop terminates.
This simulates a system that stops scanning once a "safety limit" is reached to save resources.

Nested Logic: We check the results of our inner loop (counts) to decide what the outer report
dictionary should look like.

Dictionary Lookup: Using if category in backup_inventory allows us to gracefully swap out
failing hardware for our pre-defined backup.

Final Output:
Too many faulty items in Cables, skipping further checks.

Final Equipment Status Report:
Tools: 2 items working
Cables: Replaced with backup
Sensors: 2 items working
"""

# The main inventory and a backup for failing categories
inventory = {
    "Tools": {"Screwdriver": "Working", "Drill": "Working", "Saw": "Faulty"},
    "Cables": {"HDMI": "Faulty", "Ethernet": "Faulty", "USB-C": "Working"},
    "Sensors": {"Motion": "Working", "Temperature": "Working", "Pressure": "Faulty"}
}

backup_inventory = {"Cables": "Replaced with backup"}

# This will store our final report results
report = {}

for category, items in inventory.items():
    # Defensive check: if it's not a dictionary, skip it using continue
    if not isinstance(items, dict):
        continue

    working_count = 0
    faulty_count = 0

    for item_name, status in items.items():
        if status == "Working":
            working_count += 1
        elif status == "Faulty":
            faulty_count += 1

        # Rule: If more than 1 faulty item is found, stop checking this category
        if faulty_count > 1:
            print(f"Too many faulty items in {category}, skipping further checks.")
            break

    # Logic for generating the report entry
    if faulty_count > 1:
        # Check if we have a backup for this specific failed category
        if category in backup_inventory:
            report[category] = backup_inventory[category]
        else:
            report[category] = "Offline (No Backup)"
    elif working_count == 0:
        report[category] = "Replaced with backup"
    else:
        report[category] = f"{working_count} items working"

# Final Output Display
print("\nFinal Equipment Status Report:")
for category, status in report.items():
    print(f"{category}: {status}")