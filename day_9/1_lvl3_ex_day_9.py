# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print('Middle skill:', person['skills'][len(person['skills']) // 2])
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    print('Python skill present:', 'Python' in person['skills'])

#   * If a person skills has only JavaScript and React, print('He is a front end developer'), 
#   * if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#   * if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#   * else print('unknown title') - for more accurate results more conditions can be nested!
skills = person['skills']
if 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif  skills == ['JavaScript', 'React']:
    print('He is a front end developer')
else:
    print('unknown title')

#   * If the person is married and if he lives in Finland, print the information in the following format:
#   *   Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')