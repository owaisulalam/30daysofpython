# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

marks = int(input('Enter your marks: '))
if marks <= 100 and marks >= 90:
    print(f'Grade = A')
elif marks <= 89 and marks >= 80:
    print(f'Grade = B')
elif marks <= 79 and marks >= 70:
    print(f'Grade = C')
elif marks <= 69 and marks >= 60:
    print(f'Grade = D')
else:
    print(f'Grade = F')
    

