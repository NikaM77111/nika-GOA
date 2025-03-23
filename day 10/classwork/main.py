number = float(input("Please enter a positive number: "))

#add while and number
while number <= 0:
    print("The number is not positive. Please try again.")
    number = float(input("Please enter a positive number: "))
    
print(f"You entered a positive number: {number}")