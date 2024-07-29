# Create a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Print dictionary items
print("Dictionary items:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Add a key-value pair to the dictionary
my_dict["email"] = "alice@example.com"
print("\nDictionary after adding a key-value pair:")
print(my_dict)

# Remove a key-value pair from the dictionary
del my_dict["age"]
print("\nDictionary after removing a key-value pair:")
print(my_dict)

# Check whether a key exists in the dictionary
key_to_check = "city"
if key_to_check in my_dict:
    print(f"\nThe key '{key_to_check}' exists in the dictionary.")
else:
    print(f"\nThe key '{key_to_check}' does not exist in the dictionary.")

# Iterate through the dictionary
print("\nIterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Concatenate multiple dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Using the update method to concatenate dictionaries
concatenated_dict = {}
for d in (dict1, dict2, dict3):
    concatenated_dict.update(d)

print("\nConcatenated dictionary:")
print(concatenated_dict)
