    #FONKSİYONLAR (Functions)   Kodun devaminda da kullanacaksan sonradan da cagirabilirsin.

# def <fonksiyon_ismi>(<argümanlar>): # snake_case

"""
 Bu kod ne ise yarar?                # docstring    -> Kodu okuyanin daha rahat anlamasi icin kullanilabilir.
"""

#...                                  # return/print farklari

"""
# def (print)
def bes_bastir():
    print("5")      # 5
#bes_bastir()


# def (return)
def bes_dondur():
    return 5
#print(bes_dondur())


a = bes_bastir()
print(a)        # Def'i print ile yazdimiz icin "None" output'u verecek.

b = bes_dondur()
print(b)        # Def'i return ile yazdigimiz icin "5" output'u verecek.

"""
#def sayi_dondur(sayi):
    #return sayi
#print(sayi_dondur(37))

"""

def sayi_dondur(sayi=250):
    return sayi
print(sayi_dondur(89))      #-> 89 ciktisini verecek.


def sayi_dondur(sayi=250):
    return sayi
print(sayi_dondur())        #-> Arguman vermeden cagirdigimiz icin Default olani(250) verecek.
"""

"""
def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b
print(buyuk_sayi_dondur(5,10))
"""


 # Hatali Kullanim   
#def buyuk_sayi_dondur(a,b):
    #return a
    #return b           # Sart vermeden 2 tane Return kullandigimiz icin kod ilk gordugunu calistiracak-> a yani 5'i dondurecek
    #if a>b:
        #return a
    #elif b>a:
        #return b
#print(buyuk_sayi_dondur(5,10))



#def KacYasindasin(yas):
    #print("Ben ", yas, " yasimdayim.")
#KacYasindasin(15)  #-> Ben  15  yasimdayim.



"""
def metin_yazdir(a,b):
    buyuk_sayi = buyuk_sayi_dondur(a,b)
    sablon_metin = "{} daha büyük sayidir.".format(buyuk_sayi)
    print(sablon_metin)
print(metin_yazdir(5,10))
"""


"""
"Gokce Gun".split()
def isim_soyisim_ayirma(isim_soyisim):
    isim = isim_soyisim.split()[0]
    soyisim = isim_soyisim.split()[1]
    return isim, soyisim
print(isim_soyisim_ayirma("Gokce Gun"))


a, b = isim_soyisim_ayirma("Gokce Gun")
print (a)
print (b)
"""



#print("-".join(["Gokce", "Gun"]))      #-> " " icine yazdigimiz degeri argumanların arasina atar. -> Gokce-Gun

#def isim_soyisim_birlestir(isim, soyisim):
    #return " ".join([isim, soyisim])
#print(isim_soyisim_birlestir("Turgay", "Kara"))



# 2'den Fazla eleman icin en pratik yol Asagidaki gibi ugrasmak yerine Args kullanmakatir.
#def isim_soyisim_birlestir(isim, ikinciisim, soyisim):
    #return " ".join([isim, ikinciisim, soyisim])
#print(isim_soyisim_birlestir("Erol", "Mesut", "Gün"))



# ARGS  -> 
#def isim_soyisim_birlestir(*args):
    #return " ".join(args)
#print(isim_soyisim_birlestir("Erol","Mesut","Gün"))


#def isim_soyisim_birlestir(*args):
    #for item in args:
        #print(item)         #-> args icindeki her bir item'ı yazdir.
    #return " ".join(args)
#print(isim_soyisim_birlestir("Erol","Mesut","Gün"))


"""
# KWARGS
def gobek_adi_yazdir(**kwargs):
    if 'gobekadi' in kwargs:
        print(kwargs['gobekadi'])
    else:
        print("Gobekadi Yok")

print(gobek_adi_yazdir(adi = "Erol", soyadi="Gün", gobekadi="Mesut"))	#-> Gobek adini cekip yazdiracaktir. Eger gobekadi diye bir elemanimiz olmasaydi,
"""                                                         		#-> Else degeri donecekti.