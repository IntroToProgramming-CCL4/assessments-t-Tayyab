# This loop continuously asks the user for their age and calculates movie ticket prices.

while True:
    # Get the user's age
    age = int(input("Please enter your age: "))
    
    # Check for invalid age (less than or equal to 0)
    if age <= 0:
        print("Invalid age. Please enter a valid age.")
    
    # Check for age less than 3
    elif age < 3:
        print("Your movie ticket is free.")
    
    # Check for age between 3 and 12 
    elif age >= 3 and age <= 12:
        print("Your movie ticket costs $10.")
    
    # All other cases (age greater than 12)
    else:
        print("Your movie ticket costs $15.")
    
    # Ask the user if they want to continue or quit
    end = input("Type 'quit' to exit or 'continue' to buy more tickets: ")
    
    # Exit the loop if the user enters 'quit'
    if end == 'quit':
        break
