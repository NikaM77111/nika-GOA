# Hardcoded secret number
secret_number = 42

# Start the guessing game
print("Guess the number between 1 and 100!")

# Loop until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number!")
        break  # Exit the loop when the guess is correct