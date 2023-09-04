def get_valid_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Initialize a variable to store the sum
total_sum = 0

# Get 5 valid integer inputs from the user
for i in range(5):
    user_input = get_valid_integer_input(f"Enter integer {i + 1}: ")
    total_sum += user_input

# Print the resulting sum
print("The sum of the entered integers is:", total_sum)
