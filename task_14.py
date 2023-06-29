''''To write a program print all prime number'''
lower = int(input("Enter lower number here "))
higher = int(input("Enere higher number here "))
prime_number = []
for num in range(lower, higher+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            prime_number.append(num)
print(prime_number)
