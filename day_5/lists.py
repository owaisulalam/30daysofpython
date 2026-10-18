# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items = ['keyboard', 'trackpad', 'screen', 'battery', 'processor', 'ram', 'memory']

# Find the length of your list
print(len(items))

# Get the first item, the middle item and the last item of the list
first_item = items[0]
print(first_item)
middle_item = items[3]
print(middle_item)
last_index = len(items) - 1
last_item = items[last_index]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Owais', 22, 5.7, False, 'Kashmir']
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
first_company = it_companies[0]
print('first company', first_company)
middle_company = it_companies[3]
print('middle company', middle_company)
last_company_index = len(it_companies) - 1
last_company = it_companies[last_company_index]
print('Last_company', last_company)

# Print the list after modifying one of the companies
it_companies[3] = 'Samsung'
print('modifying', it_companies)

# Add an IT company to it_companies
it_companies.append('Apple')
print('append()', it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4,'Infosys')
print('insert()', it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print('upper()', it_companies)

# Join the it_companies with a string '#;  '
hash_list = ['#; ']
it_companies += hash_list
print('join', it_companies)

# Check if a certain company exists in the it_companies list.
exist = 'Apple' in it_companies
print('exist:', exist)

# Sort the list using sort() method
it_companies.sort()
print('sort()', it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print('sort(reverse=True)', it_companies)

# Slice out the first 3 companies from the list
first_3_companies = it_companies[0:3]
print('first 3 companies:', first_3_companies)

# Slice out the last 3 companies from the list
last_3_companies = it_companies[-3:]
print('last_3_companies', last_3_companies)

# Slice out the middle IT company or companies from the list
middle_companies = it_companies[4:6]
print('middle_companies', middle_companies)

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print('first-removed', it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove('Google')
print('middle-removed', it_companies)

# Remove the last IT company from the list
it_companies.pop()
print('Last-removed or pop()', it_companies)

# Remove all IT companies from the list
it_companies.clear()
print('All removed', it_companies)

# Destroy the IT companies list
del it_companies
# print(it_companies)

# Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end += back_end

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('Full_stack =', full_stack)