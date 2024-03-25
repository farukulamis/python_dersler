# kullanıcıdan gelen herhangi bir sayının tek mi çift mi olduğunu bulan program
"""
number = int(input('Bir sayı giriniz: '))

if number % 2 ==1:
    print(f'{number} tek sayıdır')
else:
    print(f'{number} çift sayıdır')
"""


# kullanıcıdan gelen herhangi bir sayının pozitif, negatif ve 0 mı olduğunu gösterelim
"""
num1 = int(input('bir sayı giriniz: '))

if num1 == 0:
    print(f'{num1} sayısı 0 dır')
elif num1 > 0:
    print(f'{num1} sayısı pozitifdır')
else:
    print(f'{num1} sayısı negatifdır')

"""

"""
# 
#x = 10
#y = 5
#if x > y:
#    print(f'{x} sayısı {y}\'den büyüktür')

#bu ifadeyi tek satır formunda yazınız.
x = 10
y = 5
if x > y: print(f'{x} sayısı {y}\'den büyüktür')

"""

"""
# kullanıcının girdiği herhangi bir sayının faktöriyelini bulun

num = int(input('bir sayı giriniz'))
faktoriyel = 1
if num >=1:
    for i in range(1, num+1):
        faktoriyel= faktoriyel*i
    print(faktoriyel)
elif num == 0:
    print(f'{num}\'ın faktöriyeli 1 dir')
else:
    print('negatif sayının faktoriyeli yoktur')
"""


# notes ={'ahmet}: 58, 'mehmet':76, 'ebru': 44, 'pınar':90}
# 50 üzerindeki öğrencilerin geçti yazması

"""
notes ={'ahmet': 58, 'mehmet':76, 'ebru': 44, 'pınar':90}

for key,value in notes.items():
    if value >= 50:
        print(f'{key} aldığı not {value}: GEÇTİ')
    else:
        print(f'{key} aldığı not {value}: KALDI')
"""