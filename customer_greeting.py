#Customer greetings based on range of hours in a day
#store the hours in a variable (0 - 23)
hour = int(input("Enter the current hour (0-23): "))
#hour = 10

#Determine the greeting based on the hour
if 5 <= hour <= 11:
    greeting = "Good Morning!"
elif 12 <= hour <= 16:
    greeting = "Good Afternoon!"
elif 17 <= hour <= 20:
    greeting = "Good Evening!"
elif 0 <= hour <= 4 or 21 <= hour <= 23:
    greeting = "Good Night!"
else:
    greeting = "Invalid hour entered: Please enter a value between 0 and 23."
print(f"Good {greeting}")



