# a list of people that are invited to dinner
guests =["shahab","asad","moshin"]

# using for loop a message will be printed to each guset of invitaion
for guest in guests:
    print ("\nYou are invited to dinner", guest+'!')  #the invitation of dinner
    
# guest who cant make it to the dinner
print("\n" + guests[0],"will not be able to attend the dinner")

guests.remove("shahab")
guests.insert(0,"sudais")

#using for loop for invitation of modified guest list
for guest in guests:
    print ("\nYou are invited to dinner", guest+'!') #the invitation of dinner

# printing message that only 2 guests will be invited to dinner    
print ("\ni just found out that my dinner table wont't arrive on time so i can only invite two people for dinner ")

# using pop() and while loop to remove guests until two remains
while len(guests)>2:
    person_removed= guests.pop()
    print ("\ni am sorry", person_removed,"i can't invite you to dinner") 
    
# using for loop a message will be printed to each guset of invitaion
for guest in guests:
    print ("\nYou are invited to dinner", guest+'!')
    
# Using del to remove the last two names from your list, so you have an empty list.
del guests[:]

# Print the empty list to confirm
print("\nEmpty list:", guests)
    