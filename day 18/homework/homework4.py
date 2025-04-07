numbers = [1, 2, 3, 2, 4, 2]
chosen_number = int(input("Please enter a number from the list: 1, 2, 3, 4: "))
found = False
count = 0

for number in numbers:
    if number == chosen_number:
        count += 1
        found = True

if found:
    print(f"The number {chosen_number} appears {count} times.")
else:
    print("The number you entered is not in the list.")