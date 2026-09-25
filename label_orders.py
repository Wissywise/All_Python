def label_orders(start, end):
    """
    Processes order numbers in a given range.
    - Labels even numbers as 'Priority'
    - Labels odd numbers as 'Standard'
    - Skips blocked order 102
    - Stops processing when order 105 is reached
    """

    for order in range(start, end + 1):

        # Skip blocked order
        if order == 102:
            print(f"Order {order} is blocked. Skipping...")
            continue

        # Stop processing at specific order
        if order == 109:
            print(f"Order {order} reached. Stopping processing.")
            break

        # Label even and odd orders
        if order % 2 == 0:
            print(f"Order {order} - Priority")
        else:
            print(f"Order {order} - Standard")


# Example function call
label_orders(100, 110)