# assigning age to a variable Age
Age = 50

# Using if-elif-else chain to check the age and print the 
if Age > 0 and Age < 2:
    # If the age is greater than 0 and less than 2, print this
    print("The person is a baby")
    
elif Age >= 2 and Age < 4:
    # If the age is 2 or greater and less than 4, print this
    print("The person is a toddler")
    
elif Age >= 4 and Age < 13:
    # If the age is 4 or greater and less than 13, print this
    print("The person is a kid")
    
elif Age >= 13 and Age < 20:
    # If the age is 13 or greater and less than 20, print this
    print("The person is a teenager")
    
elif Age >= 20 and Age < 65:
    # If the age is 20 or greater and less than 65, print this
    print("The person is an adult")

elif Age >= 65:
    # If the age is 65 or greater, print this
    print("The person is an elder")
    
else:
    # If none of the conditions are met, print this
    print("The age you mentioned does not fit into any category")
