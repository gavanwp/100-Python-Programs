first = int(input("Enter the first value"))
operator = input("Select operator +,-,*,/,%")
second = int(input("Enter the second value"))

if operator == '+' :
    print(first + second)
elif operator == '-' :
    print(first - second)
elif operator == '/':
    print(first / second)
elif operator == '*' :
    print(first * second)
elif operator == '%' :
    print(first % second)
else :
    print("Enter your valid operator")

print("Thanks for using this calculator")


 
# While loop in python 

a = 0 
while a < 40 :
    print(a * "*")
    a += 1

a = 50
while a > 0 :
    print(a * "*")
    a -= 1

# For loop in python
for i in range(20):
    print(i + 1 )

# List in python 
marks = [22,33,44,55,66]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(len(marks))
print(marks[0:3])
print(marks[0:2])
print(marks[1:3])
print(marks[1:2])
print(marks[2:3])

for i in  marks:
    print(i)

marks.append(999)
print(marks)

marks.insert(1,100)
print(marks)


a = 0 
while a < len(marks):
    print(marks[a])
    a += 1

print(22 in marks)

marks.clear()
print(marks)


