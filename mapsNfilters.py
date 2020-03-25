from functools import reduce

dataRange = range(3,10)

# Map
print('Scaling by 2', list(map(lambda x: x*2, dataRange)))

# Filter
print('Odd number:', list(filter(lambda x: x%2!=0, dataRange)))

# Reduce
def reduceData (previousResult:int,data:int):
    print(previousResult,data)
    return previousResult+data
print('Sum of numbers:', reduce(reduceData, dataRange))