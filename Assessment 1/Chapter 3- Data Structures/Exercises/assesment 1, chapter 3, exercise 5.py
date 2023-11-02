# a list of people that are invited to dinner
guests =["shahab","asad","moshin"]

# using for loop a message will be printed to each guset of invitaion
for guest in guests:
    print ("You are invited to dinner", guest+'!') #the invitation of dinner
    
# guest who cant make it to the dinner
print(guests[0],"will not be able to attend the dinner")

guests.remove("shahab")
guests.insert(0,"sudais")

#using for loop for invitation of modified guest list
for guest in guests:
    print ("You are invited to dinner", guest+'!') #the invitation of dinner
    

