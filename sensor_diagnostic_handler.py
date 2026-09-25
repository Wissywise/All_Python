"""
def evaluate_machine(reading):

    Evaluates a single sensor reading and returns machine status.
    Used for automated testing.

    if reading == 0:
        return "Skipped"
    elif reading > 90:
        return "Critical"
    elif reading <= 30:
        return "Maintenance"
    else:
        return "Normal"


def process_sensor_readings(readings):

    Processes a list of sensor readings.
    Prints status, score, and alerts for real-time monitoring.

    for reading in readings:
        status = evaluate_machine(reading)

        print(f"Reading: {reading}")
        print(f"Status: {status}")
        print(f"Score: {reading}")

        if status == "Critical":
            print("ALERT: Immediate shutdown required!")
        elif status == "Maintenance":
            print("Notice: Schedule maintenance check.")
        elif status == "Skipped":
            print("Info: Sensor reading skipped.")

        print("-" * 30)


# Example Usage
sensor_data = [25, 45, 0, 95, 60, 30, 100]
process_sensor_readings(sensor_data)
"""
print("--------------------------------------------------")


# Function to evaluate a single sensor reading
def evaluate_machine(reading):
    """
    Evaluates one temperature reading and returns
    the machine's status as a string.

    This function is designed to be simple and testable,
    so it can be used in automated unit tests.
    """

    # If the sensor reading is 0, it means it was skipped or invalid
    if reading == 0:
        return "Skipped"

    # If the temperature is above 90, it is critical
    # Immediate attention is required
    elif reading > 90:
        return "Critical"

    # If the temperature is 30 or below,
    # the machine may require maintenance
    elif reading <= 30:
        return "Maintenance"

    # If none of the above conditions are met,
    # the machine is operating normally
    else:
        return "Normal"


# Function to process multiple sensor readings
def process_sensor_readings(readings):
    """
    Takes a list of temperature readings and:
    - Evaluates each reading
    - Prints the reading value
    - Prints its status
    - Displays alerts if necessary

    This simulates real-time monitoring output.
    """

    # Loop through each reading in the list
    for reading in readings:

        # Get the status by calling evaluate_machine()
        status = evaluate_machine(reading)

        # Print the raw sensor reading
        print(f"Reading: {reading}")

        # Print the evaluated status
        print(f"Status: {status}")

        # Print the reading as the system score/value
        print(f"Score: {reading}")

        # If the machine is in critical condition,
        # display a high-priority alert
        if status == "Critical":
            print("ALERT: Immediate shutdown required!")

        # If maintenance is required,
        # notify the technician
        elif status == "Maintenance":
            print("Notice: Schedule maintenance check.")

        # If the reading was skipped,
        # display an informational message
        elif status == "Skipped":
            print("Info: Sensor reading skipped.")

        # Print separator line for readability
        print("-" * 30)


# Example sensor data (simulating real-time machine input)
sensor_data = [25, 45, 0, 95, 60, 30, 100]

# Call the function to process the readings
process_sensor_readings(sensor_data)

