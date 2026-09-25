# Using comparison and assignment operators
# Grade result program
percentage = int(input("Please enter percentage mark e.g 75: "))  # assignment operator
result = ""  # Assigning empty value to the variale 'result'
if percentage >= 70:  # Greater than or equal to this operator
    result = "Distinction"  # Assignment operator
elif percentage >= 60:
    result = "Merit"
elif percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print("You entered percentage mark of: " + str(percentage) + ", the result awarded is: " + (result))
print("--------------------------------------------------------------------------------------------")

#CHALLENGE,write a program that asks users to enter their percentage mark and returns the following
#A mark of 80% and above is awarded 'A'
#A mark in the range of 70% through to 79% is awarded a 'B'
#A mark in the range of 60% through to 69% is awarded a 'C'
#A mark in the range of 50% through to 59% is awarded a 'D'
#A mark in the range of 40% through to 49% is awarded a 'E'
#A mark less than 40% awarded an 'F'

# Grading based on range of marks
percentage_mark = int(input("Please enter the percentage mark score e.g 50:  "))  # Accept input mark from the user
grading = ""  # Assigning empty value to the result variable

if percentage_mark >= 80: #Greater than operator
     grading = "A"
elif 70 <= percentage_mark <= 79:  #Percentage mark range
     grading = "B"
elif 60 <= percentage_mark <= 69:
     grading = "C"
elif 50 <= percentage_mark <= 59:
     grading = "D"
elif 40 <= percentage_mark <= 49:
     grading = "E"
else:
     grading = "F"

print(("You entered mark of ") + str(percentage_mark) + ("%") + " and the grade awarded is: " + str(grading))
