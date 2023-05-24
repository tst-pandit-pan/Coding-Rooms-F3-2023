# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [     ]


import random                                   # to import the built-in module / library

print("Please input the first integer:")
x = int(input() )                           # accept the first integer input from user
print("Please input the second integer:")
y = int(input() )                               # accept the second integer input from user


# for simplicity, you can assume x is always smaller than y
n = random.randint(x,y)                   # assign a random integer between x and y to n 

print("The random number generated is " + str(n) + "." )
