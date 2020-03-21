s1 = set(['Impu', 'Vikk', 'Shai'])
s2 = {'Vikk', 'Kitty', 'Nali'}

print(s1, s2)

print('Length', len(s2))

s3 = s1 | s2
print(s3)

s3.add('V*')
print(s3)

s3 |= s1

print('Random', s3.pop())
print('Indersection', s3.intersection(s1))

print('Symmetric Difference', s2.symmetric_difference(s1))

print('Difference', s1.difference(s2))

s3.discard('Vikk')
print(s3)

s3.clear()
print(s3)

# s4 is immutable
s4 = frozenset(s1)