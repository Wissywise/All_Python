import copy

"""
deep copy is used to create a new object and recursively copy all objects found in the original. 
This is useful when you want to create a completely independent copy of a complex object, 
such as a list of lists or a dictionary containing other dictionaries. Changes made to the 
deep copied object will not affect the original object, and vice versa. 
"""

original_list = [1, 2, 3, 4, 5]

deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[1] = 20

print(f"Original List: {original_list}")
print(f"Deep Copied List: {deep_copied_list}")

