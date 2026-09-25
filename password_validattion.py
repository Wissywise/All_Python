# Uses built-in function, user defined functions. modules and decision-making
# validate password program
import re  # import a built-in module named re which provides a set of powerful regular expression facilities (pattern matching)

# Define a function called validate_password that checks if a password is strong
def validate_password(password):  # user defined function named validate password
    # Check if the password length is less than 8 characters
    if len(password) < 8:  # len is a built-in function
        return False    # If too short, return False (invalid password)
    # Check if the password contains at least one lowercase letter (a–z)
    if not re.search("[a-z]", password):
        return False    # If no lowercase letter is found, return False
    # Check if the password contains at least one uppercase letter (A–Z)
    if not re.search("[A-Z]", password):
        return False    # If no uppercase letter is found, return False
    # Check if the password contains at least one digit (0–9)
    if not re.search("[0-9]", password):
        return False    # If no number is found, return False
    # If all conditions are met, the password is valid
    return True


password = input("create a new password: ") # Ask the user to input a new password
if validate_password(password): # Call the validate_password function and check the result
    print("Valid password") # If the function returns True
else:
    print("Invalid password, try again please.") # If the function returns False