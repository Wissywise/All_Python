#Get income from the user
monthly_income = int(input("Enter your total monthly income (in $): "))

#Get expenses from the user
rent = int(input("Enter your monthly rent (in $): "))
groceries = int(input("Enter your monthly groceries expenses (in $): "))
transport = int(input("Enter your monthly transportation expenses (in $): "))
utility = int(input("Enter your monthly utility expenses (in $): "))
other_expenses = int(input("Enter your monthly other expenses (in $): "))

#calculate total expenses
total_expenses = rent + groceries + transport + utility + other_expenses

#calcualte remaining income
remaining_income = monthly_income - total_expenses

#display results
print(f"Total Monthly income: ${monthly_income: .2f}")
print(f"Total Monthly Expenses: ${total_expenses: .2f}")
print(f"The remaining monthly income: ${remaining_income: .2f}")

