# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b :
    print(f'{a} is greater than {b}')
elif a < b :
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')
