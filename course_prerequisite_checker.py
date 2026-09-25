university_name = "Coventry University"

print(f"Welcome to {university_name} AI course prerequisite checker!\n")

coventry_university_ai_course_prerequisites =  {

    "Basic programming knowledge", "Mathematics proficiency",
    "Problem-solving skills", "Logical thinking", "Familiarity with AI concepts"
}

student_courses = set(input("Enter your completed courses (separated by commas): ").split(", "))

student_courses = {course.strip() for course in student_courses}

if coventry_university_ai_course_prerequisites.issubset(student_courses):
    print(f"\nCongratulations! You meet the prerequisites for the AI course at {university_name}.")
else:
    print(f"\nUnfortunately, you do not meet the prerequisites for the AI course at {university_name}.")
    print("\nPlease review the required courses and consider taking them before applying for the AI course.")

    for course in coventry_university_ai_course_prerequisites - student_courses:
        print(f"- {course}")


