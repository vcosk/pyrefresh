from functools import reduce

dataRange = range(3,10)

# Map
print('Scaling by 2', list(map(lambda x: x*2, dataRange)))

# Filter
print('Odd number:', list(filter(lambda x: x%2!=0, dataRange)))

# Reduce
print('Sum of numbers:', reduce(lambda x,y: x+y, dataRange))