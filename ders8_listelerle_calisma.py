cities =['tokyo', 'madrid', 'londra', 'kiev']
"""
#madrid in indeks numarasını öğrenmek istersek
print(cities.index('madrid'))

print(cities.index('ankara')) # hata verir çünkü ankara listede yok
"""

"""
print('ankara' in cities)
"""

"""
for city in cities:
    print(city)
"""


"""
for city in cities:
    print(f'gezilen şehir: {city}')
"""

"""
# stringi listeye çevirme
str_cities = 'tokyo, madrid, kiev'

my_list = str_cities.split(', ')

print(my_list)

str_email = 'arinyazilim@gmail.com'
my_list2 = str_email.split('@')
print(my_list2)
"""

"""
for number in range(1,10):
    print(number)
"""

"""
# 1 den 20 ye kadar olan çift sayıları yazdırmak için;

for number in range(2, 21, 2):
    print(number)
"""

"""
numbers = list(range(1,11))
print(numbers)
"""
"""
numbers = [number for number in range(1,11)]
print(numbers)
"""

"""
sehirler = ['izmir', 'ankara', 'istanbul']
print(sehirler)
sehirler2 = sehirler[:]
print(sehirler2)
sehirler2.append('artvin')
print(sehirler)
print(sehirler2)
"""