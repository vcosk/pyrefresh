l = ['A','B','C','D','E','F']
# Iterators
itr = iter(l)
print(next(itr))
print(next(itr))
print(next(itr))

# Range functions
for x in range(0,10):
    print(x, ' ', end='')
print()

for x in range(0,10, 3):
    print(x, ' ', end='')
print()

for x in range(10,0, -1):
    print(x, ' ', end='')
print()

# Ranges as list
print(list(range(0,10)))
print(list(range(0,10,3)))
print(list(range(10,0,-1)))