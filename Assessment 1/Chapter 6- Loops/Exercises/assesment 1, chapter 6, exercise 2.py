# Initialize a variable to keep track of the number of tickets bought
ticket_count = 0

# Start an infinite loop to repeatedly ask for user input
while True:
    # Ask the user to enter their age or type 'quit' to exit
    age = input("Please enter your age (or type 'quit' to exit): ")

    # Check if the user entered 'quit'
    if age == 'quit':
        # Ask the user if they want to buy another ticket
        buy_again = input("You entered 'quit'. Do you want to buy another ticket? (Type 'yes' or 'no'): ")

        # Check the user's response
        if buy_again == 'no':
            # Print the total number of tickets bought and exit the loop
            print("You have bought", ticket_count, "tickets.")
            break
        elif buy_again == 'yes':
            # Continue the loop to ask for age again if the user enters 'yes'
            continue
        else:
            # Print an error message for invalid input and continue the loop
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

    # Convert the user's input to an integer
    age = int(age)

    # Determine the cost of the movie ticket based on the user's age
    if age < 3:
        print("Your movie ticket is free.")
    elif age >= 3 and age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")

    # Increment the ticket count after purchasing a ticket
    ticket_count += 1
