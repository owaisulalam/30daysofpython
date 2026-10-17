# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print('company =', company)

# Print the length of the company string using len() method and print().
print('len(company) =', len(company))

# Change all the characters to uppercase letters using upper() method.
print('company.upper() =', company.upper())

# Change all the characters to lowercase letters using lower() method.
print('company.lower() =', company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print('capitalize() =', company.capitalize())
print('title() =', company.title())
print('swapcase() =', company.swapcase())

# Cut(slice) out the first word of Coding For All string.
first_word = company[0:7]
print('first_word =', first_word)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print('index() =', company.index('Coding'))
print('find() =', company.find('Coding'))
print('startswith() =', company.startswith('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print('replace() =', company.replace('Coding', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
everyone = "Python for Everyone"
print('Everyone to All =', everyone.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print('split() =', company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('split() =', companies.split(','))

# What is the character at index 0 in the string Coding For All.
print('Char at index 0 =', company[0])

# What is the last index of the string Coding For All.
last_char = company[len(company) - 1]
print('Char at last index =', last_char)

# What character is at index 10 in "Coding For All" string.
print("Char at index 10 =", company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
abbreviation = everyone.split()
P = abbreviation[0][0]
f = abbreviation[1][0]
E = abbreviation[2][0]
print('abbreviation =', P + f + E)

# Create an acronym or an abbreviation for the name 'Coding For All'.
company_split = company.split()
C = company_split[0][0]
F = company_split[1][0]
A = company_split[2][0]
print('abbreviation =', C + F + A)

# Use index to determine the position of the first occurrence of C in Coding For All.
print('First occurrence of C in Coding For All is at index', company.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print('First occurrence of F in Coding For All is at index', company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Last occurrence of l in Coding For All People', 'Coding For All People'.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('First occurrence of the word \'because\'', 'You cannot end a sentence with because because because is a conjunction'.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('Last occurrence of the word \'because\'', 'You cannot end a sentence with because because because is a conjunction'.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'[31:54])

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('First occurrence of the word \'because\'', 'You cannot end a sentence with because because because is a conjunction'.find('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'[31:54])

# Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(company.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
print('30DaysofPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabeneh  250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
print('radius =', radius) 
area = 3.14 * radius ** 2
print('area = 3.14 * radius ** 2')
print(f'The area of a circle with radius {radius} is {area} meters square.')

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')