    #LIST
#List (list) #-> Liste. Birden fazla data tipi depolama
#sayilar = [1,2,3,9]
#print(type(sayilar))    #-> 'list'
#print(sayilar)


    #LISTE METOTLARI
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#print(hayvanlar)



  #.append() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#hayvanlar.append("Panda")   #-> .append() -> Listeye yeni eleman ekler.
#print(hayvanlar)



  #.remove() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#hayvanlar.remove("Kedi")  #-> .remove() -> Listeden istenilen elemani çikartir.
#print(hayvanlar)



  #.pop() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#hayvanlar.pop(2)             #-> .pop() -> Listeden istenilen elemani çikartir.
#print(hayvanlar)             #-> () Boş birakilirsa son elemani çikartir.



  #.copy() METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#hayvanlar2 = hayvanlar.copy()      #-> Aktarilacak liste = kopyalanacak liste.copy()
#print(hayvanlar2)



  #.extend() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#a.extend(b)             #-> a listesini ve b listesini birleştir.
#print(a)



  #.sort() METOTU
#a = [1, 2, 3]
#b = [5, 8, 4, 12, 10]
#b.sort()                #-> .sort() Listedeki elemanlari siralamamiza yarar.
#print(b)                #-> Büyükten küçüğe siralar.

#b.sort(reverse = True)  #-> reverse tersine çevirir.
#print(b)                #-> Küçükten büyüğe siralar.

#.sort Sadece sayilari değil kelimeleri de siralayabilir;
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#hayvanlar.sort(reverse = True)
#print(hayvanlar)         #-> hayvanlar listesini tersten(reverse) siralar


  #max-min() fonksiyonu
#x = [1,2,3,4,5,10,50]
#print(max(x))   #-> Listedeki en büyük sayiyi gösterir.
#print(min(x))   #-> Listedeki en küçük sayiyi gösterir.


  #.count() METOTU
#x = [5, 8, 4, 12, 10, 4]
#print(x.count(4))   #-> .count() Istenilen elemanin kaç tane olduğunu söyler.



  #.index() METOTU
#y = [5, 8, 4, 12, 10]
#print(y.index(5))   #-> .index() Belirtilenn elemanin kaçinci indexte olduğunu söyler.



  #.insert() METOTU
#b = [5, 8, 4, 12, 10]
#b.insert(1, "TURGAY")  #-> .insert() Belirtilen indexe istenilen elemani ekler.(Belirtilen indexi silmez.)
#print(b)               #-> 1.index'e "TURGAY" elemanini ekle.



  #.clear() METOTU
#a = [1, 2, 3]
#a.clear()       #-> İstenilen listedeki tüm elemanlari siler(.clear).
#print(a)



  #slicing[] METOTU
#hayvanlar = ["At", "Köpek", "Kedi", "Balik", "Timsah"]
#print(hayvanlar)
#print(hayvanlar[2:4])  #-> 2. ve 4. Elemanlarin arasindaki elemanlari print eder. 2. eleman dahil, 4. eleman dahil DEĞİL.
#print(hayvanlar[:3])    #-> [:3] sayi sağa yazilirsa 3. Elemana kadar print eder. 3. eleman dahil DEĞİL. #slicing metotunda [x:y] y hiçbir zaman dahil edilmez.
#print(hayvanlar[3:])    #-> [3:] sayi sola yazilirsa 3. Elemandan sonraki elemanlari print eder. 3. eleman da dahil.
#print(hayvanlar[0:5:3]) #-> [x:y:z] -> z = Kaç karakter araliklarla gideceğini söyler.
#--> 0.Karakterden 3.Karakter dahil olmamak üzere 2şer araliklarla(2.dahil) print et. <--#

#hayvanlar[3] = "Ari"   #-> Listenin 3.elemani yerine istenilen elemani koy.
#print(hayvanlar)



    # SPLIT -> Listedeki elemanlari 2ye böler
#yorumbirakanlar = ["Talha Kara", "Turgay Kara", "Eşref", "Ayfer", "Engin"]
#ad, soyad = yorumbirakanlar[1].split()[0], yorumbirakanlar[1].split()[1]   #-> listedeki 1.elemanin 0. parçasi + 1.elemanin 1.parçasi
#print(ad)
#print(soyad)



#insanlar = [["Turgay", "Kara"], ["Talha", "Beyaz"], ["Eşref", "Siyah"]]
#print(insanlar[0])    #-> Turgay, Kara
#print(insanlar[0][1]) #-> Kara
#print(insanlar[2][0]) #-> Eşref
#print(len(insanlar))  #-> len -> Listenin kaç elemandan oluştuğunu söyler -> 3

#x = "Turgay"
#text = (len(x))
#print(text)