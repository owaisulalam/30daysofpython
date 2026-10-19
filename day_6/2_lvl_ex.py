# Unpack siblings and parents from family_members
family_members = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'father', 'mother')
siblings = family_members[0:7]
print(siblings)
parents = family_members[7:]
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange', 'strawberry', 'mango')
vegetables = ('carrots', 'broccoli', 'spinach', 'potatoes', 'cucumbers')
animal = ('milk', 'eggs', 'honey', 'cheese', 'wool')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[7]
print(middle_item)

# Slice out the first three items and the last three items from food_stuff_lt list
first_3_items = food_stuff_lt[:3]
print(first_3_items)
last_3_items = food_stuff_lt[-3:]
print(last_3_items)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
