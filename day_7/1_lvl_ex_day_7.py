# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
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
print('discard() doesn\'t raise any error if the item is not present in the set but remove() does.')
print(it_companies.discard('owais'))
# print(it_companies.remove('owais')) #raised error 