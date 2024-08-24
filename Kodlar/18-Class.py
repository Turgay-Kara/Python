"""
    # CLASS: Benzer ozellikler, ortak amaclar tasiyan gruplar olusturmak icin kullanilir.

#class VeriBilimci():
    #print("Bu bir siniftir")

class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
#print(VeriBilimci.sql)      #-> Sinif ozelliklerine erismek.


#VeriBilimci.sql = "hayir"   #-> Sinif ozelliklerini degistirmek
#print(VeriBilimci.sql)


ali = VeriBilimci()          #-> Sinif orneklendirmesi #-> alinin ozellikleri VeriBilimci class'inin ozelliklerini tasir. 
#print(ali.sql)
#print(ali.deneyim_yili)

ali.bildigi_diller.append("Python")     #-> Alinin bildigi dillere Python'i ekledik.

#veli = VeriBilimci()
#print(veli.bildigi_diller)   #-> Alinin diline ekledigimiz icin sonradan sinifa eklenen tum kullanicilara Python'i ekledi.
                              #-> bu sorunu cozmek icin:

class VeriBilimci():
    bolum = ""
    sql = ""
    deneyim_yili = 5
    bildigi_diller = ["R", "Python"]    #-> VeriBilimci sinifinin bildigi dillere ekleme yaptik.
    def __init__(self):
        self.bildigi_diller = []        #-> Her elemanin kendi icinde degisebilen ozelliklerden olusacak.
        self.bolum = ""

veli = VeriBilimci()
#print(veli.bildigi_diller)
veli.bildigi_diller.append("R")
#print(veli.bildigi_diller)


turgay = VeriBilimci()
turgay.bildigi_diller.append("Python")
turgay.bildigi_diller.append("R")
turgay.bolum = ("Data Hunter")
#print(turgay.bildigi_diller)

#print(VeriBilimci.bildigi_diller) 


ali.bolum = "istatistik"
print(ali.bolum)
print(turgay.bolum)
print(VeriBilimci.bolum)
"""


"""
class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)     #-> Dil ekleme islemini fonksiyon kullanarak otomatik hale getirdik.


#print(dir(VeriBilimci))     #-> Class nesnesinin erisilebilecek olan degerlerini getirir.
#VeriBilimci.dil_ekle("R")   #-> Hata

duru = VeriBilimci()
duru.dil_ekle("R")
print(duru.bildigi_diller)

turgay = VeriBilimci()
turgay.dil_ekle("Python")
print(turgay.bildigi_diller)
"""


"""
    # MIRAS YAPILARI: Daha onceden yapilmis hazir Classlar'i kullanmak.

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""

class DataScience(Employees):       #-> Miras (Employees)
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
#veribilimci1.


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.
"""


"""
turgay = Employees()
class Employees_yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.Firstname = FirstName
        self.Lastname = LastName
        self.Adress = Adress

turgay = Employees_yeni("a", "b", "c")
print(turgay.Adress)    #-> Output: c
"""    # CLASS: Benzer ozellikler, ortak amaclar tasiyan gruplar olusturmak icin kullanilir.

#class VeriBilimci():
    #print("Bu bir siniftir")

class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
#print(VeriBilimci.sql)      #-> Sinif ozelliklerine erismek.


#VeriBilimci.sql = "hayir"   #-> Sinif ozelliklerini degistirmek
#print(VeriBilimci.sql)


ali = VeriBilimci()          #-> Sinif orneklendirmesi #-> alinin ozellikleri VeriBilimci class'inin ozelliklerini tasir. 
#print(ali.sql)
#print(ali.deneyim_yili)

ali.bildigi_diller.append("Python")     #-> Alinin bildigi dillere Python'i ekledik.

#veli = VeriBilimci()
#print(veli.bildigi_diller)   #-> Alinin diline ekledigimiz icin sonradan sinifa eklenen tum kullanicilara Python'i ekledi.
                              #-> bu sorunu cozmek icin:
"""
class VeriBilimci():
    bolum = ""
    sql = ""
    deneyim_yili = 5
    bildigi_diller = ["R", "Python"]    #-> VeriBilimci sinifinin bildigi dillere ekleme yaptik.
    def __init__(self):
        self.bildigi_diller = []        #-> Her elemanin kendi icinde degisebilen ozelliklerden olusacak.
        self.bolum = ""

veli = VeriBilimci()
#print(veli.bildigi_diller)
veli.bildigi_diller.append("R")
#print(veli.bildigi_diller)


turgay = VeriBilimci()
turgay.bildigi_diller.append("Python")
turgay.bildigi_diller.append("R")
turgay.bolum = ("Data Hunter")
#print(turgay.bildigi_diller)

#print(VeriBilimci.bildigi_diller) 


ali.bolum = "istatistik"
print(ali.bolum)
print(turgay.bolum)
print(VeriBilimci.bolum)
"""


"""
class VeriBilimci():         #-> VeriBilimci sinifina bazi ozellikler tanimladik.
    bolum = ""
    sql = "evet"
    deneyim_yili = 0
    bildigi_diller = []
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ""
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)     #-> Dil ekleme islemini fonksiyon kullanarak otomatik hale getirdik.


#print(dir(VeriBilimci))     #-> Class nesnesinin erisilebilecek olan degerlerini getirir.
#VeriBilimci.dil_ekle("R")   #-> Hata

duru = VeriBilimci()
duru.dil_ekle("R")
print(duru.bildigi_diller)

turgay = VeriBilimci()
turgay.dil_ekle("Python")
print(turgay.bildigi_diller)
"""


"""
    # MIRAS YAPILARI: Daha onceden yapilmis hazir Classlar'i kullanmak.

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Adress = ""

class DataScience(Employees):       #-> Miras (Employees)
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()
#veribilimci1.


class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()
#mar1.
"""


"""
turgay = Employees()
class Employees_yeni():
    def __init__(self, FirstName, LastName, Adress):
        self.Firstname = FirstName
        self.Lastname = LastName
        self.Adress = Adress

turgay = Employees_yeni("a", "b", "c")
print(turgay.Adress)    #-> Output: c
"""