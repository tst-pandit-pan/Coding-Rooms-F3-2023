import math # import a library called math, to get a more accurate value of pi

#(1) Ask the user input three values of a, b and c.
print("a: " ,end = '')
a = input()
print("b: " ,end = '')
b = input()
print("c: " ,end = '')
c = input()
#(2) Print the maximum value of the three numbers.
max_value = max(a,b,c)
print("Maximum:" , max_value)
#(3) Round off the value of pi, correct to 3 decimal places and print it out.
pi = round(math.pi, 3) #this is the value of pi in float
print("Pi:" , pi)