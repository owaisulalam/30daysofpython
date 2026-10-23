# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i, end=" ")
print()

num = 0
while num < 11:
    print(num, end=" ")
    num += 1 
print()

# Iterate 10 to 0 using for loop, do the same using while loop.
for j in range(10,-1,-1):
    print(j, end=" ")
print()
neg = 10
while neg >= 0:
    print(neg, end=" ")
    neg -= 1
print()

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for k in range(1,8):
    print('#' * k)

# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for l in range(1, 9):
    for m in range(1, 9):
        print('#', end=" ")
    print()

# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for n in range(11):
    print(f'{n} x {n} = {n * n}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in lst:
    print(items, end=" ")
print()
# Use for loop to iterate from 0 to 100 and print only even numbers
for even in range(101):
    if even % 2 == 0:
        print(even, end=" ")
print()

# Use for loop to iterate from 0 to 100 and print only odd numbers
for odd in range(101):
    if odd % 2 == 0:
        continue
    print(odd, end=" ")