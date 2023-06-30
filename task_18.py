'''Write a program to wrint Fibonacci  Fibonacci Sequence'''
# a = 0
# # b = 1
# c = a + b = 1
# a = b = 1
# b = c = 1
# c = a + b
# a = b 
# b = c 
# c = a+b
#  
a = 0
b = 1
num = int(input("Enter a number to optain fabonacci Sequence here "))
LIst = []
if num == 1:
    print(a)
else:
    #print(a)
    LIst.append(a)
    LIst.append(b)
    #print(b)
    for i in range(2,num):
        c = a + b
        a = b
        b = c
        LIst.append(c)
        #print(c)

print(LIst)