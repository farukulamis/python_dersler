# boş liste, tuple, set ve dictionary oluşturma
"""
list1 =[]
list2 =list()

print(type(list1))
print(type(list2))

tuple1= ()
tuple2= tuple()

print(type(tuple1))
print(type(tuple2))
"""
"""
set1= {} # boş set oluşturmanın böyle bir yöntemi yok. Bu ifade dictionary dir!!!!
set2= set()

print(type(set1))
print(type(set2))
"""

"""
dict1= {}
dict2= dict()

print(type(dict1))
print(type(dict2))
"""

# Değeri sayı olan 3 elemanlı bir dictionary oluştur, 2. sayıyı ve sayıların ortalamasını çıkar
"""
friends= {'mahmut': 38, 'deniz': 29, 'ebru': 21}

print(friends['deniz'])


sum= 0
for age in friends.values():
    sum +=age
print(sum/len(friends))

# ikinci yol

print(sum(friends.values())/ len(friends))

"""

#2 olul arkadaşı ve numarlarından oluşan dict oluştur, başka bir arkadaşını ekle,
# ekli olan arkadaşı sil, update ile bir arkadaşın numarasını değiştir ve yeni arkadaş ekle
"""
friends = {'mahmut': 345, 'ebru': 127}

friends['eren'] = 76

print(friends)

del friends['mahmut']
print(friends)

friends.update({'mahmut': 777, 'eren': 666})
print(friends)
"""

# my_dict ={'even_numbers': [2, 4, 6, 8, 10, 12, 14, 16]}
# yukarıdaki dict yapısındaki tüm elemanların karesini alaım ve aynı dict üzerine update edelim
"""
my_dict ={'even_numbers': [2, 4, 6, 8, 10, 12, 14, 16]}

for x in my_dict.values():
    my_list =[]
    for y in x:
        my_list.append(y**2)

my_dict['even_numbers'] = my_list
print(my_dict)
"""

# my_friends = {'ali': 28, 'mahmut': 46, 'ebru': 34}
#keylerden liste oluştur, value lardan liste oluştur ve value kar toplamını çıkar
"""
my_friends = {'ali': 28, 'mahmut': 46, 'ebru': 34}

my_key_list= []
my_value_list= []

for key, value in my_friends.items():
    my_key_list.append(key)
    my_value_list.append(value)

print(my_key_list)
print(my_value_list)
print(sum(my_value_list))
"""


# dict comprehension ile 1 den 10 a kadar olan sayılar, sayıları key, 
# kareleri value olacak şekilde tek satırda oluştur
"""
numbers = { x: x**2 for x in range(1,11)}
print(numbers)
"""