print("Please input an integer:")
n = int(input())

for i in range(1 , n+1):
    for j in range(i):
        print("*" , end="")     # end="" means that no line break after printing each asterisk, i.e. *
    print()                  # insert a line break