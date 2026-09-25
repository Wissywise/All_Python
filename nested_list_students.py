students = [
    ["Mansah", 21, [72, 91, 85, 88]],
    ["Kwame", 22, [65, 78, 82, 90]],
    ["Ama", 20, [80, 85, 88, 92]],
    ["Kojo", 23, [70, 75, 80, 85]],
    ["Esi", 21, [90, 92, 95, 98]]
]

print("Student Records:")

for student in students:
    name = student[0]
    age = student[1]
    grades = student[2]




    #average_grade = sum(grades) / len(grades)

print(f"Name: {name}, Age: {age}, Grade: {grades}")