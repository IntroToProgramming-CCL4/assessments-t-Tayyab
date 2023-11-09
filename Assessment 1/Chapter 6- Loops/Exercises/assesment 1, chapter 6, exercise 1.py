# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Use a while loop to repeatedly prompt the user for pizza toppings
while True:
    # Prompt the user to enter a pizza topping
    topping = input("Enter a pizza topping (or 'quit' to finish):")
    
    # Check if the user entered 'quit' to exit the loop
    if topping == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    # Print a message indicating the chosen topping
    print("You'll add", topping, "to your pizza.")
    
    # Add the chosen topping to the list
    pizza_toppings.append(topping)

# Print the final list of pizza toppings
if pizza_toppings:
    print("Your pizza will have the following toppings:")
    for topping in pizza_toppings:
        print("- " + topping)
else:
    # If no toppings were selected, indicate that the user didn't select any
    print("You didn't select any pizza toppings.")
