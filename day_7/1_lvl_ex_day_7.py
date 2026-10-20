# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('length of the set it_companies =', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('Added Twitter:', it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Accenture', 'SAP', 'TCS', 'Infosys'])
print('Added more companies at once:', it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('SAP')
print('Removed SAP:', it_companies)

# What is the difference between remove and discard