# Create a list
list1 = [1, 2, 3]

# Create an alias for the list
list2 = list1

# Compare to safe copy
list3 = list1[:]

# Modify the original list
list1.append(4)

# Print both lists
print("list 1:", list1)
print("list 2:", list2)
print("list 3:", list3)