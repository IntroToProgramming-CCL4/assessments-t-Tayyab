# Define the function make_shirt with size and message parameters
def make_shirt(size = 'Large', message = "I love python"):
    # Print a sentence summarizing the size and message on the shirt
    print("The shirt size is: ", size,"and message is: ", message)

# Call the function to display the message
make_shirt()

# Call the function to make a medium shirt with the default message
make_shirt(size='Medium')

# Call the function to make a shirt of any size with a different message
make_shirt(size='Small', message='Be yourself—everyone else is taken.')
