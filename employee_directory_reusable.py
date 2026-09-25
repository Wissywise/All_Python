class EmployeeDirectory:
    def __init__(self):
        # Base directory with three employees
        self.employees = {
            101: {"name": "Alice Johnson", "role": "Manager"},
            102: {"name": "Bob Smith", "role": "Analyst"},
            103: {"name": "Carol White", "role": "Developer"}
        }

    # Add or update employee
    def add_or_update_employee(self, emp_id, name, role):
        self.employees[emp_id] = {"name": name, "role": role}

    # Update role only
    def update_role(self, emp_id, new_role):
        if emp_id in self.employees:
            self.employees[emp_id]["role"] = new_role
        else:
            print("Employee not found.")

    # List all employees
    def list_employees(self):
        for emp_id, info in self.employees.items():
            print(f"{emp_id} - {info['name']} ({info['role']})")

    # Get role (no nesting)
    def get_role(self, emp_id):
        if emp_id in self.employees:
            return self.employees[emp_id]["role"]
        else:
            return "Not Found"

    # Merge another department
    def merge_department(self, new_department):
        self.employees.update(new_department)

    # Total count
    def total_count(self):
        return len(self.employees)

    # Decision check
    def check_employee(self, target_id):
        if target_id in self.employees:
            print("Employee Ready")
        else:
            print("ID Missing")


# =========================
# Demonstration
# =========================

directory = EmployeeDirectory()

# Print total count
print("Total Employees:", directory.total_count())

# Update role of ID 102
directory.update_role(102, "Senior Analyst")

# Add new employee 104
directory.add_or_update_employee(104, "David Brown", "Intern")

print("\nUpdated Directory:")
directory.list_employees()

# Role lookup
print("\nRole Lookup:")
print("ID 101:", directory.get_role(101))  # Found
print("ID 999:", directory.get_role(999))  # Not Found

# Merge another department
new_department = {
    201: {"name": "Eve Black", "role": "HR Manager"},
    202: {"name": "Frank Green", "role": "Accountant"}
}

directory.merge_department(new_department)

print("\nMerged Directory:")
directory.list_employees()

# Decision check
directory.check_employee(201)
