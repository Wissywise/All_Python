# Simulate bottle inspection on conveyor belt

for bottle in range(1, 11):

    if bottle == 4:
        print("Bottle 4 is faulty. Skipping...")
        continue

    if bottle == 8:
        print("Critical leak in Bottle 8 . Stopping process.")
        break

    print(f"Bottle {bottle} filled successfully.")


print("--------------------------------------------------")

# Simulating the conveyor belt for 10 bottles
for bottle in range(1, 11):
    if bottle == 4:
        print(f"Bottle {bottle} is faulty. Skipping...")
        continue  # Skips the rest of the code in this iteration

    if bottle == 8:
        print(f"Critical leak in Bottle {bottle}. Stopping process.")
        break  # Terminates the loop entirely

    print(f"Bottle {bottle} filled successfully.")