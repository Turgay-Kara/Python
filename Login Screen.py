kullanici_adi = "TurgayKara"
sifre = "12345"

ad = input("Kullanıcı Adınızı giriniz : ")
sifre_gir = input("Şifrenizi giriniz : ")

if ad == kullanici_adi and sifre == sifre_gir:
    print("Sisteme başarıyla giriş yaptınız.")
elif kullanici_adi != ad:
    print("Kullanıcı adınızı yanlış girdiniz.")
else:
    print("Şifrenizi yanlış girdiniz.")
