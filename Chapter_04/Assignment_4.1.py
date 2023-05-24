# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [     ]

# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# You can click "RESET" on the top right hand corner if necessary.

originalPrice = 21                                  # Fill in a number
discount = 0.6                                      # Fill in a number
sellingPrice = originalPrice * discount             # originalPrice multiplied by discount
shippingCost = 0.75                                 # Fill in an expression to calculate

print("Please input the number of copies:")
n = int(input())


totalCost = n * (sellingPrice + 0.75)               # Fill in an expression to calculate using the sellingPrice and shippingCost


print("The total cost for " + str(n) + " copies is $" + str(totalCost) + ".")                                                  # Fill in the output statement with string concatenation 