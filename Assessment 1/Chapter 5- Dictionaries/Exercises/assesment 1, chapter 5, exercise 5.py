# Create dictionaries for different pets
Pet1 = {'kind': 'Dog', 'owner': 'asad'}
Pet2 = {'kind': 'Cat', 'owner': 'shahab'}
Pet3 = {'kind': 'Pigeon', 'owner': 'mohsin'}

# Store the pet dictionaries in a list
Pets = [Pet1, Pet2, Pet3]

# Using for loop to print information about each pet
for Pet in Pets:
    print("Kind of animal:",Pet['kind'])
    print("Owner's name:",Pet['owner'],"\n")
   