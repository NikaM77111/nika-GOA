import random

# Generate a random number
secret_number = random.randint(1, 100)

print("Guess the number between 1 and 100:")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break