# Print a message prompting the user to enter the radius to find the area of a circle.
print("To find the area of a circle")

# Use the float() function to convert the user input (radius) to a floating-point number.
radius = float(input("Enter radius: "))

# Assign the value of pi to the variable pie.
pie = 3.14

# Calculate the area of the circle using the formula.
area = pie * radius**2

# Print a message indicating the calculated area of the circle.
print("The area is ", area)
