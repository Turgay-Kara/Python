    #PRİNT
#print('Merhaba Dünya')

#print('Türkiye'nin en kalabalık şehri istanbuldur.')
#-> Sağ taraf string olarak algılanmadı.
#-> Bunu düzeltmek için ters slash(\) koyarız.
#print('Türkiye\'nin en kalabalık şehri istanbuldur.')

#-> ya da 3 tırnaktan yararlanabiliriz.
#3 tırnak ile istediğimiz kadar boşluk bırakabilir ve ya " tırnak koyabiliriz.
#print("""Türkiye'nin en kalabalık şehri istanbuldur.""")

#print("""T
#u
#r
#g
#a
#y""")


#print("Turgay\nAdamdır.")   #-> \n paragraf anlamına gelir yani \n'den sonra bir alt satıra geçer.
#print("Turgay\tAdamdır.")   #-> \t bir TAB boşluk bırakmak için kullanılır.


#print("Hello", end="-")
#print("World")


#print("Turgay", "Kara",sep="-",end="123")     #-> sep"" arasına yazılan değeri kelimeler ARASINA koyar.
                                               #-> end"" arasına yazılan değeri cümlenin SONUNA koyar.


#-> Bu şekilde değişkenlerin yerlerini değiştirebiliriz.
#sayi1=10
#sayi2=20
#sayi1, sayi2=sayi2, sayi1
#print(sayi2)


#x = 'Bu bir değişken denemesi.' 
#print(x)


#x=30
#y=70
#print(x+y) #-> 100



#print(10*'Turgay ')
#print(7)
#print(4*3)

#print("Ben " + str(16) + " yaşımdayım.")    #-> Hem int hem str kullanılmaz. Bu yüzden sayıyı str yaptık.