""" In Python, tuples are "immutable," meaning once they are created, they cannot be changed.This
makes them perfect for a seat map where you don't want the layout to be accidentally modified.
Here is your seat management tool, built using tuples and the specific logic you requested."""

""" Creating the Seat Map
We use a tuple of tuples, where each individual seat is represented by a coordinate pair: (row, number)."""

# Initial tuple of seats (Row, Seat Number)
seat_map = (
    ("A", 1),
    ("A", 2),
    ("B", 1),
    ("B", 2),
    ("C", 1)
)

print(f"Total seats initially: {len(seat_map)}")

# Count seats specifically in Row A
count_a = 0
for seat in seat_map:
    if seat[0] == "A":
        count_a += 1

print(f"Seats in Row A: {count_a}")


"""
Finding a Seat
This function uses a loop to check each "coordinate" in our map. We use break to stop as soon as we 
find the target to save processing power.
"""

def find_seat(target, seat_map):
    """Returns the index of the seat if found, otherwise 'Not Found'."""
    for index, seat in enumerate(seat_map):
        if seat == target:
            result = index
            break  # Exit the loop immediately once found
    else:
        # The else block of a loop runs only if 'break' was NOT hit
        return "Not Found"

    return result


# Function calls
print(f"Index of ('B', 1): {find_seat(('B', 1), seat_map)}")
print(f"Index of ('Z', 9): {find_seat(('Z', 9), seat_map)}")

# Extending the Seat Map (Concatenation)
# Since we can't .append() to a tuple, we create a new one by adding (concatenating) two tuples together.


# Create extra seats and concatenate
extra_seats = (("D", 1), ("D", 2))
full_map = seat_map + extra_seats

# Slicing the last two seats
print(f"Last two seats in updated map: {full_map[-2:]}")

# Nested Tuples and Row Filtering
# In this section, we create a nested structure to represent the venue rows and then iterate through them to find specific labels.


# Nested tuple: (Row Label, (Seat Numbers))
venue_layout = (
    ("A", (1, 2, 3)),
    ("B", (1, 2)),
    ("C", (1, 2, 3, 4))
)

print("\n--- Printing all seats in Row B ---")
for row_label, seats in venue_layout:
    if row_label == "B":
        for seat_num in seats:
            print(f"Seat: {row_label}{seat_num}")



"""
#Create a tuple of seats and print the total. (Each seat is (row, number).)

seats = (("A", 1), ("A", 2), ("A", 3), ("B", 1), ("B", 2))

print(len(seats))  # total seats

#Count how many seats are in row "A" using a loop and if/else (do not convert to list).

count_a = 0

for seat in seats:

    if seat[0] == "A":

        count_a = count_a + 1

    else:

        count_a = count_a

print(count_a)  # seats in row A

#Write a function find_seat(target, seat_map) that returns the index of a seat if found, otherwise "Not Found". Use a loop and break.

def find_seat(target, seat_map):

    result = "Not Found"

    index = 0

    for item in seat_map:

        if item == target:

            result = index

            break

        else:

            result = result

        index = index + 1

    return result



print(find_seat(("A", 2), seats))  # index or "Not Found"

print(find_seat(("C", 1), seats))  # "Not Found"

#Add extra seats by concatenating another tuple, then print the last two using slicing.

extra = (("B", 3), ("C", 1))

all_seats = seats + extra

print(all_seats[-2:])  # last two seats

#Make a small nested tuple of rows and their labels, then print all seats in row "B" using a loop.

rows = (("A", ("A1", "A2", "A3")), ("B", ("B1", "B2", "B3")))

for row in rows:

    if row[0] == "B":

        for label in row[1]:

            print(label)
"""