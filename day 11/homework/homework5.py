# List of numbers
numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 109]

# Initialize sum variable
total_sum = 0

# Use range to iterate through even indices (0, 2, 4, ...)
for i in range(0, len(numbers), 2):
    total_sum += numbers[i]

# Print the total sum
print("The sum of numbers at even indices is:", total_sum)