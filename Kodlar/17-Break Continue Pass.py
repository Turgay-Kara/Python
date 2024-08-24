    # BREAK
#harfler = ["a", "b", "c", "d", "e"] * 1000
#for index, harf in enumerate(harfler):
    #if harf == "c":
        #print("{} harfi {}. indexte!".format(harf, index))      #-> c harfinin kacinci indexte olduğunu söyler.
        #break   #-> break komutu olmasaydı döngü 1000 kere tekrar edecekti ama istediğimizi elde ettigimiz anda cikmak istiyorsak "break" kullanabiliriz.



    # CONTINUE
#for sayi in range(1, 6):
    #if sayi%2 == 0: #-> cift sayi sorgulama mantigi sayi%2 -> sayinin 2'ye bolumunden kalan 0 ise...
        #continue    #-> continue oldugu icin islemi range'de verdigimiz son sayiya kadar devam ettirecek.
    #print(sayi)     #-> tek olanlari yazdi cunku eğer sayi 2'ye bolunuyorsa devam etmesini soyledik.



    # PASS
#for sayi in range(1, 6):
    #if sayi%2 == 0:
        #pass            #-> bu sekilde bir durum gorursen burayı atla.
    #else:
        #print(sayi)     #-> cift olma durumunu atladigimiz icin tek olanlari yazdirdik.


#for sayi in range(1, 6):
    #if sayi%2 != 0:     #-> Kalan 0'a esit degil ise...
        #pass            #-> bu sekilde bir durum gorursen burayı atla. (Tek olan sayilari atla)
    #else:
        #print(sayi)     #-> Tek olanlari atladigimiz icin cift olanlari yazdirdik.


#for sayi in range(1,10):
    #if sayi < 5:
        #pass            #-> pass komutunu kullanmasaydik bu kısımda hata alacaktık.
                        #-> buradaki satiri goze alma. Projemize sonradan ekleme yapacaksak ekleyebiliriz.
    #else:
        #print("Hey!")