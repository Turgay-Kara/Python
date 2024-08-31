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