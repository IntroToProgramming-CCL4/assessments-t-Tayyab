# Import the datetime module, which provides classes for working with dates and times in Python.
import datetime

# Use the datetime.datetime.now() method to obtain the current date and time.
now = datetime.datetime.now()

# Print a message indicating that the following output represents the current date and time.
print("current date and time : ")

# Use the strftime method to format and print the current date and time.
print(now.strftime("%Y-%m-%d %H:%M:%S"))
