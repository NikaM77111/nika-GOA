# Get input from the user
number = int(input("Please enter a number: "))

# Assume the number is prime
is_prime = True  

# Numbers less than or equal to 1 are not prime
if number <= 1:
    is_prime = False
else:
    # Check if the number is divisible by any number from 2 to itself - 1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

# Output the result
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")