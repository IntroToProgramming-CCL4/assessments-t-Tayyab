#total budget the girl have
total_budget = 50

# the price of  1 USB stick
price = 6  

# it calculates of possible USB that can be bought 
USB_bought = (total_budget // price)  

# it calculates the remaining money
change = total_budget - (USB_bought * price)  

# it prints how many USB are bought
print("You can buy", USB_bought, "USB sticks for", total_budget, "pounds")

# it prints how many pounds are remaining
print("Change:", change, "pounds")