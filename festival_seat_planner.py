#Import array module

from array import array

#Create an array of seat numbers for a festival with 8 seats
seats = array('i', [101, 102, 103, 104, 105, 106, 107, 108])

#Print seat numbers to confirm they are correct
print("These Seat numbers at the festival:", seats)

#Print the total number of seats available
print(f"Total number of seats available: {len(seats)}")

#Replace seat 105 with 110
for i in range(len(seats)):
    if seats[i] == 104:
        seats[i] = 110  #Replace seat number 104 with 110
        break   #Stop the loop after replacing the seat number

#Print the updated seat numbers
print(f"Updated seat numbers: {seats}")

#Show the seat numbers line by line
print("Seat numbers line by line:")
for seat in seats:
    print(seat)

#Show seat slicing
print("Sliced seat numbers (first 4):", seats[:4])  #printing first four seat numbers
print("Sliced seat numbers (last 4):", seats[4:])   #printing last four seat numbers
print("Sliced seat numbers (middle 4):", seats[2:6]) #printing middle four seat numbers
print("Last three seat numbers:", seats[-3:])  #printing last three seat numbers

#Reserved seats stored in another array
reserved_seats = array('i', [102, 106])

#Loop through all seats and check if they are reserved or available
print("Seat availability:")
for seat in seats:
    if seat in reserved_seats:
        print(f"Seat {seat} is reserved.")
    else:
        print(f"Seat {seat} is available.")

"""
Function to find next available seat: Returns the first first seat number that is 
- greater than or equal to the starting seat 
- not in the reserved list. 
- If no such seat is found, it returns a message indicating that no available seats are found.
"""
def find_next_available_seat(start_seat, seats, reserved):
    for seat in seats:
        if seat >= start_seat and seat not in reserved:
            return seat
    return "No available seats found"
#Test the function to find the next available seat starting from 104
next_seat = find_next_available_seat(104, seats, reserved_seats)
print(f"The next available seat starting from 104 is: {next_seat}")

