# proje: Kullaniciya array olusturtmak.
# gelistirme: farkli tip arrayler de olusturulabilmeli

import numpy as np
def tam_kare(num):
    return int(num**0.5) ** 2 == num    #-> Tam kare sorgusu

while True:
    try:
        x = int(input("\nLutfen Tam Kare bir deger giriniz: "))
        if x < 0:
            print("# Negatif Degerler Tam Kare olamaz!")
            continue
        
        if x > 195:
            print("# Daha Kucuk bir deger girmeyi deneyiniz.")
            continue

        elif tam_kare(x):
            break

        else:
            print("# Lutfen Tam Kare bir sayi giriniz!\n")

    except ValueError:
        print("# Lutfen Sayisal bir Deger Giriniz!\n")
        continue


n = int(x**0.5)  #-> Karekok alma islemi
array = np.arange(1, (x+1)).reshape(n,n)
print("\n", array, "\n")

while True:
    try:
        opsiyon = int(input("Herhangi bir Satir veya Sutunun Tamamini\nGoruntulemek istiyorsaniz: 1\n\nVerdiginiz indexteki degeri\nGoruntulemek istiyorsaniz: 2\n\nSecim: "))
        if 0 < opsiyon < 3:
            break
        else:
            print("# Gecerli bir secim yapiniz.")
            
    except ValueError:
        print("# Lutfen Sayisal bir Deger Giriniz!\n")

while opsiyon == 1:
    secim = input("\nSatir secmek icin: C\nSutun secmek icin: S\nSecim: ").upper()

    if secim == "C":
        try:
            satir_secim = int(input("\nToplam Satir sayisi: {}\nKacinci satiri goruntulemek istiyorsunuz: ".format(n)))
            
            if 1 <= satir_secim <= n:
                print(array[satir_secim-1, :])
                break
        except ValueError:
            print("# Sayisal bir deger Girmelisiniz!")
        
        else:
            print("# Lutfen Gecerli bir satir degeri giriniz!\n")


    if secim == "S":
        print("Sutun secenegini sectiniz")
        try:
            sutun_secim = int(input("\nKacinci sutunu goruntulemek istiyorsunuz: "))
            
            if 1 <= sutun_secim <= n:
                print(array[:, sutun_secim-1])
                break
        except ValueError:
            print("# Sayisal bir deger Girmelisiniz!")

        else:
            print("# Lutfen Gecerli bir sutun degeri giriniz!\n")


while opsiyon == 2:
    try:
        secim_c = int(input("\nGoruntulemek istediginiz Satiri Giriniz: "))
        secim_s = int(input("Goruntulemek istediginiz Sutunu Giriniz: "))

        if 1 <= secim_c <= n and 1 <= secim_s <= n:
            print(array[secim_c-1, secim_s-1])
            break
        else:
            print("# Lutfen Gecerli bir deger Giriniz!")
    
    except ValueError:
        print("# Sayisal bir Deger Girmelisiniz!")