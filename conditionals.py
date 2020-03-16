import sys
import math
import random

# < > <= >= == !=
age = 23
if age > 21:
    print("You can drive a tractor")
elif age > 16:
    print("You can drive a car")
else:
    print("You shouldn't drive")

# and or not
age = 1 # int(input())
if age < 5:
    print('Stay home')
elif (age >=5 and age <=6):
    print('Go to kinder garden')
elif age >=6 and (age <= 17):
    print('Grade %d'%(age - 5))
else:
    print('Collage')

# Ternary condition_true_value if condition else condition_false_value
a = 9 if age > 5 else 10
print(a)

def d(x):
    print(x)
    x

a = d(9) if age > 5 else 10