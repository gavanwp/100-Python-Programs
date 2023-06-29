'''To Write a program to generate a random number'''

import random
num = random.randint(10,100)
print(num)
num1 = random.random()
final_result = round(num1*5,4)
print(final_result)

'''To Explore more about random module on Google and Youtube'''
List = ["Roshan", "Narsh", "Amit", "Ali"]
print(random.choice(List))
print(random.randrange(2,100))


# Shuffle
L = [23,34,26,33]

random.shuffle(L)
print(L)

# 
u = random.uniform(2,20)
print(u)
