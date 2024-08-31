"""____________________________________________
   | Best way to learn a language is to use it #
   | 1.Gunluk kod yazin.                       #
   | 2.Interaktif calisin.                     #
   | 3.20-25 dk calis - ara verin.             #
   | 4.Hata yap ve cozum bulun.                #
   | 5.calisma arkadaslari bulun.              #
   | 6.Anladiginiizi ogretmeye calisin.        #
   | 7.Projeler yapin.                         #
   |___________________________________________#
"""
    #PRINT
#print('Merhaba Dunya')

#print('Turkiye'nin en kalabalik sehri istanbuldur.')
#-> Sag taraf string olarak algilanmadi.
#-> Bunu duzeltmek icin ters slash(\) koyariz.
#print('Turkiye\'nin en kalabalik sehri istanbuldur.')

#-> ya da 3 tirnaktan yararlanabiliriz.
#3 tirnak ile istedigimiz kadar bosluk birakabilir ve ya " tirnak koyabiliriz.
#print("""Turkiye'nin en kalabalik sehri istanbuldur.""")

#print("""T
#u
#r
#g
#a
#y""")


#print("Turgay\nAdamdir.")   #-> \n paragraf anlamina gelir yani \n'den sonra bir alt satira gecer.
#print("Turgay\tAdamdir.")   #-> \t bir TAB bosluk birakmak icin kullanilir.


#print("Hello", end="-")
#print("World")


#print("Turgay", "Kara",sep="-",end="123")     #-> sep"" arasina yazilan degeri kelimeler ARASINA koyar.
                                               #-> end"" arasina yazilan degeri cumlenin SONUNA koyar.

#-> Bu sekilde degiskenlerin yerlerini degistirebiliriz.
#sayi1=10
#sayi2=20
#sayi1, sayi2=sayi2, sayi1
#print(sayi2)


#x = 'Bu bir degisken denemesi.' 
#print(x)


#x=30
#y=70
#print(x+y) #-> 100



#print(10*'Turgay ')
#print(7)
#print(4*3)


#print("Ben " + str(16) + " yasimdayim.")    #-> Hem int hem str kullanilmaz. Bu yuzden sayiyi str yaptik.


    # RANGE
#print(list(range(10)))  #-> 0'dan 9'a kadar list seklinde yaz.
#([*range(10)])      #-> Ayni sey daha pratik.
#print([*range(1,10,2)])     #-> 1den baslayarak 9'a kadar ikiser sayarak git.

#for sayi in range(10):      #-> 0'dan 9'a kadar say.
    #print(sayi)

#for sayi in range(10):      #-> sayi 5'ten buyuk oldugu surece 9'a kadar say.
    #if sayi > 5:
        #print(sayi)


#for i in range(3):
    #print('Turgay')


    # SPLIT -> Listedeki elemanlari 2ye boler
#yorumbirakanlar = ["Talha Kara", "Turgay Kara", "Esref", "Ayfer", "Engin"]
#ad, soyad = yorumbirakanlar[1].split()[0], yorumbirakanlar[1].split()[1]   #-> listedeki 1.elemanin 0. parcasi + 1.elemanin 1.parcasi
#print(ad)
#print(soyad)



    # ENUMERATE
#words = ["a","b","c","d","e"]
#for word in enumerate(words):   #-> enumerate kodu direkt olarak siralamaniza yarar.
    #print(word)                 #(0, 'a')

#words = ["a","b","c","d","e"]
#for index, harf in enumerate(words):
    #print(index)                        #-> Sadece index'i(sirayi) yaz.

#words = ["a","b","c","d","e"]          
#for index, harf in enumerate(words):
    #print(harf)                         #-> Sadece harfleri yaz.

#words = ["a","b","c","d","e"]          
#for index, harf in enumerate(words):
    #print("{}.Harf {}".format(index+1, harf))


    # ZIP
#ulkeler = ["TR", "FR", "DE"]
#siralamalar = range(1,5)

#for ulke in zip(ulkeler, siralamalar):      #-> ulkeler ve siralamalar listlerini birbirine ekledik.
    #print(ulke)                             #-> listlerin len(eleman sayisi) birbirine esit olmasi lazim.


    #DEgIsKENLER ve SABITLER (Variables and Constants)
 #degiskenler;
#a = 'turgay' #degiskenin ismi a, degeri turgay
#b = 1.34
#print(b + 3) #-> 4.34


#isim, isim2 = "turgay", "talha"
#print(isim, isim2)  #-> turgay talha


 #sabitler;
#PI = 3.14 #-> Sabitler degistirilemez ve Degiskenin ismi BuYuK harfle yazilir.




    #NUMBERS
 #INTEGER(int)  #-> Tam Sayilar (-, 0, +)
#x = 34
#y = 0
#z = -34




    #FLOAT(float) #-> Noktali Sayilar (2.34, -0.40)
"""
ortalama = 95.7
sicaklik = -3
para = -0.31

x = para 
print(type(sicaklik))  #-> Degiskenin tipini gosterir. -> 'int'
print(ortalama)        #-> Degerini gosterir. -> 95.7  
print(type(x))         #-> x'in yani para'nin tipini gosterir. -> 'float'
                       #-> Noktali sayi oldugu icin 'float'
"""




    #STRING(str) #-> "cift tirnak" ("123", "1.23", "TURGAY", "A")
#isim = "Turgay Kara"
#sifre = "sifre123e"
#yas = "16" #->INTEGER DEgIL BU BIR STRING ->cunku " icine alinmis.
#print(type(yas))    #-> 'str'
#print(isim[3]) #-> 3.karakteri yazar -> "g"



    #STRING "METOTLAR"
#isim = "Turgay Kara"
#text1 = isim.center(10, '*')            #-> turgay = 6 karakterli, .center parantezine 10yazdik 6 turgayda var kaldi 4, bu 4 karakteri isim'in yanlarina dagitir.
#text2 = isim.rjust(10, '*')             #-> .center'a benziyor ama turgay'in sagina 4 karakter * yazdirir.
#text3 = isim.ljust(10, '*')             #-> .center'a benziyor ama turgay'in soluna 4 karakter * yazdirir.
#text4 = isim.startswith("t")            #-> degiskenimiz kucuk t ile mi basliyor?
#text5 = isim.endswith("y")              #-> degiskenim kucuk y ile mi bitiyor?
#text6 = isim.title()                    #-> Tum kelimelerin bas harfini buyuk yapar.
#text7 = isim.split(" ")                 #-> Parantez icine yazilan ifadeyi her gordugunde degiskeni parcalar ve bir listeye atar.
#text8 = "-".join(isim)                  #-> Her karakter arasina istenilen elemani yazar.
#text9 = isim.swapcase()                 #-> Buyuk harfleri kucuk, kucuk harfleri buyuk yapar.
#text10 = isim.upper()                   #-> Tum harfleri Buyuk yapar.
#text11 = isim.lower()                   #-> Tum harfleri Kucuk yapar.
#text12 = isim.capitalize()              #-> Cumlenin ilk kelimesinin bas harfini buyuk yapar(Digerlerini kucultur.)
#text13 = isim.count("a")                #-> Istenilen elemanin kac tane oldugunu soyler. -> 1
#text14 = isim.lower().count("t")        #-> Tum harfleri kucultur ve istenilen elemanin cumlede kac kere gectigini sayar.
#text15 = isim.upper().count("T")        #-> Istenilen elemani buyulterek istenilen elemani sayar.
#text16 = isim.find("Kara")              #-> Bulmamiza yarar. -> 7.indexten itibaren basladigini bize soyler.
#text17 = isim.index("g")                #-> Kacinci indexten itibaren oldugunu bize soyler. -> 3
#text18 = isim.replace("Kara", "Beyaz")  #-> .replace("Degistirmek istedigin.", "Yerine koyacagin.")
#text19 = '  - Hello World  '.lstrip()   #-> Sol taraftaki boslugu sil. -> .lstrip()
#text20 = '  - Hello World  '.rstrip()   #-> Sag taraftaki boslugu sil. -> .rstrip()
#text21 = '  - Hello World  '.strip()    #-> Her iki taraftaki boslugu sil. -> #.strip()
#print(text20)




    #BOOLEAN
  #Boolean (bool) #-> 2 degeri var. True ve False
"""
havaguzel = False #-> Hava guzel degil ise
yagmuryagiyor = True

print(havaguzel)    #-> False
print(type(havaguzel)) #->Degisken tipini gosterir. 'bool'
print(yagmuryagiyor) #-> True
"""


# []  -> List (liste)  / Degitirilebilir.
# ()  -> Tuple (demet) / Degistirilemez
# ()  -> Set (kume)
# {}  -> Dictionary (sozluk)


    #LIST
#List (list) #-> Liste. Birden fazla data tipi depolama
#sayilar = [1,2,3,9]
#print(type(sayilar))    #-> 'list'
#print(sayilar)


    #LISTE METOTLARI

#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#print(hayvanlar)



  #.append() METOTU
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#hayvanlar.append("Panda")   #-> .append() -> Listeye yeni eleman ekler.
#print(hayvanlar)



  #.remove() METOTU
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#hayvanlar.remove("Kedi")  #-> .remove() -> Listeden istenilen elemani cikartir.
#print(hayvanlar)



  #.pop() METOTU
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#hayvanlar.pop(2)             #-> .pop() -> Listeden istenilen elemani cikartir.
#print(hayvanlar)             #-> () Bos birakilirsa son elemani cikartir.



  #.copy() METOTU
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#hayvanlar2 = hayvanlar.copy()      #-> Aktarilacak liste = kopyalanacak liste.copy()
#print(hayvanlar2)



  #.extend() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#a.extend(b)             #-> a listesini ve b listesini birlestir.
#print(a)



  #.sort() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#b.sort()                #-> .sort() Listedeki elemanlari siralamamiza yarar.
#print(b)                #-> Buyukten kucuge siralar.

#b.sort(reverse = True)  #-> reverse tersine cevirir.
#print(b)                #-> Kucukten buyuge siralar.

#.sort Sadece sayilari degil kelimeleri de siralayabilir;
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#hayvanlar.sort(reverse = True)
#print(hayvanlar)         #-> hayvanlar listesini tersten(reverse) siralar


  #max-min() fonksiyonu
#x = [1,2,3,4,5,10,50]
#print(max(x))   #-> Listedeki en buyuk sayiyi gosterir.
#print(min(x))   #-> Listedeki en kucuk sayiyi gosterir.

  #.count() METOTU
#x = [5, 8, 4, 12, 10, 4]
#print(x.count(4))   #-> .count() Istenilen elemanin kac tane oldugunu soyler.


  #.index() METOTU
#y = [5, 8, 4, 12, 10]
#print(y.index(5))   #-> .index() Belirtilenn elemanin kacinci indexte oldugunu soyler.



  #.insert() METOTU
#b = [5, 8, 4, 12, 10]
#b.insert(1, "TURGAY")  #-> .insert() Belirtilen indexe istenilen elemani ekler.(Belirtilen indexi silmez.)
#print(b)               #-> 1.index'e "TURGAY" elemanini ekle.



  #.clear() METOTU
#a = [1, 2, 3]
#a.clear()       #-> Istenilen listedeki tum elemanlari siler(.clear).
#print(a)



  #slicing[] METOTU
#hayvanlar = ["At", "Kopek", "Kedi", "Balik", "Timsah"]
#print(hayvanlar)
#print(hayvanlar[2:4])  #-> 2. ve 4. Elemanlarin arasindaki elemanlari print eder. 2. eleman dahil, 4. eleman dahil DEgIL.
#print(hayvanlar[:3])    #-> [:3] sayi saga yazilirsa 3. Elemana kadar print eder. 3. eleman dahil DEgIL. #slicing metotunda [x:y] y hicbir zaman dahil edilmez.
#print(hayvanlar[3:])    #-> [3:] sayi sola yazilirsa 3. Elemandan sonraki elemanlari print eder. 3. eleman da dahil.
#print(hayvanlar[0:5:3]) #-> [x:y:z] -> z = Kac karakter araliklarla gidecegini soyler.
#--> 0.Karakterden 3.Karakter dahil olmamak uzere 2ser araliklarla(2.dahil) print et. <--#


#hayvanlar[3] = "Ari"   #-> Listenin 3.elemani yerine istenilen elemani koy.
#print(hayvanlar)


#insanlar = [["Turgay", "Kara"], ["Talha", "Beyaz"], ["Esref", "Siyah"]]
#print(insanlar[0])    #-> Turgay, Kara
#print(insanlar[0][1]) #-> Kara
#print(insanlar[2][0]) #-> Esref
#print(len(insanlar))  #-> len -> Listenin kac elemandan olustugunu soyler -> 3

#x = "Turgay"
#text = (len(x))
#print(text)






    #DEMETLER(Tuples)
 #Listelere benzer ama degistirilemez ve [] degil, () parantezlerle olusturulur.

#zamirler  = ("ben", "sen", "o", "biz", "siz", "onlar") #-> Degisiklik yapilamaz.
#print(zamirler[3])     #-> 3. index'i verir. -> biz

#zamirler[0] = "bne"    #-> 0. elemani yani "ben"i, "bne ile degistirmeye calistik.
 #print(zamirler)       #-> Hata verir cunku tuple elemanlari degistirilemez(yani eklenme veya cikartma yapilamaz.!)


#Tek elemanli bir tuple olusturmak icin:
#a = (5)
#print(a)    #-> 5 cikar. Yani tuple olusmadi.

#a = (4,)
#print(a)    #-> (4,) cikti. Tek elemanli tuple olusturduk.


#Bir kac tane demeti birlestirebiliriz:
#sayilar = (1, 2, 3, 4, 4)
#print(zamirler + sayilar)


#tuple'a bu sekilde de ekleme yapabiliriz:(ustteki daha pratik)
#tuple1=('Turgay', 'Kara')
#tuple1=tuple1+('udemy',)    #-> , olmazsa ERROR
#print(tuple1)

 #Tuple'dan, List'e donusturme
#list1 = [1,2,3]
#list2 = (1,2,3)
#list2 = list(list2)
#print(type(list2))

 #List'den Tuple'a donusturme
#list1 = tuple(list1)
#print(type(list1))


#print(zamirler[0:3])       #-> Tuple'larda indexleme islemleri gecerlidir.

#print(len(zamirler))       #-> .len eleman uzunlugunu gosterir.

#print(sayilar.count(4))    #-> .count -> Istenilen elemanin kac tane oldugunu soyler.

#print(sayilar.index(2))    #-> .index -> Istenilen elemanin kacinci indexte oldugunu gosterir.




    #SoZLuKLER(Dictionary)(dict)
 #Anahtar ve degerlerden olusan bir cok elemani icerisinde bulunduran veri tipi
"""
kimlik = {
        "isim":"Turgay",
        "soyisim":"Kara",
        "TC_NO":12367845689,
        "yer":["Kastamonu", "Merkez"],
        "bilgiler":{"email":"adsfs@gmail.com",
                    "kardesi sayisi":2
                    }
        }
kimlik["yil"] = 2005    #-> Kimligin icine yil ekledik.

print(kimlik["isim"])
print(kimlik["yil"])
print(kimlik)
print(len(kimlik))  #-> Eleman sayisini gosterir. -> 4

print(kimlik.keys())       #-> Sozlukteki anahtarlari gosterir.
print(kimlik.values())     #-> Sozlukteki degerleri gosterir.
print(kimlik.items())      #-> Anahtalaari ve Degerleri yanyana gosterir.
print(kimlik.get("yer"))   #-> Istenilen anahtarin degerini gosterir.
print(kimlik.update({"Anne_adi":"Ayfer"}))  #-> Listeye yeni Anahtar(key) ve Deger(value) ekledik.
print(kimlik.copy())       #-> Kimligi kopyalar.
kimlik.pop("isim")         #-> Sozlukten istenilen degeri cikarir.
kimlik.clear()             #-> Sozlukteki tum elemanlari siler.
print(kimlik)
"""

    #.get() METOTU
"""
ing_sozluk = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lutfen anlamini ogrenmek istediginiz kelimeyi yaziniz: ")
print(ing_sozluk.get(sorgu, "Bu kelime veritabanimizda yoktur!"))
#->Birinci arguman sorgulamak istedigimiz sozluk ogesidir.
#->Ikinci arguman ise bu ogenin sozlukte bulunmadigi durumda kullaniciya hangi mesajin gosterilecegini belirtir.
"""

#

"""
soru = input("sehrinizin adini tamami kucuk harf olacak sekilde yazin: ")
if soru == "istanbul":
    print("gok gurultulu ve saganak yagisli")
elif soru == "ankara":
    print("acik ve gunesli")
elif soru == "izmir":
    print("bulutlu")
else:
    print("Bu sehre iliskin havadurumu bilgisi bulunmamaktadir.")
"""
#Bunun yerine .get() metotunu kullanabiliriz.
"""
soru = input("sehrinizin adini tamami kucuk harf olacak sekilde yazin: ")
cevap = {"istanbul": "gok gurultulu ve saganak yagisli",
         "ankara": "acik ve gunesli", "izmir": "bulutlu"}
print(cevap.get(soru, "Bu sehre iliskin havadurumu bilgisi bulunmamaktadir."))
"""





    #KuMELER(Sets)
 #-> Suslu parantez kullanilir. {}, #-> Farkli elemanlardan olusan bir veri tipi, Ayni elemani 1'den fazla basmaz.
#sayi = {1, 3, 3, 34, 543, 5324, 5, 43}
#print(sayi)     #-> 2tane 3 yazmamiza ragmen 1 tanesini gosterir.


#sayi.add(100)       #-> Eleman eklemek icin kullanilir.
#print(sayi)


#sayi.discard(3)     #-> Istenilen elemani cikartamk icin kullanilir.
#print(sayi)


#sayi.remove(34)     #-> Yine eleman cikartmak icin kullanilir ama () ici bos birakilirsa hata verir.
#print(sayi)


#yeni_sayi = {32, 3, 25, 432, 4, 325, 4}
#sayi.update(yeni_sayi)     #-> Kumeleri birlestirdik.
#print(sayi)

"""
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print(a.difference(b))      #-> a ve b kumelerindeki farklari gosterir. -> 1, 2, 3
print(a.intersection(b))    #-> istenilen kumelerdeki kesisen elemanlari gosterir. -> 4
print(a.union(b))           #-> istenilen kumeleri birlestirerek tek bir kume haline getirir. Kesisen elemanlar varsa 1 kere gecirir. -> 1, 2, 3, 4, 5, 6, 7
print(len(a))               #-> istenilen kumedeki eleman sayisini gosterir.
"""



    #TYPE METOTU ve ornekler:
 #type Method #-> Bir degiskenin tipini anlamak icin kullanilir.
 #type(x)


#a = 1           #-> int'dan
#a = "1"         #-> str'e      ->1
#print(type(a))

#b = 1           #-> int'dan
#b = float(1)    #-> float'a    -> 1.0  -> floata cevirildigi icin int'in sonuna .0 koyar
#print(type(b))

#c = "1"         #-> str'den
#c = int("1")    #-> int'a      -> 1
#print(type(c))

#d = str(1)      #-> str'den
#d = float(1)    #-> float'a    -> 1.0
#print(type(d))

#e = 1.6         #-> float'dan
#e = int(1.6)    #-> int'a      -> 1   -> float'i integer'a cevirirken YUVARLAMAZ, KESER.
#print(type(e))

#f = 1.6         #-> float'dan
#f = str(1.6)    #-> str'e      -> 1.6
#print(type(f))



#x = [1, 2, 3, 3, 4, 5]
#print(tuple(x))  #-> Listeyi, Tuple'a cevirdik.
#print(set(x))    #-> Listeyi, Set haline getirdik. cakisan elemanlari bir kere yazar ve suslu parantez halinde yazar.
#print(dict(a = 7, a = 9)) #-> Sozluk haline getirdi ve Suslu paranteze aldi, esittir(=) isaretlerini iki nokta(:) yapti.


#t = (5,4,2,6,8)
#y = (list(t))   #-> y = t'nin Liste hali
#print(type(y))


#print(round(4.56)) #-> round() ->Herhangi bir sayiya Yuvarlama yapmak icin kullanilir. -> 5


#x = 35e3           #-> 3unun de tipi float
#y = 12E4           #-> olarak cikar, cunku;
#z = -87.7e1000     #-> e = 10 uzeri demektir


"""
x = -0.30
y = 1234
z = "z harfi"
print(type(x))  #-> 'float' -> Noktali Sayi
print(type(y))  #-> 'int'   -> Tam Sayi
print(type(z))  #-> 'str'   -> Kelime
"""


#print("Benim dogum yilim 2005")    #-> 'str'
#print("Benim dogum yilim" + 2005) #ERROR #-> Hem Integer hem String kullandigimiz icin ERROR verir.
#print("Benim dogum yilim " + str(2005))





  #KARsILAsTIRMA OPERAToRLERI
 # <   #-> Kucuk mudur?
 # >   #-> Buyuk mudur?
 # <=  #-> Kucuk mudur veya esit midir?
 # >=  #-> Buyuk mudur veya esit midir?
 # ==  #-> Esit midir?
 # =   #-> variable/degisken tanimlanirken kullanilir.
 # !=  #-> Esit degilse.
"""
#or:
print(5 > 3)  #->True
print(5 > 7)  #->False

print(7 >= 7) #-> True
print(7 >= 9) #-> False

print(6 != 5)  #-> True
"""

  #MANTIKSAL OPERAToRLER
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
 #or:
print(5 < 10 or 10 > 5)    #-> True
print(5 == 5 or 5 < 2)      #-> True
print(6 == 5 or 5 < 1)     #-> False
"""

    #AITLIK OPERAToRu
 #Aitlik operatoru, bir karakter dizisi ya da sayinin,
 #Herhangi bir veri tipi icinde bulunup bulunmadigini sorgulamamizi saglayan operatordur.

#Python’da bir tane aitlik operatoru bulunur. Bu operator de in operatorudur.
#Bu operatoru soyle kullaniyoruz:
"""
a = "abcd"
print("a" in a)     #-> True
print("f" in a)     #-> False

print("e" not in a) #-> True
print("b" not in a) #-> False
"""

    #ATAMA OPERAToRLERI
  # += operatoru
#a = 23
#a = a + 5
#print(a)    #-> a = 28


  # -= operatoru
#a = 23
#a = a - 5
#print(a)


  # /= operatoru
#a = 30
#a = a / 3
#print(a)


  # *= operatoru
#a = 20
#a = a*2
#print(a)


  # %= operatoru
#a = 40
#a = a % 3   #-> 40/3 -> Kalan= 1
#print(a)    #-> 1


  # **= operatoru
#a = 12
#a = a**2    #-> 12ussu 2
#print(a)    #-> 144


  # //= operatoru
#a = 9
#a = a//2    #-> Kalanini atar.
#print(a)    #-> 4





  #ARITMETIK
 # Toplama  x+y
 # cikarma  x-y
 # carpma   x*y
 # Bolme    x/y
 # (Tam Sayi sonuclu) Bolme  x//y #-> 5/2=2   #-> Noktanin sagini atar.
 # Mod Alma x%y      #-> Bolmenin Kalanini verir.
 # us alma  x**y     #-> x ussu y

  #DIKKAT: Islem Onceligi !!!
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




     #INPUT
  #input()
"""
isim = input("Adin ne?\n")
print("Merhaba " + isim)
yas = input("Yasin kac?\n")
print("Sen " + yas + " yasindasin")
print(type(yas))
"""



"""
 #IF-ELIF-ELSE KOMUTU
KatedilenMesafe = input("Ne kadar mesafe kat ettiniz?\n")
KalanMesafe = input("Ne kadar mesafeniz kaldi?\n")
if KatedilenMesafe > KalanMesafe:  #-> Bir kosulu kontrol etmek icin if kullanilir ve sonuna : koyulur.
    print("Yolun yarisini gectiniz.")
elif KatedilenMesafe < KalanMesafe:#-> Eger 'if' komutundaki deger yanlis ise calisacak komut elif tir.
    print("Yolun yarisini gecmediniz.")
else:                              #-> Eger 2 kosul da calismazsa devreye else girer.
    print("Yolun yarisindasiniz.")
"""
#
"""
kullanici_adi = "TurgayKara"
sifre = "12345"

ad = input("Kullanici Adinizi giriniz : ")
sifre_gir = input("sifrenizi giriniz : ")

if ad == kullanici_adi and sifre == sifre_gir:
    print("Sisteme basariyla giris yaptiniz.")
elif kullanici_adi != ad:
    print("Kullanici adinizi yanlis girdiniz.")
else:
    print("sifrenizi yanlis girdiniz.")
"""
#
"""
result = input("Basvuru Sonucunu Giriniz : ")
if "olumlu" in result.lower():
    print("Ise alindiniz!")
elif "olumsuz" in result.lower():
    print("Ise alinmadiniz!")
else:
    print("Lutfen gecerli bir deger giriniz!")
"""
#
"""
print("Merhaba, bu program sayinizin 50'den >, < ya da = oldugunu soyler. :)")
number = int(input("Sayi giriniz: "))
if (number == 50):
    print("Sayi 50.")
elif (number < 50):
    print("Sayi 50'den kucuk.")
else:
    print("Sayi 50'den buyuk.")
"""
#
"""
gender = input("Cinsiyet bilginizi giriniz (E/K): ")
if gender.upper() == "E":
    BirtOfDate = int(input("Dogum yilinizi giriniz: "))

    if 2020 - BirtOfDate == 20 or 2020 - BirtOfDate > 20 and 2020 - BirtOfDate <= 28:
        print("Askere gidebilirsiniz.")
    elif 2020 - BirtOfDate != 20:
        print("Askere gidemezsiniz.")
    else:
        print("Yasiniz hesaplanamadi.")
elif gender.upper() == "K":
    print("Kadinlar askere alinamiyor.")
else:
    print("Lutfen bir cinsiyet giriniz.")
"""


"""
havadurumu = input("\n1-Gunesli\n2-Karli\n3-Yagmurlu\n4-Bulutlu\n\nHava nasil:")

if havadurumu == "1":
    print("Take sunglass.")

elif havadurumu == "2":
    print("Wear boats.")

elif havadurumu == "3":
    print("Take umbrella")

else:
    print("it's okay. You can go outside.")
"""
#

"""
list = ["0","1", "2","3","4","5"]
while True:
    hedefrakam = input("bir rakam giriniz:")

    if hedefrakam in list:
        print("\nistediginiz rakam listede bulunuyor.")


    else:
        print("\nistediginiz rakam listede bulunmuyor.\nSenin icin bu rakami da listeye ekleyecegim.")

        list.append(hedefrakam)
        print("\niste, guncel liste!")
        print(list)
        
        if len(list) == 10:
            print("Tum rakamlari girdiniz. Program sonlandiriliyor.\n")
            break
"""
#

"""
yorumbirakanlar = ["Talha", "Turgay", "Esref", "Ayfer", "Engin"]

kullanicisayisi = 0
for kullanici in yorumbirakanlar:
    kullanicisayisi = kullanicisayisi + 1
    print(kullanicisayisi, kullanici)

"""
# Ayni kod while dongusu ile

"""
yorumbirakanlar = ["Talha", "Turgay", "Esref", "Ayfer", "Engin"]
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
        print('{0}. Moderatorun Adi {1} ve Soyadi {2}'.format(modsayisi, ad, soyad))

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
#
"""
sayi = int(input("Bir sayi giriniz : "))
if sayi >= 0:       #-> Burdaki if,(2)
    if sayi == 0:       #-> Burdaki if,(1)
        print("Sayi sifirdir.")
    else:               #-> Burdaki else icindir.(1)
        print("Sayi pozitiftir.")
else:               #-> Burdaki icindir.(2)
    print("Sayi negatiftir.")
"""





    #FOR & WHILE DONGUSU
 #-> Bir durumun surekli tekrar etmesine denir.
#for Harfler in "CODING SUMMIT":     #-> : koymayi unutma.!
    #print(Harfler)

#for i in range(3):       #-> 'range' komutu her zaman 0'dan baslar.
    #print(i)             #-> 0 1 2


#for keep in range(5):
    #print("Hello")


#for keep in range(1,10+1):
    #print(keep)


#for keep in range(1,10,2):      #->1'den 10'a kadar 2'ser olarak yaz.
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


#while True:
    #print("Merhaba")   #-> Dongu True oldugu icin sonsuza kadar devam eder.

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
sayac = 10
while sayac >= 0:
    print("Sayac = " + str(sayac))
    sayac = sayac - 1
print("Sayac bitti.")
"""
#
"""
x = 0
while x <= 10:
    print("Bizim sayimiz = " , x)
    x = x + 1
else:
    print("Sayiniz 10dan buyuk.")
"""
#
"""
sayilar = [1,2,3,4,5,6,7]
print(2 in sayilar)
for sayi in sayilar:
    print("Sayiniz = ", sayi)
    if sayi == 5:
        break       #-> Dongu 5'e gelince bitsin.
else:
    print("Dongu bitti.")
"""
#
"""
 #ic ice dongu
sayi = [1,2,3,4,5,6,7]
sayi2 = [1, 2, 3]
for sayi in sayi:    #-> Ifadeyi sayilar icindeki eleman kadar dondurur.
    for x in sayi2:
        print(x)
else:
    print("Dongu bitti.")
"""

#for x in range(1,20,2): #-> 1den 20ye kadar 2ser artacak sekilde don.
    #print(x)


#print(list(range(1,20))) #-> 1den baslayarak 20ye kadar liste seklinde sayar.


#gelirler = [3000, 4000, 5000, 6000, 7000, 10000]
#for gelir in gelirler:
    #print(gelir * 2)





    #RANDOM METOTU
"""
import random #-> Bazi variable'lar icinden rastgele secmemizi saglar.
renkler = ["mavi", "beyaz", "kirmizi", "sari"]
for x in range(100):    #-> 100 defa Print et.
    print(random.choice(renkler))   #-> .choice -> Secmek istedigimiz icin kullaniyoruz.
                                    #-> random.choice(renkler) -> renkler'in icinden rastgele sec.
"""





    #FONKSIYONLAR (Functions)   Kodun devaminda da kullanacaksan sonradan da cagirabilirsin.

# def <fonksiyon_ismi>(<argumanlar>): # snake_case

"""
 Bu kod ne ise yarar?                # docstring    -> Kodu okuanin daha rahat anlamasi icin kullanilabilir.
"""

#...                                  # return/print farklari

"""
# def (print)
def bes_bastir():
    print("5")      # 5
#bes_bastir()


# def (return)
def bes_dondur():
    return 5
#print(bes_dondur())


a = bes_bastir()
print(a)        # Def'i print ile yazdimiz icin "None" output'u verecek.

b = bes_dondur()
print(b)        # Def'i return ile yazdigimiz icin "5" output'u verecek.

"""
#def sayi_dondur(sayi):
    #return sayi
#print(sayi_dondur(37))

"""

def sayi_dondur(sayi=250):
    return sayi
print(sayi_dondur(89))      #-> 89 ciktisini verecek.


def sayi_dondur(sayi=250):
    return sayi
print(sayi_dondur())        #-> Arguman vermeden cagirdigimiz icin Default olani(250) verecek.
"""

"""
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
print(buyuk_sayi_dondur(5,10))
"""


""" # Hatali Kullanim   
def buyuk_sayi_dondur(a,b):
    return a
    return b           # Sart vermeden 2 tane Return kullandigimiz icin kod ilk gordugunu calistiracak-> a yani 5'i dondurecek
    #if a>b:
        #return a
    #elif b>a:
        #return b
print(buyuk_sayi_dondur(5,10))
"""


#def KacYasindasin(yas):
    #print("Ben ", yas, " yasimdayim.")
#KacYasindasin(15)  #-> Ben  15  yasimdayim.





    #FORMAT
#isim = "Turgay"
#soyisim = "Kara"
#print(f"{isim} {soyisim} bir insandir.")


#isim = "Turgay"
#soyisim = "Kara"
#print("Benim ismim {} soyadim {} ".format(isim, soyisim))     #-> .format() suslu parantezin icine istenileni yazar.


#isim = "Turgay"
#soyisim = "Kara"
#print("{0} {1} bir  insandir.".format(isim, soyisim))


#isim = "Turgay"
#soyisim = "Kara"
#print("{C1} {C2} bir  insandir.".format(C1 = isim, C2 = soyisim))


#a=10
#b=15
#print("{} > {}".format(a,b), a < b)    #-> True
#print("{} > {}".format(b,a), b < a)    #-> False


 #format ornekleri
"""
name = "Turgay"
surname = "Kara"
age = 20
job = "Full-Stack deweloper"
city = "Istanbul"
salery = 12000
print(f"Ben {name} {surname}\n{age} yasimdayim.\n{city} sehrinde yasiyorum.\nAyda {salery} dolar kazaniyorum.")
"""

#numberone = 20
#numbertwo = 12
#print(f"Toplam : {numberone + numbertwo}\ncikartma : {numberone - numbertwo}\ncarpma : {numberone * numbertwo}\nBolme : {numberone / numbertwo}")



#def kare_al(x):
    #print(x**2)
#kare_al(5)  #-> 5'in karesini alir.



#def alan(r, pi = 3.14):
    #print(pi*r**2)
#alan(12)    #-> Pi tanimli oldugu icin Sadece yari capi yazarak alani bulduk.





    #RETURN
  #Bir sonuc dondurmesi istenen fonksiyonlarda fonksiyonun calistiktan sonra bir deger dondurmesi icin return anahtar kelimesi kullanilir.
"""
def alan(r, pi = 3.14):
    return pi*r**2
alan1 = alan(6)
alan2 = alan(8)
print(alan1 + alan2)
"""


    # BREAK
#harfler = ["a", "b", "c", "d", "e"] * 1000
#for index, harf in enumerate(harfler):
    #if harf == "c":
        #print("{} harfi {}. indexte!".format(harf, index))      #-> c harfinin kacinci indexte oldugunu soyler.
        #break   #-> break komutu olmasaydi dongu 1000 kere tekrar edecekti ama istedigimizi elde ettigimiz anda cikmak istiyorsak "break" kullanabiliriz.


    # CONTINUE
#for sayi in range(1, 6):
    #if sayi%2 == 0: #-> cift sayi sorgulama mantigi sayi%2 -> sayinin 2'ye bolumunden kalan 0 ise...
        #continue    #-> continue oldugu icin islemi range'de verdigimiz son sayiya kadar devam ettirecek.
    #print(sayi)     #-> tek olanlari yazdi cunku eger sayi 2'ye bolunuyorsa devam etmesini soyledik.


    # PASS
#for sayi in range(1, 6):
    #if sayi%2 == 0:
        #pass            #-> bu sekilde bir durum gorursen burayi atla.
    #else:
        #print(sayi)     #-> cift olma durumunu atladigimiz icin tek olanlari yazdirdik.


#for sayi in range(1, 6):
    #if sayi%2 != 0:     #-> Kalan 0'a esit degil ise...
        #pass            #-> bu sekilde bir durum gorursen burayi atla. (Tek olan sayilari atla)
    #else:
        #print(sayi)     #-> Tek olanlari atladigimiz icin cift olanlari yazdirdik.


    # BREAK
#harfler = ["a", "b", "c", "d", "e"] * 1000
#for index, harf in enumerate(harfler):
    #if harf == "c":
        #print("{} harfi {}. indexte!".format(harf, index))      #-> c harfinin kacinci indexte oldugunu soyler.
        #break   #-> break komutu olmasaydi dongu 1000 kere tekrar edecekti ama istedigimizi elde ettigimiz anda cikmak istiyorsak "break" kullanabiliriz.


    # CONTINUE
#for sayi in range(1, 6):
    #if sayi%2 == 0: #-> cift sayi sorgulama mantigi sayi%2 -> sayinin 2'ye bolumunden kalan 0 ise...
        #continue    #-> continue oldugu icin islemi range'de verdigimiz son sayiya kadar devam ettirecek.
    #print(sayi)     #-> tek olanlari yazdi cunku eger sayi 2'ye bolunuyorsa devam etmesini soyledik.


    # PASS
#for sayi in range(1, 6):
    #if sayi%2 == 0:
        #pass            #-> bu sekilde bir durum gorursen burayi atla.
    #else:
        #print(sayi)     #-> cift olma durumunu atladigimiz icin tek olanlari yazdirdik.


#for sayi in range(1, 6):
    #if sayi%2 != 0:     #-> Kalan 0'a esit degil ise...
        #pass            #-> bu sekilde bir durum gorursen burayi atla. (Tek olan sayilari atla)
    #else:
        #print(sayi)     #-> Tek olanlari atladigimiz icin cift olanlari yazdirdik.


#for sayi in range(1,10):
    #if sayi < 5:
        #pass            #-> pass komutunu kullanmasaydik bu kisimda hata alacaktik.
                         #-> buradaki satiri goze alma. Projemize sonradan ekleme yapacaksak ekleyebiliriz.
    #else:
        #print("Hey!")



"""
    # CLASS: Benzer ozellikler, ortak amaclar tasiyan gruplar olusturmak icin kullanilir.

#class VeriBilimci():
    #print("Bu bir siniftir")

class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
#print(VeriBilimci.sql)      #-> Sinif ozelliklerine erismek.


#VeriBilimci.sql = "hayir"   #-> Sinif ozelliklerini degistirmek
#print(VeriBilimci.sql)


ali = VeriBilimci()          #-> Sinif orneklendirmesi #-> alinin ozellikleri VeriBilimci class'inin ozelliklerini tasir. 
#print(ali.sql)
#print(ali.deneyim_yili)

ali.bildigi_diller.append("Python")     #-> Alinin bildigi dillere Python'i ekledik.

#veli = VeriBilimci()
#print(veli.bildigi_diller)   #-> Alinin diline ekledigimiz icin sonradan sinifa eklenen tum kullanicilara Python'i ekledi.
                              #-> bu sorunu cozmek icin:

class VeriBilimci():
    bolum = ""
    sql = ""
    deneyim_yili = 5
    bildigi_diller = ["R", "Python"]    #-> VeriBilimci sinifinin bildigi dillere ekleme yaptik.
    def __init__(self):
        self.bildigi_diller = []        #-> Her elemanin kendi icinde degisebilen ozelliklerden olusacak.
        self.bolum = ""

veli = VeriBilimci()
#print(veli.bildigi_diller)
veli.bildigi_diller.append("R")
#print(veli.bildigi_diller)


turgay = VeriBilimci()
turgay.bildigi_diller.append("Python")
turgay.bildigi_diller.append("R")
turgay.bolum = ("Data Hunter")
#print(turgay.bildigi_diller)

#print(VeriBilimci.bildigi_diller) 


ali.bolum = "istatistik"
print(ali.bolum)
print(turgay.bolum)
print(VeriBilimci.bolum)
"""


"""
class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)     #-> Dil ekleme islemini fonksiyon kullanarak otomatik hale getirdik.


#print(dir(VeriBilimci))     #-> Class nesnesinin erisilebilecek olan degerlerini getirir.
#VeriBilimci.dil_ekle("R")   #-> Hata

duru = VeriBilimci()
duru.dil_ekle("R")
print(duru.bildigi_diller)

turgay = VeriBilimci()
turgay.dil_ekle("Python")
print(turgay.bildigi_diller)
"""


"""
    # MIRAS YAPILARI: Daha onceden yapilmis hazir Classlar'i kullanmak.

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""

class DataScience(Employees):       #-> Miras (Employees)
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
#veribilimci1.


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.
"""


"""
turgay = Employees()
class Employees_yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.Firstname = FirstName
        self.Lastname = LastName
        self.Adress = Adress

turgay = Employees_yeni("a", "b", "c")
print(turgay.Adress)    #-> Output: c
"""



    # Fonksiyonel Prgoramlama

# Yan Etkisiz Fonksiyon Ornek-1 (basit yan etki)

"""
A = 9

def impure_sum(b):
    return b + A

def pure_sum(a, b):
    return a + b

print(impure_sum(6))    #-> Sonuc A'ya bagli olarak degisir. (Yan Etki)
print(pure_sum(3,4))    #-> Sonuc her zaman 7 olur.

"""



# Yan Etkisiz Fonksiyon Ornek-2 (olumcul yan etki)
# Islem sonucunda C:\Users\Turgay> klasoru icerisindeki deneme.txt adli metin dosyasisin verilerini output olarak verecektir.

#class LineCounter:
    #def __init__(self, filename):
        #self.file = open(filename, 'r')
        #self.lines = []
    
    #def read(self):
        #self.lines = [line for line in self.file]
    
    #def count(self):
        #return len(self.lines)


#lc = LineCounter('deneme.txt') 

#print(lc.lines) 
#print(lc.count())

#lc.read()

#print(lc.lines)
#print(lc.count())

#FP

#def read(filename):
  #with open(filename, 'r') as f:
      #return [line for line in f]

#def count(lines):
  #return len(lines)

#example_lines = read('deneme.txt')
#lines_count = count(example_lines)
#lines_count


"""
    # isimsiz fonksiyonlar
def old_sum(a, b):
    return a + b

print(old_sum(4,5))


    # LAMBDA
new_sum = lambda a,b: a + b
print(new_sum(4,5))

sirasiz_liste = [("b",3), ("a", 8), ("d", 12), ("c", 1)]
print(sirasiz_liste)

    # Kucukten buyuge dogru siralayalim:
print(sorted(sirasiz_liste, key = lambda x: x[1]))  # Output: [('c', 1), ('b', 3), ('a', 8), ('d', 12)]
"""


"""
    # Vektorel Operasyonlar (OOP)
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a))

for i in range(len(a)):
    ab.append(a[i]*b[i])

print(ab)       #-> Output: [2  6 12 20]
"""

#   Yukaridaki ornekte ayni islemi daha cok caba harcayarak yapmistik.

#import numpy as np
#a = np.array([1,2,3,4])
#b = np.array([2,3,4,5])
#print(a*b)      #-> Output: [2  6 12 20]



    # MAP & FILTER & REDUCE

#my_list = [1, 2, 3, 4, 5]
#for i in my_list:
    #print(i + 10)


    # Map   -> Dort islem yapabiliriz.
#my_list2 = [1, 2, 3, 4, 5]
#print(list(map(lambda x: x * 10, my_list2)))  #-> Ayni isi map kullanarak daha pratik sekilde yaptik.


    # Filter    -> Filtreleyip cikti alabiliriz.
#my_list3 = [1,2,3,4,5,6,7,8,9,10]
#print(list(filter(lambda x: x % 2 == 0, my_list3)))


    # Reduce    -> Kendi icinde dort islem yapabiliriz.
#from functools import reduce
#my_list4 = [1,2,3,4]
#print(reduce(lambda a,b: a + b, my_list4))  #-> Output: 1+2+3+4 = 10



    # Modul & Kutuphane Olusturmak  (yeni bir py dosyasi actik. (HesapModulu.py))

#import HesapModulu
#HesapModulu.yeni_maas(1000) #-> HesapModulu.py adli dosyanin icerisinde calisacak.

#import HesapModulu as hm
#hm.yeni_maas(1000)          #-> Ayni isi daha pratik sekilde gerceklestirdik.

#from HesapModulu import yeni_maas
#yeni_maas(1000)             #-> Ayni isi 3 farkli modul kullanma teknigiyle yaptik.

#import HesapModulu as hm
#print(hm.maaslar)           #-> Kutuphanemizin(modulumuzun) icinden maaslar adli degerleri cektik.



    # Hatalar & Istisnalar

"""
a = 10
b = 0
#print(a/b)     #-> Payda 0 olamaz. #ZeroDivisionError: division by zero

try:
    print(a/b)      #-> a/b ifadisini calistirmayi dene eger calismaz ise,
except ZeroDivisionError:       #-> "ZeroDivisionError" hata tipini istisna olarak gor ve print ifadesini dondur.
    print("Payda 0 degerinde olamaz!")


a = 10
b = "2"
#print(a/b)      #-> Str ifade ile Int bir ifade Matematiksel olarak calistirilamaz. #Type Error

try:
    print(a/b)
except TypeError:       #-> except: Gormezden gelme metotu
    print("Str ifade ile Int bir ifade Matematiksel olarak calistirilamaz")
"""