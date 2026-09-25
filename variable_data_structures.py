#This program will demonstrate how we can store and manipulate a list (data structures)

shopping_list1 = ["6 apples", "milk", "bread", "12 eggs"] #variable name and assign values in list using brackets
print("How many items on the shopping list?")
print(len(shopping_list1)) #printout how many items are on the list
print("-----------------------------------------------------------------")
shopping_list1.sort()  #Sort the list into alphabetical order
print(shopping_list1) #outputwhat the variable holds
#Run your program here to see the results
print("------------------------------------------------------------------")

shopping_list2 = ["cake", "biscuits", "chocolate"] #variable name and assign value using brackets
shopping_list2.sort(reverse=True) #reverse order list items, remember True needs to start with capital letter
for x in shopping_list2: #output all items one by one until no more
  print(x)
#Run your program here to see the results
print("------------------------------------------------------------------")

full_list = shopping_list1 + shopping_list2 #Use + operator to join lists together and store in new variable
print(full_list)
#Run your program here to see the results
print("-----------------------------------------------------------------")

#CHALLENGE: can you sort list alphabetically, list item one by one and print how many items are in the list?
new_full_list = shopping_list1 + shopping_list2 #Total new list
sorted_new_full_list = sorted(new_full_list) #Sorting the combined list
print(sorted_  print(item)new_full_list)
print("-------------------------------------------------------------------")
for item in sorted_new_full_list: #Print each item one by one

print("Total items in the list:", len(sorted_new_full_list)) #Print how many items are in the list


