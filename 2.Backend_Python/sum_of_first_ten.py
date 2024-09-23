##Display sum of first ten elements starting from element 5:
numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]


# Extract the first ten elements starting from the fifth element (index 4)
subset = numbers[4:14]

# Calculate the sum of these elements
result = sum(subset)

print("The sum of the first ten elements starting from the fifth element is:", result)
