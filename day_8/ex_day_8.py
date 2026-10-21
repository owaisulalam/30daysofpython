# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name' : 'daisy',
    'color':'golden',
    'breed':'golden retiever',
    'legs':'four',
    'age':'4'
}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Elena',
    'last_name':'Rostova',
    'gender':'female',
    'age':'22',
    'marital_status':'single',
    'skills':['python', 'data_analysis', 'technical_writing'],
    'country':'canada',
    'city':'toronto',
    'address':'742-Evergreen Terrace'
}
# Get the length of the student dictionary
print('Length of student dict:', len(student))

# Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')))

# Modify the skills values by adding one or two skills
student['skills'].append('SQL')
print(student)

# Get the dictionary keys as a list
keys_list = student.keys()
print(keys_list)

# Get the dictionary values as a list
values_list = student.values()
print(values_list) 

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('marital_status')
print('After deleting marital_status:', student)

# Delete one of the dictionaries
del dog
print('dog dictionary deleted.')