#Create a set named current_stock with the codes "P101", "P102", "P103", "P104".
current_stock = {"101", "P102", "P103", "P104", "P105"}

#Print it to confirm no duplicates exist.
print("Print out of the current stock", current_stock)

#Create a set named new_arrivals with "P103", "P104", "P105", "P106"
new_arrivals = {"P104", "P105", "P106", "P107"}

#Print it to confirm no duplicates exist.
print("Print out of the new arrival stock", new_arrivals)

#Use set difference to find which products are truly new
stock_difference = current_stock.difference(new_arrivals)

#Print the result
print("The stock items which are truly new :", stock_difference)

unique_stock = current_stock.union(new_arrivals)
print("The unique stock after union/merging both is: ", current_stock)

#Update the current_stock set to include the new items using the union operator
current_stock =current_stock | new_arrivals

#print the updated set.
print("The current stock after using pipe sign is: ", current_stock)

"""
Use an if statement to check if new_arrivals is a subset of current_stock.
Print "All new arrivals are now in stock" if true.
"""
if new_arrivals.issubset(current_stock):
    print("All new arrivals are in stock.")
else:
    print("Some new arrivals are not in stock.")

#Create a frozen set named discontinued containing "P101" and "P102"
discontinued_items = {"P102", "P103"}
current_stock = current_stock.difference(discontinued_items)
print(current_stock)

print("Current stock after removing discontinued items:", current_stock)
print("Discontinued items:", discontinued_items)

