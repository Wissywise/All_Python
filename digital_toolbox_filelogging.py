"""
Why this approach is "Support Engineer" standard:
The with Statement: We use with open(...). This is a Context Manager. It ensures that the file is properly
closed after we finish writing, even if the program crashes. Without this, you risk "corrupting" the file or
leaking memory.

Formatting the Output: We used .strftime() to make the timestamp readable. In a lab, knowing exactly when
the "Cables" were replaced is critical for tracking hardware life cycles.

The try/except Block: In a digital lab, file systems might be read-only or full. Adding error handling ensures
your code doesn't just "die" if it can't write the log—it tells you why.

What the maintenance_log.txt file looks like:
SYSTEM MAINTENANCE LOG Timestamp: 2026-02-27 17:40:12
Tools: 2 items working Cables: Replaced with backup Sensors: 2 items working
"""

# Assuming the 'report' dictionary from our previous step is already populated:
# report = {'Tools': '2 items working', 'Cables': 'Replaced with backup', 'Sensors': '2 items working'}

import datetime

# 1. Define the Data (The missing 'report' variable)
inventory = {
    "Tools": {"Screwdriver": "Working", "Drill": "Working", "Saw": "Faulty"},
    "Cables": {"HDMI": "Faulty", "Ethernet": "Faulty", "USB-C": "Working"},
    "Sensors": {"Motion": "Working", "Temperature": "Working", "Pressure": "Faulty"}
}

# 2. Process the inventory to create the 'report'
report = {}
for category, items in inventory.items():
    working_count = sum(1 for status in items.values() if status == "Working")
    faulty_count = sum(1 for status in items.values() if status == "Faulty")

    if faulty_count > 1:
        report[category] = "Replaced with backup"
    else:
        report[category] = f"{working_count} items working"


# 3. Define the Logging Function
def generate_log_file(report_data, filename="maintenance_log.txt"):
    """Saves the status report to a timestamped text file."""
    try:
        with open(filename, "w") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"SYSTEM MAINTENANCE LOG\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write("-" * 30 + "\n")

            for category, status in report_data.items():
                file.write(f"{category}: {status}\n")

            file.write("-" * 30 + "\n")
            file.write("End of Report\n")

        return f"Successfully saved to {filename}"

    except Exception as e:
        return f"Error writing to file: {e}"


# 4. Execute the logging (Now 'report' is defined!)
log_status = generate_log_file(report)
print(log_status)