"""
        #MOTIVATION
"""  

#   Arac Satis
#   Aksiyon-1: Satis olmayan zamanlarda indirim yap.
#       ilan suresi 1 hafta oldugundan ilan verenler arac fiyatlarini git gide dusurecektir.
#   Aksiyon-2: Kullanicilari urune yonlendir ve bunu veri ile destekle.

#       Arac fiyati = (80.000) - (0,2*60.000) - (2500*HasarDurumu) + ... + (6.000*VitesTuru)


#   Asama asama Katma Degerler:
#   1-Betimleyici Analitik     2-Teshis/Tani Analitigi     3-Tahminsel Analitik    4-Yonergeli Analitik
#         Ne olmus?                 Neden olmus?                Ne olacak?        Ne olmali, Nasil olmali?


#   Deployement: 2. El ilan sitesini Canli sisteme entegre etme isi.



"""
        # VERI OKURYAZARLIGI
"""

#   Degisken: Birimden birime farkli deger alan nicelik

#       Degisken Turleri:
#   Sayisal Degiskenler (nicel, kantitatif)     -> ornek: boy, kilo, yas, hava sicakligi
#   Kategorik Degiskenler (nitel, kalitatif)    -> ornek: cinsiyet, vites turu, model, rutbeler


#       Olcek Turleri: ()ornekler

#   Sayisal Degiskenler   icin: Aralik(- de olabilir) ve Oran(0 = baslangic noktasi)
#   Kategorik Degiskenler icin: Nominal(verilerin siniflari arasinda fark yok.) ve Ordinal(verilerin siniflari arasinda fark var.) 

#       Aralik ornek    : Hava sicakligi        Nominal ornek: Cinsiyet
#       Kategorik ornek : Arac Fiyati           Ordinal ornek: Rutbeler, Egitim durumu


#   Medyan:      Kucukten buyuge dogru siralandiginde ortada kalan eleman.

#   Mod:         En cok tekrar eden deger.

#   Kartiller:   Kucukten buyuge siralandiginda seriyi 4 parcaya ayiran degerler. (.png)

#   Aciklik:     Maximum - Minimum deger

#   Stdrt Sapma: Verilerin ortalamasini bul. Elemanlari tek tek ortalamadan cikarip sonucun karesini al.
#                Buldugun sonuclari topla ve eleman sayisina bol. Sonucun kokunu al.

#   Varyans:     Standart sapmanin karesine  esittir.

#   Negatif Carpik: Tepe noktasi saga yatkindir
#   Pozitif Carpik: Tepe noktasi sola yatkindir.

#   Carpiklik Katsayisi = 3(x ort - medyan) / (standart sapma)  (.png)
#       CK > 0 -> Pozitif Carpik
#       CK < 0 -> Negatif Carpik
#       CK = 0 -> Simetrik

#   Basiklik:    Dagilimin sivri mi, basik mi oldgunu ifade eder.

#   Basiklik Katsayisi = m4 / s^^4  (.png)  # BK = (terimler - ortalama)^^4  / (toplam veri sayisi)
#       BK > 3 -> sivri
#       BK = 3 -> 
#       BK < 3 -> basik  
#
#
#
#   Herhangi bir bakkal defterinde saat 12.00 - 15.00 araligindaki satislari ele alirsak:
#   Bu satisten elde edilen kazanc yuksek ise bu bakkalin is yerlerine yakin bir konumda
#   oldugu varsayimini yapabiliriz.


"""
        PYTHON PROGRAMLAMA
"""



"""
        VERI MANIPULASYONU (NumPy & Pandas)
"""

# NumPy -> Bilimsel islemler icin kullanilir.
import numpy as np  #-> Bu her zaman calisir durumda olmali.

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