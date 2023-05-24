# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [     ]

import random		               	                 # to import the built-in module / library
n = random.randint(0,3)	                             # assign a random integer between 0 and 3 to n  as there are FOUR integers 
ans = (90)*n + 45                               # ?-? is the difference between any two adjacent integers while 45 is the first integer
print("The value of n is " + str(ans) + "." )
