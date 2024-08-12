    # RANGE
#print(list(range(10)))  #-> 0'dan 9'a kadar list şeklinde yaz.
#([*range(10)])      #-> Aynı şey daha pratik.
#print([*range(1,10,2)])     #-> 1den başlayarak 9'a kadar ikişer sayarak git.

#for sayi in range(10):      #-> 0'dan 9'a kadar say.
    #print(sayi)

#for sayi in range(10):      #-> sayi 5'ten büyük oldugu sürece 9'a kadar say.
    #if sayi > 5:
        #print(sayi)



    # ENUMERATE
#words = ["a","b","c","d","e"]
#for word in enumerate(words):   #-> enumerate kodu direkt olarak sıralamanıza yarar.
    #print(word)                 #(0, 'a')

#words = ["a","b","c","d","e"]
#for index, harf in enumerate(words):
    #print(index)                        #-> Sadece index'i(sırayı) yaz.

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
    #print(ulke)                             #-> listlerin len(eleman sayisi) birbirine eşit olmasi lazim.