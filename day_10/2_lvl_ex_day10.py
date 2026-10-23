# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
total = 0
for i in range(101):
    total += i 
print('The sum of all numbers is', total)
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
even_sum = 0
odd_sum = 0
for j in range(101):
    if j % 2 == 0:
        even_sum += j
    else:
        odd_sum +=j 
print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')