# Get input from the user
number = int(input("Please enter a number: "))

# Calculate the sum of numbers from 1 to the entered number
total_sum = 0
for i in range(1, number + 1):
    total_sum += i

# Output the result
print(f"The sum of all numbers from 1 to {number} is: {total_sum}")