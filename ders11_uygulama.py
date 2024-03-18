"""
new_tuple =('izmir', 'ankara')
print(type(new_tuple))

tuple = ('izmir')
print(type(tuple))

tuple =('izmir',)
print(tuple)
"""


"""
new_tuple = (4, 8, [1, 20]) # 4 değerini 50 ye çeciri, 1 i 100 e çevir
'''
new_tuple[0] = 50
print(new_tuple)
'''

new_tuple[2][0] = 100
print(new_tuple)
# tuple ın içinde liste varsa, o elemanı değiştirebiliriz
"""

'''
cities =('istanbul', 'ankara', 'izmir')

print('izmir' in cities)
'''
"""
#new tuple daki aynı elemanları teke indiren program

new_tuple = ('5', 'izmir', 28, 'ankara', '5', 'izmir')

new_tuple2 = tuple(set(new_tuple))

print(new_tuple2)
"""


"""
# aşağıdaki kümeye ismini ekle ve listeye çevir
new_set = {'ahmet', 'mehmet', 'ayşe', 'fatma' }

new_set.add('faruk')
print(new_set)
new_list = list(new_set)
print(new_list)
"""


# aşağıdaki harfleri teke indir ve set halinde yazdır

letters = "asdfasdfasdfsdfgsdfgqefasdzxcvxbhsdfg"

new_set = {letter for letter in letters}

print(new_set)

