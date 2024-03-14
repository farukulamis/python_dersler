"""
dersler =['mat', 'fizik', 'kimya', 'ingilizce', 'türkçe']
print(dersler[1].upper())
print(dersler[-1].upper())
"""

"""
# nested list kullanımı
dersler =['mat', ['fizik', 'kimya'], 'ingilizce', 'türkçe']
print(dersler[1])
print(dersler[1][0])
print(dersler[1][1])
# son elemanı len fonksiyonu kullanarak yazdır
print(dersler[len(dersler)-1])
"""

"""
dersler =['mat', 'fizik', 'kimya', 'ingilizce', 'türkçe']
print(len(dersler))
dersler.append('tarih')
print(dersler)
dersler[len(dersler):] = ['coğrafya']
print(dersler)
"""

"""
dersler =['mat', 'fizik', 'kimya', 'ingilizce', 'türkçe']
dersler.insert(len(dersler), 'tarih')
print(dersler)
"""

"""
# del yöntemiyle kimya dersini kaldır
#remove yöntemiyle türkçe dersini kaldır
dersler =['mat', 'fizik', 'kimya', 'ingilizce', 'türkçe']

del dersler [2]

print(dersler)

dersler.remove('türkçe')
print(dersler)
"""


"""
#listeyi azalacak ve artacak şekilde sıralamak

numbers = [8, 4, 5, 1, 6, 9, 2, 7, 3, 10]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
"""



"""
#iç içe listenin içindeki sondaki elemanlar ile yeni bir liste oluşturalım

dersler =[['mat', 'fizik'], ['kimya', 'ingilizce'], ['türkçe', 'tarih']]

dersler2 = []

for ders in dersler:
    dersler2.append(ders[-1])

print(dersler2)
"""

"""
# 1 den 10 a kadar olan sayıların karelerinden liste oluştur
# daha sonra aynı işlemi list comprehension ile yapalım

karesi = []

for kare in range(1, 11):
    kare = kare**2
    karesi.append(kare)

print(karesi)

######################
karesi =[kare**2 for kare in range(1, 11) ]
print(karesi)
"""
