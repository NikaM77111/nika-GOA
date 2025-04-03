def positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

# ტესტირება
numbers_list = [1, -2, 3, -4, 5, -6]
positive_numbers = positive_numbers(numbers_list)
print(positive_numbers) 