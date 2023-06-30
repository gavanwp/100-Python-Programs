'''Write program to sum natural number'''
# first = int(input("Enter first natural number here  "))
# second = int(input("Enter secound natural number here "))
# if first < 0:
#     print("Plese Enter a natural number")

# else:
#     print(first+second)
lower = int(input("Enter  lower number here "))
upper = int(input("Enter upper number here "))
sum = 0
for num in range(lower, upper+1):
    if num < 0:
        print("it is not a natural number")
    else:
        sum+=num
print(sum)

#       Solution here 
number = int(input("Enter a number here "))
if number < 0:
    print('please enter a positive number ')
else:
    sum = 0 
    while number > 0:
        sum+=number
        number-=1
    print(sum)