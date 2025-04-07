# len() copy of function
def my_len(collection):
    count = 0
    for item in collection:
        count += 1
    return count

# max() copy of function
def my_max(collection):
    max_value = collection[0]
    for item in collection:
        if item > max_value:
            max_value = item
    return max_value

# min() copy of function
def my_min(collection):
    min_value = collection[0]
    for item in collection:
        if item < min_value:
            min_value = item
    return min_value