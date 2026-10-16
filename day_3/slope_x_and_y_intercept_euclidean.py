# Calculate the slope, x-intercept and y-intercept of y = 2x -2

# Comparing with the formula y = mx + b
m1 = 2   # slope
b = -2  # y-intercept

# Slope 
slope = m1

# y-intercept
y_intercept = b

# Calculating the x_intercept
x_intercept = -b / m1

print("Slope: ", slope)
print("y-intercept: ", y_intercept)
print("x-intercept: ", x_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1, x2, y2 = 2, 2, 6, 10
m2 = (y2 - y1) / (x2 - x1)
print("Slope = ", m2)

euclidean = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
print("Euclidean distance = ", euclidean)

# Compare the slopes in tasks 8 and 9.

print(m1 < m2)
print(m1 > m2)
print(m1 == m2)