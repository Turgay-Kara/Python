    #FOR-WHILE DÖNGÜSÜ
 #-> Bir durumun sürekli tekrar etmesine denir.
#for Harfler in "CODING SUMMIT":     #-> : koymayi unutma.!
    #print(Harfler)

#for i in range(3):       #-> 'range' komutu her zaman 0'dan başlar.
    #print(i)             #-> 0 1 2


#for keep in range(5):
    #print("Hello")


#for keep in range(1,10+1):
    #print(keep)


#for keep in range(1,10,2):      #->1'den 10'a kadar 2'şer olarak yaz.
    #print(keep)                 #->1, 3, 5, 7, 9

    
#for keep in range(10,0,-1):
    #print(keep)


#list1 = [1,2,3,4,5,6,7,8,9,10]
#for keep in list1:
    #print(keep)


#dict1 = {"Name":"Ali","Surname":"Yildirim"}
#for keep in dict1.items():
    #print(keep)


#list2 = []
#for keep in range(1,1000):
    #list2.append(keep)
#for keep in list2:
    #print(keep)


#number = int(input("Satir Sayisi Giriniz : "))
#for keep in range(1,number+1):
    #print("*"*keep)


#for keep in range(10,0,-1):
    #print(keep)



"""
tup1 = (1, 3, 5, 7)

for sayi in tup1:
    print(sayi)
"""

"""
list = [[1,2], [3,4], [5,6]]
for x,y in list:
    print(x*y)
"""


"""
kullanici1 = {
    'ad':'Naz',
    'soyad':'Yagci'
}
print(kullanici1.values())

for k, v in kullanici1.items():
    print("Key: {} \t Value: {}".format(k,v))

for v in kullanici1.values():
    print("Value: {} \t".format(v))
"""


#while True:
    #print("Merhaba")   #-> Döngü True olduğu için sonsuza kadar devam eder.


"""
sayi = 1
while True:
    sayi = sayi + 1
    print(sayi)
"""


"""
x = 1
while x < 5:
    print("hello, user!")
    x = x + 1
else:
    print("The loop has stopped!")
"""
#
"""
sayaç = 10
while sayaç >= 0:
    print("Sayaç = " + str(sayaç))
    sayaç = sayaç - 1
print("Sayaç bitti.")
"""
#
"""
x = 0
while x <= 10:
    print("Bizim sayimiz = " , x)
    x = x + 1
else:
    print("Sayiniz 10dan büyük.")
"""
#
"""
sayilar = [1,2,3,4,5,6,7]
print(2 in sayilar)
for sayi in sayilar:
    print("Sayiniz = ", sayi)
    if sayi == 5:
        break       #-> Döngü 5'e gelince bitsin.
else:
    print("Döngü bitti.")
"""
#
"""
 #iç içe döngü
sayi = [1,2,3,4,5,6,7]
sayi2 = [1, 2, 3]
for sayi in sayi:    #-> İfadeyi sayilar içindeki eleman kadar döndürür.
    for x in sayi2:
        print(x)
else:
    print("Döngü bitti.")
"""

#for x in range(1,20,2): #-> 1den 20ye kadar 2şer artacak şekilde dön.
    #print(x)


#print(list(range(1,20))) #-> 1den başlayarak 20ye kadar liste şeklinde sayar.


#gelirler = [3000, 4000, 5000, 6000, 7000, 10000]
#for gelir in gelirler:
    #print(gelir * 2)


"""
yorumbirakanlar = ["Talha", "Turgay", "Eşref", "Ayfer", "Engin"]

kullanicisayisi = 0
for kullanici in yorumbirakanlar:
    kullanicisayisi = kullanicisayisi + 1
    print(kullanicisayisi, kullanici)

"""
# Ayni kod while döngüsü ile

"""
yorumbirakanlar = ["Talha", "Turgay", "Eşref", "Ayfer", "Engin"]
kullanicisayisi = 0
sira = 0

while sira < len(yorumbirakanlar):
    kullanicisayisi = kullanicisayisi + 1
    print(kullanicisayisi, yorumbirakanlar[sira])
    sira = sira + 1
"""
#

"""
yorumbirakanlar = ["Ismail Aydemir", "Uygar Aydin", "Naz Yagcioglu", "Ferhat Ibrik", "Ulas Acil", "Bilal Kurucay"]
mod = "Ferhat Ibrik"
kullanicisayisi = 0
modsayisi = 0

for kullanici in yorumbirakanlar:
    kullanicisayisi +=1
    ad, soyad = kullanici.split()[0], kullanici.split()[1]

    if kullanici == mod:
        modsayisi +=1
        print('{0}. Moderatörün Adi {1} ve Soyadi {2}'.format(modsayisi, ad, soyad))

    else:
        print('{0}. Kullanicinin Adi {1} ve Soyadi {2}'.format(kullanicisayisi, ad, soyad))
"""
#
"""
for keep in range(1,11):
    if keep == 6:
        break
    print(keep)
"""
#
"""
for keep in range(1,11):
    if keep == 6:
        continue
    print(keep)
"""