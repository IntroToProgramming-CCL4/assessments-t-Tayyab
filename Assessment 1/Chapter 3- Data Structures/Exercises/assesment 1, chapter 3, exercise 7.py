# List of places to visit
Places_to_visit = ["Istanbul", "Paris", "Switzerland", "Germany", "Canada"]

# the list in its original order
print("Original order: ", Places_to_visit)

# the list in alphabetical order using sorted()
sorted_list = sorted(Places_to_visit)
print("Alphabetical order: ", sorted_list)

# the list in reverse alphabetical order using sorted()
reverse_sorted_list = sorted(Places_to_visit, reverse=True)
print("Reverse alphabetical order: ", reverse_sorted_list)

# Reversing the original list
Places_to_visit.reverse()
print("Reversed order:", Places_to_visit)

# Reversing the list back to the original order
Places_to_visit.reverse()
print("Reversed order again:", Places_to_visit)

# Sorting the list in alphabetical order
sorted_list = sorted(Places_to_visit)
print("Alphabetical order: ", sorted_list)

# Sorting the list in reverse alphabetical order
reverse_sorted_list = sorted(Places_to_visit, reverse=True)
print("Reverse alphabetical order: ", reverse_sorted_list)
