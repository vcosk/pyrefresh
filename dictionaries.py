dic1 = {
    'dad' : 'Vikk',
    'daughter'  :   'Impu'
}
print(dic1)

dic2 = dict([
    ('dad', 'vikk'),
    ('daughter', 'impu')
])
print(dic2)

print(len(dic1))
print(dic1['dad'])

dic1['mom'] = 'shai'

print(dic1.items())
print(list(dic1.items()))
print(list(dic1.keys()))
print(list(dic1.values()))

for x,y in dic1.items():
    print(x,y,sep=': ')

for f in dic1:
    print(f, dic1[f])

del dic2['dad']
print(dic2)
print(dic2.pop('daughter'), dic2)
print('mom' in dic1)


# Formating dictionary entries
d1 = {'name' : 'bread', 'price' : 0.2356}
print('%(name)s costs %(price).2f'%d1)


# Sorting dictionaries
scores = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
print(scores, sorted_scores)