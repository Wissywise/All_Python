"""What This Covers:

Dictionary creation

Updating values

Adding new key-value pairs

Looping through dictionaries

Function with simple if/else

Dictionary merging using .update()

Membership decision check using in

Clean formatted output"""

#Create base directory with three employees
employees = {
    101: {"name": "Alice Johnson", "role": "Manager"},
    102: {"name": "Bob Smith", "role": "Analyst"},
    103: {"name": "Carol White", "role": "Developer"}
}

# Print total count
print("Total Employees:", len(employees))


#Update role of ID 102 and add new employee 104
employees[102]["role"] = "Senior Analyst"
employees[104] = {"name": "David Brown", "role": "Intern"}

print("\nUpdated Directory:")
print(employees)


#Print clean roster line by line
print("\nEmployee Roster:")
for emp_id, info in employees.items():
    print(f"{emp_id} - {info['name']} ({info['role']})")


#Function to get role (no nesting)
def get_role(emp_id, data):
    if emp_id in data:
        return data[emp_id]["role"]
    else:
        return "Not Found"


# Show two calls
print("\nRole Lookup:")
print("ID 101:", get_role(101, employees))   # Found
print("ID 999:", get_role(999, employees))   # Not Found


#Merge another department dictionary
new_department = {
    201: {"name": "Eve Black", "role": "HR Manager"},
    202: {"name": "Frank Green", "role": "Accountant"}
}

employees.update(new_department)

print("\nMerged Directory:")
for emp_id, info in employees.items():
    print(f"{emp_id} - {info['name']} ({info['role']})")


#Decision check
target_id = 201

if target_id in employees:
    print("\nEmployee Ready")
else:
    print("\nID Missing")