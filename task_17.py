'''Write a python program to print a multiplication Table '''
num = int(input("Enter a Table number here " ))

for i in range(1,11):
    print(f"{i}*{num} = {i*num}")


# using while loop

i = 1
while i <= 10:
    print(f'{i}*{num} = {i*num}')
    i +=1