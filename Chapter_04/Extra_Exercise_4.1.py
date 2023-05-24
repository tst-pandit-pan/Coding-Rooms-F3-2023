N = int(input("Enter the number of seconds: ")) # input() is a function to read the user input, you may ignore this statement at this moment

a = (N // (60 * 60)) # modify it with a mathematical expression
b = (N - a * (60 * 60)) // 60
c = (N - a * (60 * 60) - b * 60) # modify it with a mathematical expression

print(N, "seconds equals to", a, "hours", b, "minutes and", c, "seconds.")