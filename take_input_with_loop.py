
'''
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter the element {i+1}: "))
    a.append(element)
print(f"List: {a}")
print("Sum of of list is:", sum(a))
'''

'''
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = (input(f"Enter the element {i+1}: "))
    a.append(element)
print(f"List: {a}")
'''
'''
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
li = list(map(int, input("Enter numbers seperated by space: ").split()))
print(f"Our list is: {li} ")
print("Sum of list is:", sum(li))
'''

li = [x.split(",") for x in input("Enter nested list (use commas and semicolons): ").split(";")]
print("Nested List:", li)