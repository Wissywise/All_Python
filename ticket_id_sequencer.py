# Print IDs from 1001 to 1010

"""for user_id in range(1001, 1011):

    if user_id == 1005:
        continue  # Skip blocked ID

    if user_id == 1009:
        print(f"ID {user_id} - {'VIP' if user_id % 2 == 0 else 'Standard'}")
        break  # Stop after reaching 1009

    if user_id % 2 == 0:
        print(f"ID {user_id} - VIP")
    else:
        print(f"ID {user_id} - Standard")

print("---------------------------------------------------------")


for user_id in range(1001, 1011):
    # Stop the process when we reach 1009
    if user_id == 1009:
        print(f"ID {user_id}: System termination reached. Stopping.")
        break

    # Skip the blocked ID 1005
    if user_id == 1005:
        print(f"ID {user_id}: Blocked. Skipping...")
        continue

    # Label Even as VIP and Odd as Standard
    if user_id % 2 == 0:
        status = "VIP"
    else:
        status = "Standard"

    print(f"ID {user_id}: {status}")

print("----------------------------------------------------------")"""

#Create the loop to print IDs 1001–1010.
start_id = 1001
end_id = 1010

for tid in range(start_id, end_id + 1):
    print(tid)

#Add an if/else to label even IDs as “VIP” and odd as “Standard.”
start_id = 1001
end_id = 1010

for tid in range(start_id, end_id + 1):
    if tid % 2 == 0:
        label = "VIP"
    else:
        label = "Standard"
    print(f"ID: {tid} - {label}")

#Skip the blocked ID 1005 using continue.
start_id = 1001
end_id = 1010
for tid in range(start_id, end_id + 1):
    if tid == 1005:
        continue
    if tid % 2 == 0:
        label = "VIP"
    else:
        label = "Standard"
    print(f"ID: {tid} - {label}")

#Stop after reaching 1009 using break and show the final output format.
start_id = 1001
end_id = 1010
for tid in range(start_id, end_id + 1):
    if tid == 1005:
        continue
    if tid % 2 == 0:
        label = "VIP"
    else:
        label = "Standard"
    print(f"ID: {tid} - {label}")

    if tid == 1009:
        break