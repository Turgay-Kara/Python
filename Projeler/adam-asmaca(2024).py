import random

alfabe = ["a", "b", "c", "d", "e", "f", "g", "h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
kelimeler = ["at", "piyano", "tabanca", "bilgisayar"]
tahmin_edilen_harfler = []

print("\n>> Adam Asmaca Oyununa Hoş Geldin! <<")
print("Kelimenin tamamini tahmin etmek istiyorsaniz 'kelime' yazin.")
secilen = random.choice(kelimeler)
yanlis_tahmin_sayisi = 0

sonuc = ['_' for _ in secilen]
print(sonuc)


while yanlis_tahmin_sayisi <= 7:
    tahmin = input("Herhangi bir harf giriniz: ").lower()
    
    if tahmin == "kelime":
        kelime_tahmini = input("Kelimenin tamamini tahmin et: ").lower()
        if kelime_tahmini == secilen:
            print("\nTebrikler, doğru kelimeyi tahmin ettiniz!")
            print("Doğru Kelime: ", secilen)
            break

        else:
            print("\nOyunu Kaybettiniz! Doğru Kelime: ", secilen)
            break

    elif tahmin not in alfabe or len(tahmin) != 1:
        print("Lütfen geçerli bir harf giriniz!\n")
    
    elif tahmin in tahmin_edilen_harfler:
        print("\nAyni harfi birden fazla kez tahmin edemezsin!")
        print("Tahmin edilen harfler: ", tahmin_edilen_harfler, "\n")

    else:
        tahmin_edilen_harfler.append(tahmin)

        if tahmin in secilen:
            print("Doğru tahmin!\n")
            for i, harf in enumerate(secilen):
                if harf == tahmin:
                    sonuc[i] = harf
            print(sonuc)
            
            if "_" not in sonuc:
                print("\nTebrikler, oyunu kazandiniz!")
                print("Doğru Kelime: ", secilen)
                break
        else:
            print("Yanliş tahmin!\n")
            print(sonuc)
            yanlis_tahmin_sayisi += 1
            
            if yanlis_tahmin_sayisi == 7:
                print("\nOyunu kaybettiniz! Doğru Kelime: ", secilen)
                break