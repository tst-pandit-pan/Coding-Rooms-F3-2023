sentence = " Write down the output of the code."
count_o = 0
for i in sentence:
    if i == "o":
        count_o += 1    # same as count_o = count_o + 1
        print(i)
print("There are " + str(count_o) + " \"o\"s in the string")
