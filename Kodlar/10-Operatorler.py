  #KARŞILAŞTIRMA OPERATÖRLERİ
 # <   #-> Küçük müdür?
 # >   #-> Büyük müdür?
 # <=  #-> Küçük müdür veya eşit midir?
 # >=  #-> Büyük müdür veya eşit midir?
 # ==  #-> Eşit midir?
 # =   #-> variable/değişken tanımlanırken kullanılır.
 # !=  #-> Eşit değilse.
"""
#ör:
print(5 > 3)  #->True
print(5 > 7)  #->False

print(7 >= 7) #-> True
print(7 >= 9) #-> False

print(6 != 5)  #-> True
"""

  #MANTIKSAL OPERATÖRLER
 # True and True   #-> True
 # True and False  #-> False
 # False and True  #-> False
 # False and False #-> False

 # True or True    #-> True
 # True or False   #-> True
 # False or True   #-> True
 # False or False  #-> False

 # not True        #-> False
 # not False       #-> True
"""
 #ör:
print(5 < 10 or 10 > 5)    #-> True
print(5 == 5 or 5 < 2)      #-> True
print(6 == 5 or 5 < 1)     #-> False
"""

    #AİTLİK OPERATÖRÜ
 #Aitlik operatörü, bir karakter dizisi ya da sayının,
 #Herhangi bir veri tipi içinde bulunup bulunmadığını sorgulamamızı sağlayan operatördür.

#Python’da bir tane aitlik operatörü bulunur. Bu operatör de in operatörüdür.
#Bu operatörü şöyle kullanıyoruz:
"""
a = "abcd"
print("a" in a)     #-> True
print("f" in a)     #-> False

print("e" not in a) #-> True
print("b" not in a) #-> False
"""

    #ATAMA OPERATÖRLERİ
  # += operatörü
#a = 23
#a = a + 5
#print(a)    #-> a = 28


  # -= operatörü
#a = 23
#a = a - 5
#print(a)


  # /= operatörü
#a = 30
#a = a / 3
#print(a)


  # *= operatörü
#a = 20
#a = a*2
#print(a)


  # %= operatörü
#a = 40
#a = a % 3   #-> 40/3 -> Kalan= 1
#print(a)    #-> 1


  # **= operatörü
#a = 12
#a = a**2    #-> 12üssü 2
#print(a)    #-> 144


  # //= operatörü
#a = 9
#a = a//2    #-> Kalanını atar.
#print(a)    #-> 4





  #ARİTMETİK
 # Toplama  x+y
 # Çıkarma  x-y
 # Çarpma   x*y
 # Bölme    x/y
 # (Tam Sayı sonuçlu) Bölme  x//y #-> 5/2=2   #-> Noktanın sağını atar.
 # Mod Alma x%y      #-> Bölmenin Kalanını verir.
 # Üs alma  x**y     #-> x üssü y

  #DİKKAT: İŞLEM ÖNCELİĞİ !!!
"""
x = 3
y = 5
print(x+y)  #-> 8
print(x-y)  #-> -2
print(x*y)  #-> 15
print(x/y)  #-> 0.6
print(x//y) #-> 0
print(x%y)  #-> 3
print(x**y) #-> 243
"""