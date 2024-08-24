    #SÖZLÜKLER(Dictionary)(dict)
 #Anahtar ve değerlerden oluşan bir çok elemani içerisinde bulunduran veri tipi
"""
kimlik = {
        "isim":"Turgay",
        "soyisim":"Kara",
        "TC_NO":12367845689,
        "yer":["Kastamonu", "Merkez"],
        "bilgiler":{"email":"adsfs@gmail.com",
                    "kardeşi sayisi":2
                    }
        }
kimlik["yil"] = 2005    #-> Kimliğin içine yil ekledik.

print(kimlik["isim"])
print(kimlik["yil"])
print(kimlik)
print(len(kimlik))  #-> Eleman sayisini gösterir. -> 4

print(kimlik.keys())       #-> Sözlükteki anahtarlari gösterir.
print(kimlik.values())     #-> Sözlükteki değerleri gösterir.
print(kimlik.items())      #-> Anahtalaari ve Değerleri yanyana gösterir.
print(kimlik.get("yer"))   #-> İstenilen anahtarin değerini gösterir.
print(kimlik.update({"Anne_adi":"Ayfer"}))  #-> Listeye yeni Anahtar(key) ve Değer(value) ekledik.
print(kimlik.copy())       #-> Kimliği kopyalar.
kimlik.pop("isim")         #-> Sözlükten istenilen değeri çikarir.
kimlik.clear()             #-> Sözlükteki tüm elemanlari siler.
print(kimlik)
"""

    #.get() METOTU
"""
ing_sözlük = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamini öğrenmek istediğiniz kelimeyi yaziniz: ")
print(ing_sözlük.get(sorgu, "Bu kelime veritabanimizda yoktur!"))
#->Birinci argüman sorgulamak istediğimiz sözlük öğesidir.
#->İkinci argüman ise bu öğenin sözlükte bulunmadiği durumda kullaniciya hangi mesajin gösterileceğini belirtir.
"""

#

"""
soru = input("Şehrinizin adini tamami küçük harf olacak şekilde yazin: ")
if soru == "istanbul":
    print("gök gürültülü ve sağanak yağişli")
elif soru == "ankara":
    print("açik ve güneşli")
elif soru == "izmir":
    print("bulutlu")
else:
    print("Bu şehre ilişkin havadurumu bilgisi bulunmamaktadir.")
"""
#Bunun yerine .get() metotunu kullanabiliriz.
"""
soru = input("Şehrinizin adini tamami küçük harf olacak şekilde yazin: ")
cevap = {"istanbul": "gök gürültülü ve sağanak yağişli",
         "ankara": "açik ve güneşli", "izmir": "bulutlu"}
print(cevap.get(soru, "Bu şehre ilişkin havadurumu bilgisi bulunmamaktadir."))
"""