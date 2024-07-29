# Create two different sets with the data
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print set items
print("Set 1:", set1)
print("Set 2:", set2)

# Add items to a set
set1.add(6)
print("Set 1 after adding 6:", set1)

# Remove items from a set
set2.remove(8)
print("Set 2 after removing 8:", set2)

# Perform union operation
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

# Perform intersection operation
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# Perform difference operation
difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2 (Set 1 - Set 2):", difference_set)

# Perform symmetric difference operation
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of Set 1 and Set 2:", symmetric_difference_set)

# Check if one set is a subset of another
is_subset = set1.issubset(set2)
print("Is Set 1 a subset of Set 2?:", is_subset)

is_subset = set2.issubset(set1)
print("Is Set 2 a subset of Set 1?:", is_subset)
