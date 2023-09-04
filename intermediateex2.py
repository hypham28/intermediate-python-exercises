def combine_dicts(dict1, dict2):
    result_dict = {}
    
    # Iterate through the keys in dict1
    for key, value in dict1.items():
        if key in dict2:
            # If the key exists in both dicts, sum the values
            result_dict[key] = value + dict2[key]

    return result_dict

# Test the function with two sample dictionaries
dict1 = {"apple": 3, "banana": 2, "cherry": 1}
dict2 = {"apple": 2, "banana": 4, "date": 5}

result = combine_dicts(dict1, dict2)

# Print the result
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Combined Dictionary:", result)
