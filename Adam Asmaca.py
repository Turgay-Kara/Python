import random
import sys #-> Oyun kazanılırsa oyundan atılmak için kullanılır.
from time import sleep #-> Kuralları anlatırken beklet(sırayla çıkart).

Kelime_Listesi = ["elma", "armut", "muz", "kivi", "kitap", "kalem", "defter", "silgi", "köpek", "kedi", "yılan", "kartal", "monitör", "klavye", "fare", "hoparlör"]
TahminEdilen_Kelime = []    #-> Oyunda tahmin edilen kelime her seferinde farklı olmasını istediğimiz için içi boş bir liste olacak. []
Gizli_Kelime = random.choice(Kelime_Listesi)
Kelime_Uzunluğu = len(Gizli_Kelime) #-> Kelimenin kaç harf olduğun görmek için kullandık. len Herhangi bir stringdeki karakter sayısını bize int olarak veren bir modül.
Alfabe = "abcdefghijklmnopqrstuvwxyz" #-> ! gibi işaretlerin kullanılmamasını istediğimiz için sadece alfabeyi yazdık.
Harf_Deposu = [] #-> Bir defa tahmin ettiğimiz harfi tekrar tahmin etmemek için kullandık. Tahmin edilen harfler Harf_Deposuna gider.

def kurallar():
    for karakter in Gizli_Kelime:
        TahminEdilen_Kelime.append("-") #->Gizli_Kelimeyi Hanelere böldük. Kelimedeki her harf yerine - koyar.
    print("Tahmin  etmemiz gereken kelimede ", Kelime_Uzunluğu, " Harf var.")
    sleep(1) #-> Kuralları 1 saniye arayla anlat.
    print("10 tahmin hakkınız var. ")
    print("10 seferde bilemezseniz oyunu kaybedersiniz!")
    print(TahminEdilen_Kelime)

def Kelime_TahminEtme():
    while True:
        Kelime_Tahmin = input("Tüm kelimeyi tahmin etmek ister  misiniz?\nYanlış tahmin ederseniz oyunu kaybedersiniz.\n")
        if Kelime_Tahmin == "evet":
            Kelime_TahminDeneme = input("Kelimeyi tahmin ediniz:\n")
            if Kelime_TahminDeneme == Gizli_Kelime:
                print("Tebrikler! Oyunu kazandınız.")
                sys.exit()
            else:
                print("Yanlış kelimeyi tahmin ettiniz! Oyun bitti\n")
                sleep(1)
                print("Gizli Kelime: ", Gizli_Kelime)
                sys.exit()
        elif(Kelime_Tahmin) == "hayır":
            print("Tamam, Oyuna devam edelim \n")
            break
        else:
            print("Lütfen evet veya hayır diye bir cevap veriniz.\n")
            continue #-> if komutunun en başına gelir.

def Harf_TahminEtme():
    TahminSayısı = 0

    while TahminSayısı < 10: #-> Oyuncu oyunu kaybetmemişken..
        Kelime_TahminEtme()
        Harf_Deneme = input("Bir harf deneyin.\n ")
        if not Harf_Deneme in Alfabe:   #-> Eğer Harf_Deneme albadede değil ise.
            print("Lütfen alfabeden bir karakter yazınız.\n ")
        elif Harf_Deneme in Harf_Deposu:
            print("Bu harfi zaten tahmin ettiniz.\n ")
        else:
            Harf_Deposu.append(Harf_Deneme) #-> .append Harf_Deneme, Harf_Deposu nda yoksa bu harfi Harf_Deposu na ekler.

        if Harf_Deneme in Gizli_Kelime:
            print("Doğru Tahmin!")
            for x in range(0, Kelime_Uzunluğu):   #-> for loop'u Gizli_Kelimemiz içinde Kelime_Uzunluğu kadar gidip gelicek  #-> for loopu belirli bir sayıda tekrar yapmak iin kullanılır.
                if Gizli_Kelime[x] == Harf_Deneme:  #-> index method, [x]-> x index'i ->  for loop'unun Gizli_Kelimenin içinde gezerken bulduğu o kelimenin index'i
                    TahminEdilen_Kelime[x] = Harf_Deneme #-> Tahmin edilen kelimenin x'inci sıradaki(elementindei?) -'yi Harf_Deneme'sine değiştiriyoruz.
                    print(TahminEdilen_Kelime)
                if not "-" in TahminEdilen_Kelime: #-> Eğer oyuncunun son tahmini ise ve kelimeyi buldu ise. Listede - kalmamasını farkeden bir komut yazdık.
                    print("Tebrikler, Oyunu kazandınız!")
                    break
        else:
            print("Yanlış tahmin. Tekrar deneyin.\n")   #-> Eğer harfi yanlış tahmin ederse.
            TahminSayısı += 1   #-> Tahmin sayısına 1 ekler.
        if TahminSayısı == 10: #-> Tahmin sayısı 10'a ulaşınca.
            print("Kaybettiniz! Gizli kelime:\n ", Gizli_Kelime)

kurallar()
Harf_TahminEtme()
