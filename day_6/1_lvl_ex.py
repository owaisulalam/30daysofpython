# Create an empty tuple
empty_tpl = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('a', 'b', 'c')
brothers = ('d', 'e', 'f', 'g')

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print('Siblings:',siblings)

# How many siblings do you have?
print('No. of siblings =', len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_and_mother = ('father', 'mother')
family_members = siblings + father_and_mother
print('Family members:', family_members)