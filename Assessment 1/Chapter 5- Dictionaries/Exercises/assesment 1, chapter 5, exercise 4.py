# Define a dictionary with major rivers and the countries they flow through
major_rivers={'nile':'egypt','Amazon River':'brazil colombia peru','indus':'china india pakistan'}

# Loop through the dictionary and print information about each river and the countries they flow through
for key,value in major_rivers.items():
    print("The", key ,"play a vital role in the geographical and ecological landscapes of",value+".\n")

# Print a section header   
print("\n Famous rivers")

# using for loop through the keys of the dictionary and print the names of the rivers
for key in major_rivers.keys():
    print("\n",key)
    
# Print another section header
print("\n counties they flow through:")

# usinf for loop through the values of the dictionary and print the countries each river flows through
for value in major_rivers.values():
    print("\n",value)