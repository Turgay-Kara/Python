    #DEMETLER(Tuples)
 #Listelere benzer ama değiştirilemez ve [] değil, () parantezlerle oluşturulur.

#zamirler  = ("ben", "sen", "o", "biz", "siz", "onlar") #-> Değişiklik yapılamaz.
#print(zamirler[3])     #-> 3. index'i verir. -> biz

#zamirler[0] = "bne"    #-> 0. elemanı yani "ben"i, "bne ile değiştirmeye çalıştık.
 #print(zamirler)       #-> Hata verir çünkü tuple elemanları değiştirilemez(yani eklenme veya çıkartma yapılamaz.!)


#Tek elemanlı bir tuple oluşturmak için:
#a = (5)
#print(a)    #-> 5 çıkar. Yani tuple oluşmadı.

#a = (4,)
#print(a)    #-> (4,) çıktı. Tek elemanlı tuple oluşturduk.


#Bir kaç tane demeti birleştirebiliriz:
#sayılar = (1, 2, 3, 4, 4)
#print(zamirler + sayılar)


#tuple'a bu şekilde de ekleme yapabiliriz:(üstteki daha pratik)
#tuple1=('Turgay', 'Kara')
#tuple1=tuple1+('udemy',)    #-> , olmazsa ERROR
#print(tuple1)

 #Tuple'dan, List'e dönüştürme
#list1 = [1,2,3]
#list2 = (1,2,3)
#list2 = list(list2)
#print(type(list2))

 #List'den Tuple'a dönüştürme
#list1 = tuple(list1)
#print(type(list1))


#print(zamirler[0:3])       #-> Tuple'larda indexleme işlemleri geçerlidir.

#print(len(zamirler))       #-> .len eleman uzunluğunu gösterir.

#print(sayılar.count(4))    #-> .count -> Istenilen elemanın kaç tane olduğunu söyler.

#print(sayılar.index(2))    #-> .index -> Istenilen elemanın kaçıncı indexte olduğunu gösterir.