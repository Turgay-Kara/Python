isim = input("Adınız nedir?\n")
print("Sisteme başarıyla giriş yaptınız.\nMerhaba " + isim + ", Hoşgeldin\nOynamaya başlamadan önce lütfen !kurallar yazarak kuralları okuyunuz.")
print("\n" + isim + " Sisteme giriş yaptı. ")

print("""\nKuralları görmek istiyorsanız !kurallar yazmanız,
Silah deseninizi değiştirmek istiyorsanız !ws yazmanız,
Grubumuza katılmak istiyorsanız !grup yazmanız yeterli olacaktır.
Çıkış yapmak için q tuşuna basın.\n""")
while True:
    secim = input("")
    if secim == "!kurallar":
        print("\nKurallar:\nHile Kullanmak, Küfür etmek ve Argo kelime kullanmak Yasaktır.!!\n")
        
    if secim == "!ws":
        print("\nDesen:\nDesenini değiştirmek istediğiniz silahın türünü seçiniz.\n")

    if secim == "!grup":
        print("\nGrup:\nGrubumuza başarıyla katıldınız.\nTK ailesi iyi oyunlar diler. :)\n")
        
    if secim == "q":
        break
