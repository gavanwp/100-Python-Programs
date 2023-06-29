


a = "hello world"
b = "This is my python code"
print(a+ " " + b)
print(a+ " " + "hello dear")


# Arithmetic operators

# Addition a + b
print("Addition", 20+20)
# Substraction a - b
print("Substraction", 50-20)
# Multiplication a * b 
print("Multiplication", 10*5)
# Division a /b
print("Division", 30/7)
# Modulus a % b
print("Modulus", 30%7)
# Exponents x ** y
print("Exponents", 5**5) # 5*5*5*5*5
# Floor division
print("Floor division", 30//7) 



# Assigment Operator in python 
x = 30
print(x)
x+=5
print(x)

x-=10
print(x)


# Comparison Operators

# 1 Equal ==
# 2  Not Equal !=
# 3 Greater than > 
# 4 Less than < 
# 5 Greater than or equal to >=
# Less than or equal to <=

a = 90
b = 50
print("a is greater than b", a > b)
print("a is greator than or equal to b" , a>=b)
print("b is less than a " , b<a)
print("b is less than or equal to a" , a<=b)
print("a is not equal to b", a!=b)
print("a is equal to b " , a==b)



# Logical Operators 
x = 20 
y = 20

print(x == 20 and x <= y)
print(x != y or x ==20)
print(not x > y)





# Membership Operators
a = [33,44,66,33,43]

if 33 in a:
    print("Yes")
else:
    print("No")



class info:
    def __init__(self, name, age , salary, job):
        self.name = name
        self.age = age
        self.salary = salary
        self.job = job
    def showme(self):
        print(f"Name : {self.name} \n Age : {self.age} \n Salary : {self.salary} \n Job : {self.job}")
class newdata(info):
    def add(self):
        print("hello world")



em1 = info("Roshan kumar", 15, 20000, "Teacher")
em1.showme()
em2 = newdata("Naresh kumar", 20, 30000 , "Dictor")
em2.add()

        