# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [     ]

# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE (except ????????)!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE (except ????????)!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE (except ????????)!!!!!!!
# You can click "RESET" on the top right hand corner if necessary.



print("Please input the first term:")
a = int(input())
print("Please input the last term:")
b = int(input())

print("Please input the common difference:")
d = int(input())

s = 0

for i in range(a, b+1, d):
    s = s + i

print("The sum is " + str(s) + ".")