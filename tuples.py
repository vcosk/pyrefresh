# Tuples are immutables
t1 = (1, 'Dad', 'Vikk')
t2 = (2, 'Daughter', 'Impu')

print('Length', len(t1))
print('Index', t2[0])
print('Range', t1[0:2])
print('Indexing from end', t2[-1])
print('Every other', t2[0:-1:2])
print('Reversing a tuple', t2[::-1])