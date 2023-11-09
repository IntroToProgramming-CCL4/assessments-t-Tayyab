# Define a list of sandwich orders
sandwich_orders = ["tikka sandwich", "chicken sandwich", "beef sandwich", "mutton sandwich"]

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Process each sandwich order until the list is empty
while sandwich_orders:
    # Pop an order from the end of the sandwich_orders list
    order = sandwich_orders.pop()
    
    # Print a message indicating that the sandwich is made
    print("I made your", order + ".")
    
    # Add the completed order to the finished_sandwiches list
    finished_sandwiches.append(order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

