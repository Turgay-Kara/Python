    #TYPE METHOTU ve Ornekler:
 #type Method #-> Bir değişkenin tipini anlamak için kullanılır.
 #type(x)


#a = 1           #-> int'dan
#a = "1"         #-> str'e      ->1
#print(type(a))

#b = 1           #-> int'dan
#b = float(1)    #-> float'a    -> 1.0  -> floata çevirildiği için int'ın sonuna .0 koyar
#print(type(b))

#c = "1"         #-> str'den
#c = int("1")    #-> int'a      -> 1
#print(type(c))

#d = str(1)      #-> str'den
#d = float(1)    #-> float'a    -> 1.0
#print(type(d))

#e = 1.6         #-> float'dan
#e = int(1.6)    #-> int'a      -> 1   -> float'ı integer'a çevirirken YUVARLAMAZ, KESER.
#print(type(e))

#f = 1.6         #-> float'dan
#f = str(1.6)    #-> str'e      -> 1.6
#print(type(f))



#x = [1, 2, 3, 3, 4, 5]
#print(tuple(x))  #-> Listeyi, Tuple'a çevirdik.
#print(set(x))    #-> Listeyi, Set haline getirdik. Çakışan elemanları bir kere yazar ve süslü parantez halinde yazar.
#print(dict(a = 7, a = 9)) #-> Sözlük haline getirdi ve Süslü paranteze aldı, eşittir(=) işaretlerini iki nokta(:) yaptı.


#t = (5,4,2,6,8)
#y = (list(t))   #-> y = t'nin Liste hali
#print(type(y))


#print(round(4.56)) #-> round() ->Herhangi bir sayıya Yuvarlama yapmak için kullanılır. -> 5


#x = 35e3           #-> 3ünün de tipi float
#y = 12E4           #-> olarak çıkar, çünkü;
#z = -87.7e1000     #-> e = 10 üzeri demektir


"""
x = -0.30
y = 1234
z = "z harfi"
print(type(x))  #-> 'float' -> Noktalı Sayı
print(type(y))  #-> 'int'   -> Tam Sayı
print(type(z))  #-> 'str'   -> Kelime
"""


#print("Benim doğum yılım 2005")    #-> 'str'
#print("Benim doğum yılım" + 2005) #ERROR #-> Hem İnteger hem String kullandığımız için ERROR verir.
#print("Benim doğum yılım " + str(2005))