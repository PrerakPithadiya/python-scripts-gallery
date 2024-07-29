# Step 1: Create a tuple with different data types
my_tuple = (1, "hello", 3.14, True)

# Step 2: Print tuple items
print("Original tuple:", my_tuple)

# Step 3: Convert tuple into a list
my_list = list(my_tuple)
print("Converted to list:", my_list)

# Step 4: Remove data items from the list
# Let's remove the first two two items ("1") and ("hello")
my_list.remove("hello")
my_list.remove(True)
print("List after removing items:", my_list)

# Step 5: Convert list back into a tuple
new_tuple = tuple(my_list)

# Step 6: Print the final tuple items
print("Final tuple:", new_tuple)
