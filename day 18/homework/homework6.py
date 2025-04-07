fruits = ["apple", "banana", "cherry", "orange", "grape"]
print("Current list of fruits:", fruits)

to_remove = int(input("Enter the index of the fruit to remove: "))

if to_remove >= 0 and to_remove < len(fruits):
    removed_fruit = fruits.pop(to_remove)
    print(f"{removed_fruit} has been removed.")
else:
    print("Invalid index. No fruit removed.")

print("Updated list:", fruits)