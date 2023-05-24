print("Please input an integer:")
n = int(input()) 									
for i in range(1 , n+1 ):
    for j in range(n-i):      # output a series of spaces
        print(" ", end="")
    for j in range(i):        # output a series of asterisks
        print("*", end="")
    print()					  # insert a line break
