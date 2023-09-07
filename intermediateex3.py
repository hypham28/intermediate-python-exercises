def count_lowercase_letters(input_string):
    # start an empty dictionary to store letter counts
    letter_counts = {}

    # Remove spaces and convert the input string to lowercase
    cleaned_string = input_string.replace(" ", "").lower()

    # go through cleaned string
    for char in cleaned_string:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts

# Get input from the user
user_input = input("Enter a string: ")

# Call function
result_dict = count_lowercase_letters(user_input)

# Print the resulting dictionary
print("Letter counts (excluding spaces):")
print(result_dict)
