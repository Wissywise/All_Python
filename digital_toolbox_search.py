"""
Adding a search feature turns this script from a static reporter into an interactive tool.
We can use the input() function to let a user query the final_report dictionary we just built.

Here is the updated main() function. I've added a simple loop so you can search for multiple
categories without having to restart the program.

Interactive Support Tool

How the Search Logic Works:
.strip().capitalize(): Users are unpredictable. They might type " tools " or "tools". strip() removes
accidental spaces, and capitalize() ensures "tools" becomes "Tools" to match our dictionary keys.

while True: This creates an infinite loop, allowing the engineer to check multiple items (Tools, then Sensors, etc.)
in one session.

The "Kill Switch": We check if the input is "quit" right at the start. If it is, the break command kills the loop.

final_report.get(query): This is much safer than final_report[query]. If the user types a category that doesn't
exist (like "Drones"), the .get() method returns None instead of crashing your program with a KeyError.
"""

def main():
    """Main execution point of the script with interactive search."""
    inventory = {
        "Tools": {"Screwdriver": "Working", "Drill": "Working", "Saw": "Faulty"},
        "Cables": {"HDMI": "Faulty", "Ethernet": "Faulty", "USB-C": "Working"},
        "Sensors": {"Motion": "Working", "Temperature": "Working", "Pressure": "Faulty"}
    }

    print("Step 1: Processing Inventory...")
    final_report = process_inventory(inventory)

    print("Step 2: Generating Log File...")
    generate_log_file(final_report)

    # --- NEW SEARCH FEATURE ---
    print("\n" + "=" * 30)
    print("EQUIPMENT SEARCH TOOL")
    print("Type a category name (e.g., 'Tools') or 'quit' to exit.")

    while True:
        query = input("\nEnter category to check: ").strip().capitalize()

        if query.lower() == 'quit':
            print("Exiting search tool. Goodbye!")
            break

        # Use .get() to search the dictionary safely
        status = final_report.get(query)

        if status:
            print(f"Status for {query}: {status}")
        else:
            print(f"Error: Category '{query}' not found in inventory.")