def unique_elements(input_list):
    # Create an empty list to store unique elements
    unique_list = []

    # go through the input list
    for item in input_list:
        # If the item is not in the unique list, add it
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Test 
sample_list = [3, 14, 15, 2, 3, 6, 8]
result = unique_elements(sample_list)


print("Original list:", sample_list)
print("List with unique elements:", result)
