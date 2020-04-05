# Tuples are immutables
t1 = (1, 'Dad', 'Vikk')
t2 = (2, 'Daughter', 'Impu')

print('Length', len(t1))
print('Index', t2[0])
print('Range', t1[0:2])
print('Indexing from end', t2[-1])
print('Every other', t2[0:-1:2])
print('Reversing a tuple', t2[::-1])



points = [(0,0), (0,1), (1,0), (2,3)]
print((0,0) in points)
points = {(0,0), (0,1), (1,0), (2,3)}
print((0,0) in points)
print((0,1) in points)
print((1,1) in points)
points.add((1,1))
points.add((1,0))
print(points)

# named tuples
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt1 = Point(1,2)
pt2 = Point(5,9)
pt3 = Point._make([5,9])
pt4 = Point(*[5,9])
print(pt1, pt2, pt3, pt1.__class__)

Car = namedtuple('Car','Price Mileage Colour Class')
c1 = Car(Class=1,Colour=2,Price=3,Mileage=4)
print(c1)