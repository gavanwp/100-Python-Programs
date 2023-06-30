'''Find the Largest Among Three Numbers'''

List = []
a = int(input())
b = int(input())
c = int(input())
List.append(a)
List.append(b)
List.append(c)

print(max(List))

# Using another method in pyhton
if a > b and a > c:
    print(f'Number {a} is greater ')
elif b > a and b > c:
    print(f"Number {b} is greater")
elif c > a and c > a:
    print(f"Number {c} is greater")
else:
    print("all number is equal to ")

def marks(**kwargs):
  for key , value in kwargs.items():
    print(key, value)

Student_marks = {"mohitarora":77,
                 "ryostyles":45,
                 "khadimhusen":66,
                 "Gajendrasinghyadav":76,
                 "urvashityagi":54,
                 "shashankgpt":88
                 
  
}
marks(**Student_marks)



   

