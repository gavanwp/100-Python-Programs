'''to write a Python Program to Find Armstrong Number in an Interval '''
lower = int(input("Enter lower number here "))
upper = int(input("Enter upper number here "))

for num in range(lower, upper+1):
    order = len(str(num))
    sum = 0 
    temp = num
    while temp > 0:
        digit = temp%10
        cube = digit**order
        sum+=cube
        temp//=10
    if num == sum:
        print(sum)
    