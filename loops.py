w1 = 2

while w1 > 0:
    print(w1)
    w1 -= 1

l = ['A','B','C','D','E','F']
while len(l):
    print("List content %s"%l.pop(0))

for x in range(0, 10):
    print(x, ' ', end='')
print()

l = ['A','B','C','D','E','F']
for x in l:
    print('List content %s'%x)

for x in range(0,10,2):
    print(x, ' ', end='')
print()