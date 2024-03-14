## tuple da normal parantez kullanılır ve eleman değiştirilemez!!!
capitals = ('tahran', 'ankara', 'madrid', 'tiflis')


"""
print(len(capitals))
print(capitals[0])
print(capitals[1:3])

##
capitals[0] = 'izmir'
# TypeError: 'tuple' object does not support item assignment
"""

"""
for capital in capitals:
    print(capital)

"""

# aynı tuple içine farklı bir tuple ekleyebiliriz
"""
capitals = ('tahran', 'ankara', 'madrid', 'tiflis')
print(capitals)

capitals = ('berlin', 'roma')
print(capitals)
"""

### kümeler sırasız (elemanların indeks numarası yoktur ) ve tek elemanlardır
cities = {'izmir', 'istanbul', 'ankara', 'kars', 'istanbul'}

"""
print(type(cities))

print(cities)

cities.add('gaziantep')
print(cities)

cities.update(['edirne', 'trabzon'])
print(cities)
"""

"""
# set ten eleman silme
cities.remove('ankara')
print(cities)

cities.clear()
print(cities)
"""