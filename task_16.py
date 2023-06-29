'''To write a python program to Find the Factorial of a Number '''
'''Using for loop'''
factorail = int(input("Enter a number here "))
a = 1
if factorail < 0:
    print("Factorial is not exist ")
elif factorail == 0:
    print('Factorial of 0 is 1')
elif factorail > 0:
    for i in range(1,factorail+1):
        a = a*i
print('The factorial of the given number is ',a)

'''Using recursion method'''
a = int(input("Enter the number here "))
def fact(a):
    if a == 0:
      return  1
    else:
        return ((a)*fact(a-1))
result = fact(a)
print(result)