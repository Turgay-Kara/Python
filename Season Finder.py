ay = input("Lütfen bir ay giriniz.\n")
ay = ay.replace("İ","i")
ay = ay.replace("I","ı")
ay = ay.lower()

if ay =="aralık" or ay =="ocak" or ay =="şubat":
    print("Kış mevsimindesiniz.")
elif ay == "mart" or ay =="nisan" or ay =="mayıs":
    print("İlkbahar mevsimindesiniz.")
elif ay == "haziran" or ay =="temmuz" or ay =="ağustos":
    print("Yaz mevsimindesiniz.")
elif ay == "eylül" or ay =="ekim" or ay =="kasım":
    print("Sonbahar mevsimindesiniz.")
else:
    print("Lütfen bir ay giriniz.")
