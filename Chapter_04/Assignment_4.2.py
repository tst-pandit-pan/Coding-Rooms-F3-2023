# Input your name here (e.g. Chan Tai Man): [           ]

# input your class and class number here (e.g. 3F39): [         ]

# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# PLEASE DO NOT DELETE ANY PART OF THE GIVEN CODE!!!!!!!
# You can click "RESET" on the top right hand corner if necessary.

message1 = str(input("Please input the first message:"))
print()
message2 = str(input("Please input the second message:"))
print()

print("The values of message1 and message2 before swapping are \"" + message1 + "\" and \"" + message2 + "\".")    # Do not make changes to this line!!!!!

# Write three statements in lines 18 to 20 below to perform swapping, i.e. interchange the content of message 1 with that of message 2!!!!!
message_tmp = message1
message1 = message2
message2 = message_tmp
print("The values of message1 and message2 after swapping are \"" + message1 + "\" and \"" + message2 + "\".")     # Do not make changes to this line!!!!!