all_restaurants = {"McDonald's", "Burger King", "Wendy's", "Taco Bell", "Subway", "KFC"}
fast_food = {"McDonald's", "Burger King", "Wendy's","Taco Mill"}
# Check if fast_food is a subset of all_restaurants
is_subset = fast_food.issubset(all_restaurants)
print(f"Is fast_food a subset of all_restaurants? {is_subset}")
# Check if all_restaurants is a superset of fast_food
is_superset = all_restaurants.issuperset(fast_food)
print(f"Is all_restaurants a superset of fast_food? {is_superset}")