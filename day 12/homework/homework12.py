# Get user's age and student status
age = int(input("Please enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == 'yes'

# Decision logic based on age and student status
if age < 18 and not is_student:
    print("You are a minor and not a student.")
else:
    print("You are either an adult or a student.")