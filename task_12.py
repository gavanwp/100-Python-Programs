'''To write a program to check if number is a prime numer is not '''
num = int(input("Enter a number here !"))
if num == 1 or num < 0:
    print("it is not a prime number")
if num > 1 :
    for i in range(2,num):
        if num%i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")


    
