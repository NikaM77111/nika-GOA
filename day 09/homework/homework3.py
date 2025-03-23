# Get a number from the user
number = int(input("Enter a number: "))

# Loop to print numbers from the entered number down to 1
for i in range(number, 0, -1):
    print(i, end=" ")