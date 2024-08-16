# Wilson Asali Hesaplama

import math

def asal_mi(deger):
    x = deger - 1

    if deger < 2:
        return False

    while x > 1:
        if deger % x == 0:
            return False
        x -= 1

    return True
    
deger = int(input("Wilson Asali olup olmadigini kontrol etmek istediginiz Sayiyi giriniz: "))
if asal_mi(deger):
    P = deger
    faktoriyel_sonuc = math.factorial(P - 1)

    wilson_kontrol = (faktoriyel_sonuc + 1) / (P * P)
    if wilson_kontrol.is_integer():
        print("{} sayisi bir Wilson Asalidir!".format(deger)) 
    else:
        print("{} sayisi Asal bir sayidir Ancak Wilson Asali degildir!".format(deger))

else:
    print("{} sayisi Asal olmadigindan dolayi Wilson Asalinin ilk kuralina uymaz.".format(deger))