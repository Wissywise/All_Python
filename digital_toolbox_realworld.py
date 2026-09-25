"""
In the professional world, we use the if __name__ == "__main__": block. This ensures that your code only runs when the script is executed directly, and not if it's imported as a module into another project. It’s like having a "Start" button on a machine.

Here is your tool refactored into a professional, modular structure.

The Professional "Main" Pattern
"""

import datetime


def process_inventory(inventory _data):
    """Business logic to categorize equipment status."""
    report = {}
    for category, items in inventory_data.items():
        working_count = sum(1 for status in items.values() if status == "Working")
        faulty_count = sum(1 for status in items.values() if status == "Faulty")

        if faulty_count > 1:
            report[category] = "Replaced with backup"
        else:
            report[category] = f"{working_count} items working"
    return report


def generate_log_file(report_data, filename="maintenance_log.txt"):
    """File handling logic to save the report."""
    try:
        with open(filename, "w") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"SYSTEM MAINTENANCE LOG\nTimestamp: {timestamp}\n")
            file.write("-" * 30 + "\n")
            for category, status in report_data.items():
                file.write(f"{category}: {status}\n")
            file.write("-" * 30 + "\nEnd of Report\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def main():
    """Main execution point of the script."""
    # Data is kept inside main to avoid global variable issues
    inventory = {
        "Tools": {"Screwdriver": "Working", "Drill": "Working", "Saw": "Faulty"},
        "Cables": {"HDMI": "Faulty", "Ethernet": "Faulty", "USB-C": "Working"},
        "Sensors": {"Motion": "Working", "Temperature": "Working", "Pressure": "Faulty"}
    }

    print("Step 1: Processing Inventory...")
    final_report = process_inventory(inventory)

    print("Step 2: Generating Log File...")
    success = generate_log_file(final_report)

    if success:
        print("Success: Maintenance log is ready.")
    else:
        print("Failure: Check system permissions.")


# This tells Python: "Only run the main() function if this file is run directly"
if __name__ == "__main__":
    main()

    
    """
    Why this structure is superior:
Encapsulation: The inventory data is now local to the main() function. This prevents "Variable Leaks" where 
other parts of a large program might accidentally change your data.

Reusability: You can now import your process_inventory function into a different script without triggering 
the print statements or file creation.

Readability: Anyone reading your code can look at main() and immediately see the high-level "story" of what 
the script does (Process -> Generate -> Notify).
"""