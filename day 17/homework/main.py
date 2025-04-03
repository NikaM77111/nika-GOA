#
def powTwo(numbers):
    result = []

    for num in numbers:
        result.append(num * num)
    
    return result


print(powTwo([1,2,3]))
#
def filter(word):
    vowels = "aeiou"
    result = ""

    for char in word:
        if char in vowels:
            result += char
    
    return result


filter("Luka")
#
def filter(word):
    vowels = "aeiou"
    result = ""

    for char in word:
        if char in vowels:
            result += char
    
    return result


filter("Luka")
#7
def filter_positive(numbers):
    negative_numbers = []

    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
    
    return negative_numbers

filter_positive([1,2,3,-5,-8,-10,7,11])
#8
def math_operation(number):
    return (number ** 2) * 10