# Input string
input_string = "Hello, World!"

# Loop through the string and print characters at even indices
for i in range(len(input_string)):
    if i % 2 == 0:  # Check if the index is even
        print(input_string[i])