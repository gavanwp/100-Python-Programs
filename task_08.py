'''Write a program to check negative number , positive number or zero'''

num = int(input("Enter a number"))
if num < 0:
    print(num, 'this number is a Negatibe number')
elif num == 0:
    print(num,'this is a Zero')
else:
    print(num,'this number is a positive number')