"""
        VERI MANIPULASYONU (NumPy)
"""

# NumPy -> Bilimsel islemler icin kullanilir.
#import numpy as np  #-> Bu her zaman calisir durumda olmali.

#import numpy as np
#a = np.array([1,2,3,4])
#b = np.array([2,3,4,5])
#print(a * b)
#print(type(a))      #-> <class 'numpy.ndarray'>

#print(np.array([1, 2, 3.14]))        #-> Hepsini ondalikli sekilde yazacaktir.
#print(np.array([1, 2, 3.14], dtype = "int"))    #-> bu sekilde her elemani int hale getirebiliriz.


    # 0'dan Array olusturmak
#print(np.zeros(5, dtype = "int"))       #-> [0 0 0 0 0]
#print(np.ones(5, dtype = "int"))        #-> [1 1 1 1 1]
#print(np.ones((3,5), dtype = "int"))    #-> 3 satir, 5 sutunluk bir Array olusturdu.
#print(np.full(3, 5))                    #-> 3'lerden olusan bir sekilde yaptik.
#print(np.arange(0, 31, 3))              #-> 0'dan 30'a kadar ucer ucer say. *
#print(np.linspace(0,1,10))              #-> 0 ve 1 arasinda 10 tane deger olustur. *
#print(np.random.normal(10,4, (3,4)))    #-> Matris (2 boyutlu) # sayilari random verecek.
#print(np.random.randint(0,10), (3,3))   #-> Random integer *
#print(np.random.randint(10, size = 5))  #-> 0'dan 10'a kadar rastgele 5 deger


#a = np.random.randint(10, size = 5)
#print(a.ndim)   #-> Kac boyutlu oldugu bilgisini verir.
#print(a.shape)  #-> Boyut bilgilerini verir (her bir boyuttaki eleman sayisini)
#print(a.size)   #-> Toplam eleman sayisini verir.
#print(a.dtype)  #-> Array veri tipini verir (elemanlarin veri tipi, ornegin int64, float32 gibi).

#b = np.random.randint(10, size = (3,5))
#print(b)
#print(b.ndim)   #-> 2 boyutlu oldugu icin "2" ciktisini verecek.
#...

#print(np.random.randint(10, size = (5,3,2)))    #-> 5 blok, 3 satir, 2 sutun



# >> randint ile olusturulmus bir Zar ornegi: <<
"""
atis = 0
yazi = 0
tura = 0
print("\n")
while yazi < 100 and tura < 100:
    para = np.random.randint(0,2)
    if para == 0:
        print("Yazi Geldi!")
        yazi +=1
        atis +=1

    if para == 1:
        print("Tura Geldi!")
        tura +=1
        atis +=1

ortalama_yazi = (yazi / atis) * 100
ortalama_tura = (tura / atis) * 100

print("\nPara Toplam:", atis, "Kere Atildi!\n")
print("Yazi Gelme Ihtimali: %{:.1f} olarak belirlendi.".format(ortalama_yazi))
print("Tura Gelme Ihtimali: %{:.1f} olarak belirlendi.\n".format(ortalama_tura))
"""



    # RESHAPE
    # Tek boyuttan > 2 Boyuta yukseltmek veya 2 Boyuttan > Tek boyuta indirmek gibi islere yarar.

#print(np.arange(1,10))  #-> 1'den 10'a kadar olan bir Array.
#print(np.arange(1,10).reshape(3,3))     #-> 1'den 10'a kadar olan Array'i 3'e 3 olacak sekilde donusturur.


#a = np.arange(1,10)
#b = np.arange(1,10).reshape(3,3)
#print(a.ndim)   #-> 1D -> Vektor
#print(b.ndim)   #-> 2D -> Matris


#a = np.arange(1,10)
#print(a.ndim)               #-> 1D              [1 2 3 4 5 6 7 8 9]     -> Tek Parantez
#print(a.reshape(1,9).ndim)  #-> 2D (reshape)   [[1 2 3 4 5 6 7 8 9]]    -> Cift Parantez



    # CONCATENATE
    # Array birlestirme gorevini yapar.

#x = np.array([1,2,3])
#y = np.array([4,5,6])
#z = np.array([7,8,9])

#print(np.concatenate([x,y]))    #-> [1 2 3 4 5 6]
#print(np.concatenate([x,y,z]))  #-> [1 2 3 4 5 6 7 8 9]


#a = np.array([[1,2,3],
              #[4,5,6]]) #-> 2 Boyutlu bir Array olusturduk. # Okunakli olmasi icin alt satira yazdik.
#print(a)

#print(np.concatenate([a,a]))            #-> Satir bazinda birlestirir.
#print(np.concatenate([a,a], axis = 1))  #-> Sutun bazinda birlestirir.  (0 satirlari, 1 sutunlari ifade eder.)
                                         #-> 2 Boyutlularda ise yarar.



    # SPLITTING
    # Array ayirma gorevini yapar.

#x = np.array([1,2,3,99,99,3,2,1])
#print(np.split(x, [3,5]))   #-> Output: [array([1, 2, 3]), array([99, 99]), array([3, 2, 1])]


#x = np.array([1,2,3,99,99,3,2,1])
#a,b,c = np.split(x, [3,5])
#print(a)        #[1 2 3]
#print(b)        #[99 99]
#print(c)        #[3 2 1]


    # 2D ayirma
#m = np.arange(16).reshape(4,4)

#print(np.vsplit(m, [2]))     #-> Yataylamasina 2 parcaya bolecek.
#ust, alt = np.vsplit(m, [2]) #-> Her 2 parcaya da deger atadik "ust", "alt" diye.
#print(ust)
#print(alt)

#print(np.hsplit(m, [2]))     #-> Dikeylemesine 2 parcaya bolecek.
#sag, sol = np.hsplit(m, [2]) #-> Her 2 parcaya da deger atadik "sag", "sol" diye.
#print(sag)
#print(sol)



    # SORTING
    # Arraylari siralama gorevini yapar.

#v = np.array([3,4,1,2])
#print(np.sort(v))       # [1 2 3 4]

#v = np.array([3,4,1,2])
#v.sort()    #-> Array'i komple sirali olan sekliyle degistirdi.
#print(v)    #-> [3,4,1,2] cikmasi gerekirken [1 2 3 4] ciktisini verdi.


    # 2D siralama
#m = np.random.normal(20, 5, (3,3))  #-> Ortalamasi 20, Standart Sapmasi  5 olacak sekilde 3'e 3'luk bir Array olustur.
#print(m)

#print(np.sort(m, axis = 1))         #-> Satir bazinda bir Siralama gerceklestirdi.
#print(np.sort(m, axis = 0))         #-> Sutun bazinda bir Siralama gerceklestirdi.


    # Index ile Elemanlara Erismek
#a = np.random.randint(10, size = 10)
#print(a)
#print(a[0])     #-> ilk elemana eristik.
#a[0] = 100      #-> Elemanin degerini degistirebiliriz.

#m = np.random.randint(10, size = (3,5))
#print(m)
#print(m[1,2])   #-> 2. Satirin, 3. Elemanina erisiriz.
#m[1,4] = 99     #-> 2. Satirin, 5. Elemanini 99 olarak degistirdik.
#m[1,4] = 2.2    #-> Float olarak ekleyemez. O yuzden sadece 2 diye ekleyecek.
#print(m)


    # Slice islemleri
#a = np.arange(20,30)
#print(a)
#print(a[0:3])   #-> 0'dan 3. elemana kadar yazdirir
#print(a[0::2])  #-> ilk elemandan baslayarak ikiser ikiser sona kadar yazdirir.


    # 2D Slice islemleri    #-> (0 1 2 diye sayma yap!)
#m = np.random.randint(10, size = (5,5))
#print(m)
#print(m[0:,2])         #-> Butun satirlari sec, 2. sutun'u getir.
#print(m[2:,0])         #-> 2. Satir ve sonrasini sec, 0. sutunu getir.
#print(m[0:2, 0:3])     #-> 0'dan 2'ye kadar satirlari sec, 0'dan 3'e kadar sutunlari getir.
#print(m[0:,0:2])       #-> Butun satirlari sec, 0 ve 1. sutunu getir.


    # Alt Kume islemleri
#a = np.arange(1,26).reshape(5,5)
#alt_a = a[0:3, 0:2]

#alt_a[0,0] = 999
#print(alt_a)
#print(a)                   #-> Array'i komple degistirdi. Bunu onlemek icin .copy() metotu:

#b = np.arange(1,26).reshape(5,5)
#alt_b = b[0:3, 0:2].copy()  #-> Yapilan alt_kume degisikligini Ana Arraydan bagimsiz gerceklestirecek.
#alt_b[0,0] = 999
#print(alt_b)
#print(b)                    #-> Ana Array .copy() metotunu kullandigimiz icin degismedi.



    # Fancy Index ile Elemanlara erismek(!)
#import numpy as np
#v = np.arange(0,31,3)
#print(v[5])                 #-> Az elemanda bu yontemi kullanabiliriz.
                             #-> Cok fazla deger oldugunda kullanacagimiz metot: Fancy index
#al_getir = [1,3,5]
#print(v[al_getir])


    # 2D Fancy Index
#m = np.arange(9).reshape(3,3)
#print(m)
#satir = np.array([0,1])     #-> 0.Satirin, 1.Sutunu
#sutun = np.array([1,2])     #-> 1.Satirin, 2.Sutunu
#print(m[satir, sutun])      #-> [1 5]


    # Basit Index + Fancy Index
#print(m[0, [1,2]])

    # Slice + Fancy
#print(m[0:, [1,2]])


    # Kosullu Eleman Islemleri
#v = np.array([1,2,3,4,5])
#print(v > 5)        #-> Her eleman icin Sorgu islemi yapacaktir. Output: [False False False False False]
#print(v > 3)        #-> Output: [False False False  True  True]
#print(v[v > 2])     #-> v array'inin 2'den buyuk olan elemanlarini getir. [3 4 5]
#print(v[v != 3])    #-> 3 disindaki elemanlari cagir. [1 2 4 5]
#print(v*2)          #-> [ 2  4  6  8 10]
#print(v**2)         #-> [ 1  4  9 16 25]


    # Matematiksel Islemler
#v = np.array([1,2,3,4,5])
#print(v-1)
#print(v*5/10 - 1)

# >> ufunc <<
#print(np.subtract(v,1))     # -  islemi
#print(np.add(v,1))          # +  islemi
#print(np.multiply(v,4))     # *  islemi
#print(np.divide(v,3))       # /  islemi
#print(np.power(v,3))        # ** islemi

#print(np.mod(v,2))                  # % (bolumunden kalan) islemi
#print(np.absolute(np.array([-3])))  # Mutlak Deger alma islemi

#print(np.sin(360))          # sin alma islemi
#print(np.cos(360))          # cos alma islemi

#x = np.array([1,2,10])
#print(np.log(x))            # log alma islemi
#print(np.log10(x))



        # Cheat Sheet
        # "istedigimiz icerik" + "cheat sheet"
        # ornek: "numpy mathematics cheat sheet"



    # NumPy ile 2 Bilinmeyenli Denklem Cozum
"""
    5x + y = 12
    x + 3y = 8
    ___________
    -14x = -28
    x = 2
    y = 2
"""

#a = np.array([[5,1], [1,3]])    #-> (1.denklemde) 5 = 1.Bilinmeyen Katsayisi, 1 = 2.Bilinmeyen Katsayisi
                                 #-> (2.denklemde) 1 = 1.Bilinmeyen Katsayisi, 3 = 2.Bilinmeyen Katsayisi

#b = np.array([12, 8])           #-> (1.denklemde) Sonuc = 12
                                 #-> (2.denklemde) Sonuc = 8
#x = np.linalg.solve(a, b)
#print(x)



    # Practice:
#m = np.arange(16).reshape(4, 4)
#print(m)

# soru 1 >> m matrisinin 0. satirindaki tum sutunlari secin. 
#print(m[0, 0:4])


# soru 2 >> m matrisinin 2. satirindaki 1. ve 3. sutunlardan elemanlari secin. 
#print(m[2, [1,3]])


# soru 3 >> m matrisinin 1. ve 3. satirlarindan, 2. sutunlarindaki elemanlari secin.
#print(m[[1,3], 2])


# soru 4 >> m matrisinin 1. ve 2. satirlarindan, 0. ile 3. sutunlar arasindaki elemanlari secin.
#print(m[1:3, 1:3])


# soru 5 >> m matrisinin 0. ve 2. satirlarindan, 1. ve 2. sutunlarindaki elemanlari secin.
#print(m[[0,2], 1:3])