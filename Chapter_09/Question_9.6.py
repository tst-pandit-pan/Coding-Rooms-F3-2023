s = "Stud"
oldstr = s            # backup the original sentence for printing later
for i in range(3):    # add single character input by users for 3 times
    s = s + input()   # input 3 characters, "e", "n", "t" one by one
    print("When i =", i , "s =" , s)
print("The original string is", oldstr)
print("The new string is " + s)
