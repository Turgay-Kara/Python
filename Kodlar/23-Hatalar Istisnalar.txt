    # Hatalar & Istisnalar

"""
a = 10
b = 0
#print(a/b)     #-> Payda 0 olamaz. #ZeroDivisionError: division by zero

try:
    print(a/b)      #-> a/b ifadisini calistirmayi dene eger calismaz ise,
except ZeroDivisionError:       #-> "ZeroDivisionError" hata tipini istisna olarak gor ve print ifadesini dondur.
    print("Payda 0 degerinde olamaz!")


a = 10
b = "2"
#print(a/b)      #-> Str ifade ile Int bir ifade Matematiksel olarak calistirilamaz. #Type Error

try:
    print(a/b)
except TypeError:       #-> except: Gormezden gelme metotu
    print("Str ifade ile Int bir ifade Matematiksel olarak calistirilamaz")
"""