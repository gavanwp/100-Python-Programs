'''To write a program if the NUmber is Armstrong or not '''
# 153 = (1*1*1)+(5*5*5) + (3*3*3) = 143 mean it is a armstrong number 
# 53 = (5*5)+(3*3) = 34 mean it is not a armstrong number 
num = int(input("Enter a number here "))
index = str(num)
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    cube = digit**len(index)
    # sum = sum + cube
    sum+=cube
    temp//= 10
if sum == num:
    print("it is an armstrong number")
else:
    print("it not an armstrong number")
