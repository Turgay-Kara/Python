"""
 #IF-ELIF-ELSE KOMUTU
KatedilenMesafe = input("Ne kadar mesafe kat ettiniz?\n")
KalanMesafe = input("Ne kadar mesafeniz kaldi?\n")
if KatedilenMesafe > KalanMesafe:  #-> Bir koşulu kontrol etmek için if kullanilir ve sonuna : koyulur.
    print("Yolun yarisini geçtiniz.")
elif KatedilenMesafe < KalanMesafe:#-> Eğer 'if' komutundaki değer yanliş ise çalişacak komut elif tir.
    print("Yolun yarisini geçmediniz.")
else:                              #-> Eğer 2 koşul da çalişmazsa devreye else girer.
    print("Yolun yarisindasiniz.")
"""
#
"""
kullanici_adi = "TurgayKara"
sifre = "12345"

ad = input("Kullanici Adinizi giriniz : ")
sifre_gir = input("Şifrenizi giriniz : ")

if ad == kullanici_adi and sifre == sifre_gir:
    print("Sisteme başariyla giriş yaptiniz.")
elif kullanici_adi != ad:
    print("Kullanici adinizi yanliş girdiniz.")
else:
    print("Şifrenizi yanliş girdiniz.")
"""
#
"""
result = input("Başvuru Sonucunu Giriniz : ")
if "olumlu" in result.lower():
    print("İşe alindiniz!")
elif "olumsuz" in result.lower():
    print("İşe alinmadiniz!")
else:
    print("Lütfen geçerli bir değer giriniz!")
"""
#
"""
print("Merhaba, bu program sayinizin 50'den >, < ya da = olduğunu söyler. :)")
number = int(input("Sayi giriniz: "))
if (number == 50):
    print("Sayi 50.")
elif (number < 50):
    print("Sayi 50'den küçük.")
else:
    print("Sayi 50'den büyük.")
"""
#
"""
gender = input("Cinsiyet bilginizi giriniz (E/K): ")
if gender.upper() == "E":
    BirtOfDate = int(input("Doğum yilinizi giriniz: "))

    if 2020 - BirtOfDate == 20 or 2020 - BirtOfDate > 20 and 2020 - BirtOfDate <= 28:
        print("Askere gidebilirsiniz.")
    elif 2020 - BirtOfDate != 20:
        print("Askere gidemezsiniz.")
    else:
        print("Yaşiniz hesaplanamadi.")
elif gender.upper() == "K":
    print("Kadinlar askere alinamiyor.")
else:
    print("Lütfen bir cinsiyet giriniz.")
"""


"""
havadurumu = input("\n1-Gunesli\n2-Karli\n3-Yagmurlu\n4-Bulutlu\n\nHava nasil:")

if havadurumu == "1":
    print("Take sunglass.")

elif havadurumu == "2":
    print("Wear boats.")

elif havadurumu == "3":
    print("Take umbrella")

else:
    print("it's okay. You can go outside.")
"""
#

"""
list = ["0","1", "2","3","4","5"]
while True:
    hedefrakam = input("bir rakam giriniz:")

    if hedefrakam in list:
        print("\nistediginiz rakam listede bulunuyor.")


    else:
        print("\nistediginiz rakam listede bulunmuyor.\nSenin için bu rakami da listeye ekleyecegim.")

        list.append(hedefrakam)
        print("\niste, güncel liste!")
        print(list)
        
        if len(list) == 10:
            print("Tum rakamlari girdiniz. Program sonlandiriliyor.\n")
            break
"""