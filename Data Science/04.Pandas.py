"""
        VERI MANIPULASYONU (Pandas)
"""

#Pandas: Verileri duzenleme, analize etme ve isleme

#import pandas as pd

#seri = pd.Series([11,22,33,44,55,66])
#print(seri)
#print(type(seri))     #-> Seri tipi >> <class 'pandas.core.series.Series'>  
#print(seri.axes)      #-> Seri'nin indexlerine erisim. >> [RangeIndex(start=0, stop=6, step=1)]
#print(seri.dtype)     #-> >> int64
#print(seri.size)      #-> Seri eleman sayisi >> 6
#print(seri.ndim)      #-> Kac Boyutlu >> 1D
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



    # ileri seviye Birlestirme islemi
    # Birebir Birlestirme

#df1 = pd.DataFrame({'calisanlar' : ["Turgay", "Emir", "Zehra"],
                    #'grup' : ["Data", "Design", "AI"]})

#df2 = pd.DataFrame({'calisanlar': ["Turgay", "Emir", "Zehra"],
                    #'ilk_giris' : [2010, 2014, 2019]})

#birlestirx = pd.merge(df1,df2)       #-> 2 Veri setinde de Calisanlar ortak oldugu icin ona gore birlestirme yapti.
#print(birlestirx)

#birlestiry = pd.merge(df1,df2, on = 'calisanlar')
#print(birlestiry)


    # Coktan teke Birlestirme
#df3 = pd.merge(df1, df2)
#df4 = pd.DataFrame({'grup' : ["Data", "Design", "AI"],
                    #'mudur' : ["Turgay", "Emir", "Efe"]})

#b = pd.merge(df3,df4)   #-> 4 farkli Veri setini tek bir veri seti altinda topladik.
#print(b)

#df5 = pd.DataFrame({'grup' : ['Data', 'Data', 'Data', 'Design', 'Design', 'AI'],
                    #'skills' : ['Math', 'Coding', 'Acumen', 'Html', 'CSS', 'Yonetim']})


#birlestirz = pd.merge(df1, df5)     #-> Calisanlari da otomatik olarak coklayacaktir.
#print(birlestirz)



    # Toplulastirma ve Gruplama
# Basit toplulastirma Metotlari
"""
import seaborn as sns
df = sns.load_dataset("planets")    # Veri seti ornegi
print(df.head())                    # Baslik altinda yaz.
print(df.shape)                     # Satir, Sutun
print(df["mass"].mean())            # Ortalama hesaplama
print(df["mass"].count())           # Degerleri say.
print(df["mass"].min())             # Degiskendeki min deger
print(df["mass"].max())             # Degiskendeki max deger
print(df["mass"].sum())             # Degisken degerlerini topla
print(df["mass"].std())             # Standart Sapmasini verir.
print(df["mass"].median())          # Degiskenin Medyanini verir.
print(df["mass"].var())             # Varyansini gosterir.
print(df["mass"].iloc[0])           # Veri setinin ilk Degiskeni
print(df["mass"].iloc[-1])          # Veri setinin son Degiskeni

print(df.describe().T)              # Betimsel istatistikleri verir.
print(df.dropna().describe().T)     # Eksik degerleri silerek Betimsel istatistikleri verir.
"""


# Gruplama Islemleri
"""
df = pd.DataFrame({'classes' : ["A","B","C","A","B","C"],
                   'point' : [90,50,90,75,85,10]}, columns=["classes", "point"])

#print(df.groupby("classes").mean())     # Siniflarin Not ortalamasi
#print(df.groupby("classes").sum())      # Notlarin Toplami
"""


#import seaborn as sns
#df = sns.load_dataset("planets")
#print(df.head())    # >> cesitli grup degiskenleri

#print(df.groupby("method")["orbital_period"].mean())       
#print(df.groupby("method")["year"].sum())
#print(df.groupby("method")["orbital_period"].describe())    # Toplu sekilde gormek icin.



    # Aggregate
"""
import pandas as pd
df = pd.DataFrame({'gruplar': ["A","B","C","A","B","C"],
                   'degisken1': [10,23,33,22,11,99],
                   'degisken2': [100,253,333,3262,111,969]},
                   columns= ['gruplar', 'degisken1', 'degisken2'])

#print(df.groupby("gruplar").mean())
#print(df.groupby("gruplar").aggregate(["min", "median", "max"]))
#print(df.groupby("gruplar").aggregate({"degisken1": "min", "degisken2":"max"}))

"""



    # Filter
"""    
import pandas as pd
df = pd.DataFrame({'gruplar': ["A","B","C","A","B","C"],
                'degisken1': [10,23,33,22,11,99],
                'degisken2': [100,253,333,3262,111,969]},
                columns= ['gruplar', 'degisken1', 'degisken2'])

def filter_func(x):
    return x["degisken1"].std() > 9
print(df.groupby("gruplar").std())
print(df.groupby("gruplar").filter(filter_func))    #-> Standart sapmasi > 9 olan verileri getir.
"""