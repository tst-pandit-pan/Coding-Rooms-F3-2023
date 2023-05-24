# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [     ]

# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# You can click "RESET" on the top right hand corner if necessary.

import random

print("Please input 1, 2 or 3 for paper, scissor and rock:")
player = int(input())
if ((player == 1)or(player == 2)or(player == 3)):
    comp = random.randint(1,3)
else:
    comp = 4

if (player == 1):
    print("You picked paper", end ="")
elif (player == 2):
    print("You picked scissor", end ="")
elif (player == 3):
    print("You picked rock", end ="")
else:
    print("You are not entering the correct number!!!")

if (comp == 1):
    print(" and the computer picked paper.")
elif (comp == 2):
    print(" and the computer picked scissor.")
elif (comp == 3):
    print(" and the computer picked rock.")
else:
    print()

if ((player == 1) and (comp == 2)) or ((player == 2) and (comp == 3)) or ((player == 3) and (comp == 1)):
    print("You lose!")
elif ((player == 2) and (comp == 1)) or ((player == 3) and (comp == 2)) or ((player == 1) and (comp == 3)):
    print("You win!")
elif ((player == 1) and (comp == 1)) or ((player == 2) and (comp == 2)) or ((player == 3) and (comp == 3)):
    print("Draw!")