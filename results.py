numbers = [5, 12, 7, 18, 3]

result = [n * 2 for n in numbers if n % 2 == 0]
print(result)

print("----------------------------------------------------------------")

my_numbers = [5,12,7,18,3, 20, 25, 30]
result = (n * 2 for n in my_numbers if n % 2 == 0)

for value in result:
    print(value)

print("----------------------------------------------------------------")

by_numbers = [5, 12, 7, 18, 3, 20, 25, 30]
result = {n: n * 2 for n in by_numbers if n % 2 == 0}
print(result)
