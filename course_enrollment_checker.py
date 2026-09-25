# Create a set of students enrolled in the Python for beginners course
python_beginners = {"Emma", "Liam", "Olivia", "Noah"}

# Create a set of students enrolled in the Python Projects course
python_projects = {"Liam", "Olivia", "Ava", "Sophia"}

#Students enrolled in both courses (intersection)
# .intersection() returns only the elements that appear in BOTH sets.
both_courses = python_beginners.intersection(python_projects)

# Print the result so we can see which students are in both classes.
print(f"Students enrolled in both courses: {both_courses}")

# Students ONLY in the Beginners course
# .difference() returns items that are in the first set but NOT in the second.
only_beginners = python_beginners.difference(python_projects)

# Print the students who are only taking the beginner course.
print(f"Students enrolled in only Python for beginners: {only_beginners}")

# Students ONLY in the Projects course
only_projects = python_projects.difference(python_beginners)

# Print the students who are only taking the project course.
print(f"Students enrolled in only Python Projects: {only_projects}")

# Total unique students across BOTH courses
# .union() combines both sets and removes duplicates automatically
all_students = python_beginners.union(python_projects)

# Print the full set of unique students.
print(f"Total unique students across both courses: {all_students}")



