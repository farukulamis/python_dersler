cities = ['barcelona', 'floransa', 'moskova', 'belgrad', 'tahran']
"""
print(cities[0])

print(len(cities))

print(cities[-1])

print(cities[:2])"""

"""
cities[0] = 'tiflis'

print(cities)"""


"""
cities.append('tiflis')
print(cities)
# eklediğimiz liste elemanını en sona ekledi
"""

"""
cities.insert(0, 'roma')
print(cities)
# insert de birinci eklenecek indeksi ikinci eklenecek liste elemanını verir
"""

"""
del cities[0]
print(cities)
# burada del ile sildiğimiz elemana ulaşamayız...
"""

'''
cities2 = cities.pop()
print(cities)
print(cities2)
'''

"""
cities.remove('belgrad')
print(cities)
"""
"""
cities.sort()
print(cities) # alfabetik olarak sıralama yapar

cities.sort(reverse=True)
print(cities) # alfabetik sıranın tersine sıralar"""

# sort metodu sıralamayı kalıcı olarak değiştirir. kalıcı değişiklik istemiyorsak sorted fonksiyonu kullanılırız

"""
print(cities)
print(sorted(cities))
print(cities)
"""

numbers =[12, 28, 11, 27]

print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))