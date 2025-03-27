user_info = []

# Collecting user information
name = input("Enter your first name: ")
user_info.append(name)

surname = input("Enter your last name: ")
user_info.append(surname)

age = input("Enter your age: ")
user_info.append(age)

birthdate = input("Enter your birthdate (dd/mm/yyyy): ")
user_info.append(birthdate)

height = input("Enter your height (cm): ")
user_info.append(height)

email = input("Enter your email: ")
user_info.append(email)

phone_number = input("Enter your phone number: ")
user_info.append(phone_number)

address = input("Enter your address: ")
user_info.append(address)

# Output the collected information
print("\nUser Information:")
for info in user_info:
    print(info)