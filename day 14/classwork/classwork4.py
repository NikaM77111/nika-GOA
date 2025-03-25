def find_unique_element(lst):
    # Sort the list to group the same elements together
    lst.sort()

    # Look for the unique element in the middle
    for i in range(1, len(lst) - 1):  
        if lst[i] != lst[i - 1] and lst[i] != lst[i + 1]:
            return lst[i] 

    # Check if the first or last element is unique
    if lst[0] != lst[1]:
        return lst[0]
    if lst[-1] != lst[-2]:
        return lst[-1]

# Example list 
lst = [2, 3, 3, 3, 5]

#result
unique_element = find_unique_element(lst)
print(f"The unique element is: {unique_element}")