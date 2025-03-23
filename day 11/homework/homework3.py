# Hardcoded username and password
correct_username = "user123"
correct_password = "password456"

print("Welcome to the system!")

# Loop until the user enters correct username and password
while True:
    # Get username and password input from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password are correct
    if username == correct_username and password == correct_password:
        print("Login successful! Welcome!")
        break  # Exit the loop when login is successful
    else:
        print("Incorrect username or password. Try again.")