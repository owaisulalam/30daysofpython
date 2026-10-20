age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print('length of list =', len(age))
print('length of set =', len(age_set))

# Explain the difference between the following data types: string, list, tuple and set
print('Any data under single, double or triple quote are strings.')
print('List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.')
print('Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.')
print('Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.')

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
sentence_split = sentence.split()
sentence_set = set(sentence_split)
print('Unique words =', len(sentence_set))