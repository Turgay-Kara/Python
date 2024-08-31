"""
        VERI MANIPULASYONU (NumPy & Pandas)
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

# soru 1 >> m matrisinin 0. satirindaki tüm sütunlari seçin. 
#print(m[0, 0:4])


# soru 2 >> m matrisinin 2. satirindaki 1. ve 3. sütunlardan elemanlari seçin. 
#print(m[2, [1,3]])


# soru 3 >> m matrisinin 1. ve 3. satirlarindan, 2. sütunlarindaki elemanlari seçin.
#print(m[[1,3], 2])


# soru 4 >> m matrisinin 1. ve 2. satirlarindan, 0. ile 3. sütunlar arasindaki elemanlari seçin.
#print(m[1:3, 1:3])


# soru 5 >> m matrisinin 0. ve 2. satirlarindan, 1. ve 2. sütunlarindaki elemanlari seçin.
#print(m[[0,2], 1:3])



"""
        VERI MANIPULASYONU (NumPy & Pandas)
"""

#Pandas: Verileri düzenleme, analize etme ve işleme

#import pandas as pd

#seri = pd.Series([11,22,33,44,55,66])
#print(seri)
#print(type(seri))     #-> Seri tipi >> <class 'pandas.core.series.Series'>  
#print(seri.axes)      #-> Seri'nin indexlerine erisim. >> [RangeIndex(start=0, stop=6, step=1)]
#print(seri.dtype)     #-> >> int64
#print(seri.size)      #-> Seri eleman sayisi >> 6
#print(seri.ndim)      #-> Kaç Boyutlu >> 1D
#print(seri.values)    #-> >> [11 22 33 44 55 66]

#print(seri.head(3))   #-> Seri'nin ilk 3 indexini getirecek.
#print(seri.tail(3))   #-> Seri'nin son 3 indexini getirecek.



    # Index isimlendirme
#a = pd.Series([10,20,30,40,50], index = [1,3,5,7,9])
#print(a)

#b = pd.Series([10,20,30,40,50], index = ["a","b","c","d","e"])
#print(b)
#print(b["a"])        #-> a'nin karsilik geldigi degere eristik.

#print(b["a":"d"])    #-> slice islemi ile a'dan d'ye kadar eristik.



    # Sozluk uzerinden Seri olusturma
#sozluk = {"reg": 10, "log": 11, "cart": 12, "passwd":1234}
#seri = pd.Series(sozluk)
#print(seri)

#print(seri["reg":"cart"])   #-> Slicing islemi



    # 2 Seriyi Birlestirerek Seri olusturma
"""    
sozluk = {"reg": 10, 
          "log": 80, 
          "cart": 12, 
          "passwd":1234}

sozluk2 = {"name": "Duru", 
           "age": 18, 
           "salary": 75000, 
           "langs": ["Python", "R"]}

seri = pd.Series(sozluk)
seri2 = pd.Series(sozluk2)
print(pd.concat([seri,seri2], axis=1))
"""



    # Eleman islemleri
#import numpy as np
#import pandas as pd

#a = np.array([11,22,33,44,55])
#seri = pd.Series(a)
#print(seri)

#print(seri[0])
#print(seri[0:3])    #-> 0'dan 2.indexe kadar

#seri = pd.Series([120, 240, 360, 480], index=["reg","log","cart","rf"])
#print(seri)
#print(seri.values)  # >> [120 240 360 480]
#print(seri.keys)    # >>
#print(seri.index)   # >> Index(['reg', 'log', 'cart', 'rf'], dtype='object')
#print(seri.items())
# >>
#for index, value in seri.items():
    #print("Index: {}, Value: {}".format(index, value))



    # Eleman Sorgulama
#print("reg" in seri)        # >> True
#print("a" in seri)          # >> False
#print(seri["reg"])          # >> 120
#print(seri[["reg", "log"]])

#seri["reg"] = 150           #-> "reg" Key'inin Value'sunu 150 olarak degistirdik. 
#print(seri["reg"])
#print(seri["reg":"cart"])



    # DataFrame
#import pandas as pd
#l = [1,20,300,4000]
#df = pd.DataFrame(l, columns= ["degisken_ismi"])
#print(df)


#import numpy as np
#m = np.arange(1,10).reshape(3,3)
#df = pd.DataFrame(m, columns= ["var1", "var2", "var3"])
#print(df)



    # DF Ornek:
"""
import pandas as pd
data = {
    "names": ["Turgay", "Emir", "Beyza"],
    "langs": ["Python", ["Html CSS"], "R"],
    "salary": [120000, 750000, 85000]
    }
df = pd.DataFrame(data)
print(df)
"""



    # DF isimlendirme
#m = np.arange(1,10).reshape(3,3)
#df = pd.DataFrame(m, columns= ["var1", "var2", "var3"])
#print(df.columns)           #-> Degisken isimlerini getirir >> Index(['var1', 'var2', 'var3'], dtype='object')

#df.columns = ["deg1", "deg2", "deg3"]   #-> Degisken isim degistirme:
#print(df)
#print(df.axes)          #-> Satir ve Sutun bilgilerini verir.
#print(df.shape)         #-> Boyut Bilgisi   >> (3, 3)
#print(df.ndim)          # >> 2D
#print(df.size)          # >> 9

#print(df.values)        #-> DataFrame'den Verileri cekip Elemanlari bir Array'e donusturecek.
#print(type(df.values))  #-> >> <class 'numpy.ndarray'>

#print(df.head(2))        #-> Bastan 2 satiri getirir.
#print(df.tail(2))        #-> Sondan 2 satiri getirir.


#print(df["var1"][0:2])      #-> var1 sutununda 0 ve 1. satirlari al.
#print(df[["var1","var2"]][0:2])


#a = np.array([1,2,3,4,5])
#df = pd.DataFrame(a, columns = ["deg1"])
#print(df)


"""
import numpy as np
import pandas as pd

s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

sozluk = {
    "var1": s1,
    "var2": s2,
    "var3": s3
}
df = pd.DataFrame(sozluk)
df.index = ["a","b","c", "d","e"]       #-> index isimlendirme islemi
print(df)
"""
#df2 = df.drop("a", axis = 0)            #-> a satirini sil.
#print(df2)

#df.drop("a", axis = 0, inplace = True)  #-> a satirini sil. (ayni islem farkli metot)
#print(df)

#df.drop(["a", "b"], axis = 0, inplace = True)   #-> a ve b satirini sil
#print(df)



    # Sorgulama Islemi
#print("var1" in df)        #-> var1 df icerisinde yer aliyor mu?   >> True
#l = ["var1", "var4", "var2"]
#for i in l:
    #print(i in df)         #-> l'nin icerisindeki elemanlar df'in icerisinde mi kontrol et.



#df["var4"] = df["var1"] * df["var2"]         #-> "var4" Yeni sutun ekledik.

#print(df.drop("var4", axis = 1))             #-> "var4" gecici olarak silindi.

#df.drop("var4", axis = 1, inplace = True)    #-> "var4" kalici olarak silindi.
#print(df)

#l = ["var1", "var2"]
#print(df.drop(l, axis = 1))              #-> l listinin icindeki degiskenler silindi.



    # loc: Tanimlandigi sekli ile secim yapmak icin kullanilir.
import numpy as np
import pandas as pd
#m = np.random.randint(1,30, size = (10,3))
#df = pd.DataFrame(m ,columns =  ["var1","var2","var3"]) 
#print(df)
#print(df.loc[0:3])          #-> 0, 1, 2, 3. satirlari alir.


    # iloc: Alisik oldugumuz indexleme mantigi ile secim yapar.
#print(df.iloc[0:3])         #-> 0, 1, 2. satirlari alir.
#print(df.iloc[1,1])
#print(df.iloc[:3,:2])       #-> Toplam 3 satir, 2 sutun alir.
#print(df.loc[0:3, "var3"])
#print(df.iloc[0:3])
#print(df.iloc[0:3]["var3"]) #-> Sadece 3.sutun


        #-> Ozet:
    # Loc:  Verilen kurallara bagli bir sekilde secim yapilacaksa. (Gozlem ya da Degisken isimlendirmeleri)
    # iLoc: Verilen isimlendirmelerden bagimsiz klasik index mantigi ile secim yapilacaksa.



    # .var
#m = np.random.randint(1,30, size = (10,3))
#df = pd.DataFrame(m ,columns =  ["var1","var2","var3"]) 
#print(df)
#print(df.var1)
#print(df[df.var1 > 15])             #-> var1 sutunu icerisinde 15'ten buyuk olan degerleri al.
#print(df[df.var1 > 15]["var1"])     #-> ayni islem yalnizca var1 sutununu alacak.

#print(df[(df.var1 > 15) & (df.var3 < 5)]["var1","var3"])   #-> Verilen 2 durum da aynanda gerceklesmesi lazim. (ve baglaci)
#print(df[(df["var1"] > 15) & (df["var3"] < 5)][["var1", "var3"]])

#print(df.loc[(df.var1 > 15), ["var1", "var2"]])     # .loc olmadan calistirirsak hata aliriz.
#print(df[(df.var1 > 15)][["var1", "var2"]])         # Ayni islemi .loc kullanmadan calistirdik.



    # Join(birlestirme) islemleri
    # help(pd.concat)
#m = np.random.randint(1,30, size = (5,3))
#df1 = pd.DataFrame(m ,columns =  ["var1","var2","var3"]) 
#df2 = df1 + 99
#join = pd.concat([df1, df2], ignore_index=True)    #-> Default olarak False olan degeri True yaptigimizda istenilen siralamayi elde edecegiz.
#print(join)                                        #-> False olarak kaldiginde birlestirme islemini:
                                                    #-> >> 01234 01234 seklinde yapacakti


#m = np.random.randint(1,30, size = (5,3))
#df1 = pd.DataFrame(m ,columns =  ["var1","var2","var3"]) 
#df2 = df1 + 99
#join = pd.concat([df1, df2], ignore_index=True)
#df2.columns = ["var1","var2","deg3"]

#birlestir = pd.concat([df1, df2])
#print(birlestir)

#birlestir2 = pd.concat([df1, df2], join='outer', ignore_index=True)
#print(birlestir2)

#birlestir3 = pd.concat([df1, df2], join = "inner", ignore_index=True)
#print(birlestir3)                                  #-> 3. sutunlar kesismedigi icin sadece var1 ve var2'yi aldi.