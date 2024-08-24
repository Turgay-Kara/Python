    #KÜMELER(Sets)
 #-> Süslü parantez kullanilir. {}, #-> Farkli elemanlardan oluşan bir veri tipi, Ayni elemani 1'den fazla basmaz.
#sayi = {1, 3, 3, 34, 543, 5324, 5, 43}
#print(sayi)     #-> 2tane 3 yazmamiza rağmen 1 tanesini gösterir.


#sayi.add(100)       #-> Eleman eklemek için kullanilir.
#print(sayi)


#sayi.discard(3)     #-> Istenilen elemani çikartamk için kullanilir.
#print(sayi)


#sayi.remove(34)     #-> Yine eleman çikartmak için kullanilir ama () içi boş birakilirsa hata verir.
#print(sayi)


#yeni_sayi = {32, 3, 25, 432, 4, 325, 4}
#sayi.update(yeni_sayi)     #-> Kümeleri birleştirdik.
#print(sayi)

"""
a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print(a.difference(b))      #-> a ve b kümelerindeki farklari gösterir. -> 1, 2, 3
print(a.intersection(b))    #-> istenilen kümelerdeki kesişen elemanlari gösterir. -> 4
print(a.union(b))           #-> istenilen kümeleri birleştirerek tek bir küme haline getirir. Kesişen elemanlar varsa 1 kere geçirir. -> 1, 2, 3, 4, 5, 6, 7
print(len(a))               #-> istenilen kümedeki eleman sayisini gösterir.
"""