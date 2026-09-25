#How it works:
#Applies age-based discount first.

#Adds an extra 5% if the customer has a loyalty card.

#Calculates and prints the final price rounded to 2 decimal places.

#Includes basic error handling for invalid inputs.

def calculate_price(base_price, age, has_loyalty_card):
    # Determine age-based discount
    if age < 18:
        discount = 0.20
    elif 18 <= age <= 60:
        discount = 0.10
    else:  # age > 60
        discount = 0.50

    # Add loyalty discount if applicable
    if has_loyalty_card:
        discount += 0.05

    # Calculate final price
    final_price = base_price * (1 - discount)
    return round(final_price, 2)


# --- Main Program ---
try:
    base_price = float(input("Enter the base price of the coffee: $"))
    age = int(input("Enter customer's age: "))
    loyalty_input = input("Does the customer have a loyalty card? (yes/no): ").strip().lower()

    has_loyalty_card = loyalty_input == "yes"

    final_price = calculate_price(base_price, age, has_loyalty_card)

    print(f"\nFinal price to pay: ${final_price}")

except ValueError:
    print("Invalid input. Please enter correct numeric values for price and age.")
