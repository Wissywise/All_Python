# Using comparison, logical and assignment operators
# Password username checker program
actual_password = 'password'  # Assignment operator
password_entered = str(input("Please enter your password: "))  # Taking input from the user

if (password_entered != actual_password):  # Relational operator 'not equal to'
    print("Invalid password entered")
else:
    print("Valid password entered")

# CHALLENGE, now let's incorporate username and logical operator
actual_username = 'Joebloggs'  # Assignment operator
username_entered = str(input("Please enter your username: "))  # Taking input from the user
# Introducing logical operator 'or'
if (username_entered != actual_username) or (password_entered != actual_password):
    print("Invalid username or password entered")
else:
    print("Valid username and password entered")