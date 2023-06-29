# Break and continue
students = ["ram", "shyam", "kishan", "radha","radika"]
for student in students:
    if student == "radha":
        break
    print(student)


# continue
for student in students:
    if student == "kishan":
        continue
    print(student)


a = ("hello", "world")
print(type(a))
print(a.count('world')) 
# tuple is immutable 


# set   the default
b = {"hello": "world"}
print(type(b))
# b.get('Gavan')
# print(b)

b["hello"] = "Gavan kumar"
print(b)

c = {22,33,44,55,22,33,44,55,22,33,44,55,22}
# print(c[0]) we cant use index method  here instead of index method we use loop 
for i in c :
    print(i)

c.add(1000)
print(c)
c.discard(33)
print(c)
c.remove(1000)
print(c)
c.pop()
print(c)


y = {22,33,44,55}
x = {22,33,44,55, 11, 23}
union = y.union(x)
print(union)

# dictionary in python
a = {"name": "roshan", "class":8, 
     "age":13}
    
print(a["name"])
print(a.values())
print(a.keys())
a["age"] = 29
print(a["age"])



