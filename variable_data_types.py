#This program will demonstrate how we can create Variables, use data types and obtain inputs
#Deaclare variables and assign values
full_name = "Joe Bloggs" #String
age = 25  #Integer
height_in_cm = 152.4  #float
home_owner = True  #Boolea, True or False must start with uppercase

#Add a print statement to the output of each variable
print(full_name)
print(age)
print(height_in_cm)
print(home_owner)

print("My name is " + full_name) #Challenge output the rest of the data in this format

#take an input from the user to make our program interactive
pet = input("Which pet do you own?")
print("Nice you own: " + pet) #Output user response

print("---------------------------------------------------------------------------------------")

#CHALLENGE: can you add more?
your_name = input("Please enter your name:")
your_age = int(input("Please enter your age:"))
print(f"Your name is {your_name} and you are {your_age} years old")
