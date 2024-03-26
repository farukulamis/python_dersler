#
"""
number = 1

while number <= 10:
    print(number)
    number = number + 1

"""

"""
#quit yazana kadar ekranda mesaj görelim
message =''

while message != 'quit':
    message = input('quit yazana kadar bu mesajı göreceksin')
    print(message)

"""

"""
# sonsuz dongü -- çıkmak için ctrl+c --terminali silme cls


while 5 > 3:
    print(' 5  büyüktür')

"""

#flag değişkeni
"""
my_flag = True
message =''

while my_flag:
    message = input('çıkmak için quit yazınız') # bu kısım sonsuz döngü olur
    if message =='quit':
        my_flag = False
    else:
        print(message)
    

"""

#break kullanımı. döngüden çıkmak için kullanılır.
"""
number =1

while number < 10:
    print(number)
    if number ==5:
        break
    number +=1
"""
# flag ile break in farkı flagda varolan koşul değiştirildi

#continue durumu
"""
number =1

while number < 10:
    number +=1
    if number % 2 == 0:
        continue
    print(number)
"""   