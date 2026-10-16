# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python'))    # 6
print(len('dragon'))    # 6
print(len('python') != len('dragon'))   # Falsy statement

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' in 'dragon')

# Find the length of the text python and convert the value to float and convert it to string
print(len('python'))
print(float(len('python')))
print(type(float(len('python'))))
print(str(len('python')))
print(type(str(len('python'))))