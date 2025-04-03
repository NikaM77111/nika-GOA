def negative_numbers(numbers):
    negative_numbers = []
    for num in numbers:
        if num < 0:
            negative_numbers.append(num)
    return negative_numbers

# Test the function
numbers_list = [1, -2, 3, -4, 5, -6]
negative_numbers = negative_numbers(numbers_list)
print(negative_numbers)  