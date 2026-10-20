A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
A_and_B = A.union(B)
print(A_and_B)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print('Is A subset of B:', A.issubset(B))

# Are A and B disjoint sets
print("Are A and B disjoint sets;", A.isdisjoint(B))

# Join A with B and B with A
A_with_B = A.union(B)
print('A joined with B:', A_with_B)
B_with_A = B.union(A)
print('B joined with A:', B_with_A)

# What is the symmetric difference between A and B
print('What is the symmetric difference between A and B:', A.symmetric_difference(B))

# Delete the sets completely