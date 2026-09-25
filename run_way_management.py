# Nested tuple of airplanes
airplanes = (
    ("BA117", "approaching"),
    ("EK901", "delayed"),
    ("LH400", "approaching"),
    ("AA390", "emergency"),
    ("LT270", "landed"),
    ("AF123", "approaching"),
    ("UA456", "delayed"),

)

approaching_count = 0

delayed_count = 0

# Loop through the airplanes
for plane in airplanes:
    plane_id, status = plane  # unpacking the nested tuple

    if status == "landed":  # Skip landed airplanes
        continue

    elif status == "delayed":
        print(f"Attention: {plane_id} is delayed!. Further investigation needed.")
        delayed_count += 1
    elif status == "approaching":
        print(f"Plane {plane_id} is approaching. Prepare clearance for landing.")
        approaching_count += 1

    elif status == "emergency":
        print(f"Critical Alert! {plane_id} has emergency. Stopping checks for Further investigation.")
        break  # Stop checks immediately

    # Final account of approaching and delayed airplanes
    print(f"Total approaching planes: {approaching_count}.")
    print(f"Total delayed planes: {delayed_count}.")

