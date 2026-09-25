class EmployeeDirectory:
    def __init__(self):
        # Base directory with three employees
        self.employees = {
            101: {"name": "Alice Johnson", "role": "Manager"},
            102: {"name": "Bob Smith", "role": "Analyst"},
            103: {"name": "Carol White", "role": "Developer"}
        }

    def add_or_update_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        role = input("Enter Role: ")
        self.employees[emp_id] = {"name": name, "role": role}
        print("Employee added/updated successfully.")

    def update_role(self):
        emp_id = int(input("Enter Employee ID to update: "))
        if emp_id in self.employees:
            new_role = input("Enter New Role: ")
            self.employees[emp_id]["role"] = new_role
            print("Role updated successfully.")
        else:
            print("Employee not found.")

    def list_employees(self):
        print("\nEmployee Roster:")
        for emp_id, info in self.employees.items():
            print(f"{emp_id} - {info['name']} ({info['role']})")

    def get_role(self):
        emp_id = int(input("Enter Employee ID to look up: "))
        if emp_id in self.employees:
            print("Role:", self.employees[emp_id]["role"])
        else:
            print("Not Found")

    def merge_department(self):
        print("Enter new department employees.")
        count = int(input("How many employees to merge? "))
        new_department = {}

        for _ in range(count):
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            role = input("Enter Role: ")
            new_department[emp_id] = {"name": name, "role": role}

        self.employees.update(new_department)
        print("Department merged successfully.")

    def total_count(self):
        print("Total Employees:", len(self.employees))

    def decision_check(self):
        target_id = int(input("Enter ID to check: "))
        if target_id in self.employees:
            print("Employee Ready")
        else:
            print("ID Missing")


# =========================
# Interactive Menu
# =========================

directory = EmployeeDirectory()

while True:
    print("\n===== Employee Directory Menu =====")
    print("1. Add/Update Employee")
    print("2. Update Role")
    print("3. List Employees")
    print("4. Get Role by ID")
    print("5. Merge Department")
    print("6. Total Employee Count")
    print("7. Decision Check")
    print("8. Exit")

    choice = input("Choose an option (1-8): ")

    if choice == "1":
        directory.add_or_update_employee()
    elif choice == "2":
        directory.update_role()
    elif choice == "3":
        directory.list_employees()
    elif choice == "4":
        directory.get_role()
    elif choice == "5":
        directory.merge_department()
    elif choice == "6":
        directory.total_count()
    elif choice == "7":
        directory.decision_check()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
