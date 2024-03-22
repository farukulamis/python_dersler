# dictionaries
# key - value lardan oluşur..

"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
print(type(monster_1))
print(monster_1)
print(monster_1['name'])
"""
# yeni eleman ekleme
"""
monster_1['position']= 100
print(monster_1)

print(monster_1['position'])
"""

"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
print(monster_1.get('name'))
print(monster_1['name'])
# yukarıdaki iki şekilde name key değerini gördük. aralarındaki fark birinde aşağıdaki gibidir
print(monster_1.get('boy')) # burada none çıktısı verir
print(monster_1['boy']) # burada hata verir
"""

"""
#yeni bir değer değilde varolan değerleri değiştirmek istersek;
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
monster_1['position']= 100
print(monster_1)

monster_1.update({'name': 'GURU', 'power': 20 })
print(monster_1)

# update fonksiyonu varolanları değiştirir olmayanları olduğu gibi bırakır. olmayan bir şeyi yazarsak
# mesela age: 33 dersek, onu da ekler.

monster_1.update({'age': 33})
print(monster_1)
"""

#her key-value çiftini nasıl silebiliriz
"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
del monster_1['power']
print(monster_1)
"""

# pop metoduyla da silebiliriz
"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
monster_1.pop('power')
print(monster_1)
"""
# len fonksiyonu, key değerlerini yazdırma
"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}
print(len(monster_1))

print(monster_1.keys())

print(monster_1.values())

print(monster_1.items())
"""


"""
monster_1= {'name': 'guru','power': 10, 'color' :'red'}

for key in monster_1:
    print(key)

for key in monster_1.keys():
    print(key)

for value in monster_1.values():
    print(value)
"""

## dictionary leri herhangi bir liste içerisinde de kullanabiliriz



my_friends = [
    {'name': 'deniz', 'age': 40},
    {'name': 'bülent', 'age': 44}
    ]
# burada birinci elemanın yaşına nasıl ulaşırız?

print(my_friends[0]['age'])
