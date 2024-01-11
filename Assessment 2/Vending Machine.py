# Function to display the menu of the vending machine
def display_menu(products):
    print("\nWelcome to the Vending Machine")
    
    # Using for loop it reads each category in the products dictionary
    for category, items in products.items():
        print(f"{category}:\n")  # Print the category name
        print("Code\tProduct\t\tPrice\tQuantity")
        
        # Using for loop it reads each product in the current category
        for code, product in items.items():
            # Display product details including code, name, price, and quantity
            print(f"{code}\t{product['name']} \t${product['price']}\t{product['quantity']}")

# Function to suggest alternative items based on the user's selection
def suggest_item(products, selected_category, selected_code, balance, num_suggestions=5):
    print("\nSuggested Items:")

    # Determine the suggestion category based on the selected category
    suggestion_category = 'Snacks' if selected_category in ['Coffee', 'Drinks'] else 'Coffee'

    suggestions = []

    # Explore the products in the suggestion category to find alternatives
    for code, product in products[suggestion_category].items():
        # Check if the product is different from the selected one and still available
        if code != selected_code and product['quantity'] > 0:
            suggestions.append((code, product))

    # Display up to 'num_suggestions' alternative products
    for i in range(1, min(num_suggestions + 1, len(suggestions) + 1)):
        code, product = suggestions[i - 1]
        print(f"{i}. {code}\t{product['name']} \t${product['price']}\t{product['quantity']}")

    # Allow the user to choose from the suggestions
    if suggestions:
        while True:
            choice = input("Choose a suggestion (1-5) or enter '0' to skip: ")
            if choice.isdigit() and 0 <= int(choice) <= num_suggestions:
                if int(choice) == 0:
                    break
                selected_code = suggestions[int(choice) - 1][0]
                product = products[suggestion_category][selected_code]
                product_name = product['name']
                price = product['price']

                # Deduct the price from the balance for the selected suggestion
                if balance >= price:
                    balance -= price
                    product['quantity'] -= 1
                    print(f"\nYou chose: {selected_code} - {product_name}")
                    print(f"\nDispensing {product_name}...")
                    print(f"Remaining Balance: ${balance:.2f}")
                    print(f"Remaining {product_name} quantity: {product['quantity']}")
                else:
                    print("\nInsufficient balance. Please insert more money.")
                    balance = insert_money(balance)  # Request more money

                    # Check if the balance is now sufficient after requesting more money
                    if balance >= price:
                        balance -= price
                        product['quantity'] -= 1
                        print(f"\nAutomatically purchasing {product_name}...")
                        print(f"\nDispensing {product_name}...")
                        print(f"Remaining Balance: ${balance:.2f}")
                        print(f"Remaining {product_name} quantity: {product['quantity']}")
                    else:
                        print("\nInsufficient balance. Exiting.")
                        print("\nThank you for using the Vending Machine. Goodbye!")
                        exit()  # Exit the program if balance is still insufficient
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5 or '0' to skip.")

# Function to handle the insertion of money into the vending machine
def insert_money(balance):
    while True:
        # Prompt the user to input the amount of money
        money_input = input("\nInsert money (in dollars): ")

        # Check if the input can be converted to a positive float value
        if money_input.replace('.', '', 1).isdigit():
            money = float(money_input)

            # Check if the entered amount is positive
            if money > 0:
                balance += money
                print(f"Current Balance: ${balance:.2f}")
                break  # Exit the loop if a valid amount is entered
            elif money < 0:
                print("Invalid amount. Please insert a positive amount.")
            else:
                print("Enter the currency in digit form.")
        else:
            print("Invalid input. Please enter a numeric amount.")

    return balance

# Function to handle user decision on making another purchase or providing feedback/closing
def condition():
    while True:
        # Prompt the user to decide whether to make another purchase
        more_purchase = input("\nDo you want to make another purchase? (yes/no): ").lower()
        
        if more_purchase == 'yes':
            return 'purchase'  # User wants to make another purchase
        elif more_purchase == 'no':
            # If the user doesn't want to make another purchase, prompt for feedback or closing
            feedback_option = input("\nDo you want to give feedback or close? (feedback[f]/close[c]): ").lower()
            if feedback_option == 'f':
                return 'feedback'  # User wants to provide feedback
            elif feedback_option == 'c':
                return 'close'  # User wants to close the program
            else:
                print("\nInvalid input. Please enter 'feedback' or 'close'.")
        else:
            print("\nInvalid input. Please enter 'yes' or 'no.'")

# Function to handle the selection of a product by the user
def select_product(products, balance):
    while True:
        # Prompt the user to enter the product code
        code = input("\nEnter the product code: ").upper()

        category, product = None, None
        
        # Search for the entered product code in the product categories
        for cat, items in products.items():
            if code in items:
                category = cat
                product = items[code]
                break  # Exit the loop once the product is found

        if product:
            # Check if there is enough quantity of the product and if the balance is sufficient
            while product['quantity'] > 0 and balance < product['price']:
                print("\nInsufficient balance. Please insert more money.")
                balance = insert_money(balance)  # Ask for more money

            if product['quantity'] > 0:
                # Deduct the product price from the balance and update the product quantity
                balance -= product['price']
                product['quantity'] -= 1
                print(f"\nDispensing {product['name']}...")
                print(f"Remaining Balance: ${balance:.2f}")
                print(f"Remaining {product['name']} quantity: {product['quantity']}")
                
                # After dispensing, suggest alternative items to the user
                suggest_item(products, category, code, balance)  # Pass the balance to suggest_item
                
                # Return the selected category and product code
                return category, code  
            elif product['quantity'] == 0:
                print("\nSorry, this product is out of stock.")
            else:
                print("\nInsufficient balance. Please insert more money.")
        else:
            print("\nInvalid choice. Please enter a valid product code.")
            
# Function to simulate the operation of a vending machine
def vending_machine(products):
    display_menu(products)

    balance = 0  # Initialize balance outside the loop
    total_spent = 0  # Initialize total spent
    change = 0  # Initialize change
    suggested_items_displayed = False  # Flag to track if suggested items are already displayed

    while True:
        exit_after_feedback = False  # Initialize exit_after_feedback at the beginning of the loop

        # Ask for money only if the balance is zero and suggested items haven't been displayed yet
        if balance <= 0 and not suggested_items_displayed:
            balance = insert_money(balance)  # Only ask for money if balance is zero
            suggested_items_displayed = True  # Set the flag to True after inserting money

        # Get details of the selected product
        selected_category, selected_code = select_product(products, balance)

        if selected_category and selected_code:
            # Update total spent and deduct the price from the balance
            total_spent += products[selected_category][selected_code]['price']
            balance -= products[selected_category][selected_code]['price']

            # Display suggested items only once after the initial purchase
            if not suggested_items_displayed:
                # Pass the balance to suggest_item to display suggestions
                suggest_item(products, selected_category, selected_code, balance)
                suggested_items_displayed = True  # Set the flag to True

            more_purchase = condition()

            if more_purchase == 'feedback':
                # Provide feedback option directly without prompting for a product code
                print("\nProvide Feedback:")
                # Prompt user for feedback after each purchase
                rating = int(input("Enter your rating (1-5): "))
                comment = input("Leave a comment: ")
                # Append feedback to the selected product's reviews
                products[selected_category][selected_code]['reviews'].append({'rating': rating, 'comment': comment})
                print("Thank you for your feedback!")
                exit_after_feedback = True  # Set the flag to True to exit after feedback

            if more_purchase == 'close' or exit_after_feedback:
                # Calculate change here, after the user decides not to make another purchase or after feedback
                change = balance
                print(f"Total spent: ${total_spent:.2f}")
                if change < 0:
                    change = 0
                print(f"Change: ${change:.2f}")
                print("Thank you for using the Vending Machine. Goodbye!")
                break  # Exit the loop if the user chooses to close the program or after feedback


# Dictionary representing the products available in the vending machine
products = {
    'Drinks': {
        'A1': {'name': 'Coca Cola', 'price': 2.00, 'quantity': 10, 'reviews': []},
        'A2': {'name': 'Mountain Dew', 'price': 2.00, 'quantity': 8, 'reviews': []},
        'A3': {'name': 'Fanta   ', 'price': 2.00, 'quantity': 15, 'reviews': []},
        'A4': {'name': 'Water   ', 'price': 2.00, 'quantity': 8, 'reviews': []},
        'A5': {'name': 'Choclate Milk', 'price': 2.00, 'quantity': 15, 'reviews': []}
    },
    'Coffee': {
        'B1': {'name': 'Black Coffee', 'price': 5.00, 'quantity': 12, 'reviews': []},
        'B2': {'name': 'Espreso Coffee', 'price': 5.00, 'quantity': 10, 'reviews': []},
        'B3': {'name': 'Cappuccino', 'price': 4.00, 'quantity': 20, 'reviews': []},
        'B4': {'name': 'Latte   ', 'price': 4.00, 'quantity': 10, 'reviews': []},
        'B5': {'name': 'Mocha   ', 'price': 3.00, 'quantity': 20, 'reviews': []}
    },
    'Snacks': {
        'C1': {'name': 'Lays Chips', 'price': 1.00, 'quantity': 12, 'reviews': []},
        'C2': {'name': 'Cookie  ', 'price': 2.25, 'quantity': 10, 'reviews': []},
        'C3': {'name': 'Donut   ', 'price': 1.75, 'quantity': 20, 'reviews': []},
        'C4': {'name': 'Coffee Cake', 'price': 1.25, 'quantity': 10, 'reviews': []},
        'C5': {'name': 'Croissant', 'price': 2.75, 'quantity': 20, 'reviews': []}
    }
}

# Call the vending machine function with the defined products
vending_machine(products)