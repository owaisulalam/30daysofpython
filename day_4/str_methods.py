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