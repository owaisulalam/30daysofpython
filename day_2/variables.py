# Day 2: 30 Days of python programming

# Variables in Python

first_name = 'Owais'
last_name = 'Sofi'
full_name = 'Owais ul alam sofi'
country = 'India'
city = 'Srinagar'
age = 22
year = 2026
is_married = False
is_true = True
is_light = True
name, roll_num, sem, university = 'Owais', 26, '7th', 'Central University of Kashmir'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(name))
print(type(roll_num))
print(type(sem))
print(type(university))

print(len(first_name))
print(len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_two ** num_one
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
area_of_circle = (22/7) * radius ** 2
circum_of_circle = 2 * (22/7) * radius
print(area_of_circle, circum_of_circle)

r = int(input("Enter the radius: "))
area_of_circle = (22/7) * r ** 2
print(area_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print(first_name, last_name, country, age)
print(help('keywords'))