import random		               	                 # to import the built-in module / library

print("Please input the first number:")
x = float(input())                                               # accept the first float input from user
print("Please input the second number:")
y = float(input())                                              # accept the second float input from user

# for simplicity, you can assume x is always smaller than y
n = random.random() * (y-x) + x	                                         # assign a random integer between x and y to n 

print("The random number generated is", str(n) + "." )
