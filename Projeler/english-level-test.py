import random

print(">> Turkce Karakterler Kullanmaktan Kacinin <<")
print("#1 A1\n#2 A2\n#3 B1\n#4 B2\n#5 C1\n#6 C2")
seviye = int(input("\nKelimelerini bilmek istediginiz Seviye: "))

words_a1 = {
    "Tree": "Agac",
    "Cry": "Aglamak",
    "Phone": "Telefon",
    "Box": "Kutu",
    "Thin": "ince",
    "Cow": "inek",
    "Case": "dava",
    "Animal": "Hayvan",
    "Hungry": "Ac",
    "Draw": "Cizmek"
}

words_a2 = {
    "Explain": "Aciklamak",
    "Island": "Ada",
    "Key": "Anahtar",
    "Leg": "Bacak",
    "Connect": "Baglanmak",
    "Tent": "Cadir",
    "Chin": "Cene",
    "Try": "Denemek",
    "Elbow": "Dirsek",
    "Fill": "Doldurmak"
}

words_b1 = {
    "Audience": "izleyici",
    "Behavior": "Davranis",
    "Cancel": "iptal etmek",
    "Disease": "Hastalik",
    "Effort": "Caba",
    "Garbage": "Cop",
    "Health": "Saglik",
    "Industry": "Sanayi",
    "Knowledge": "Bilgi",
    "Law": "Hukuk"
}

words_b2 = {
    "Accurate": "Dogru",
    "Benefit": "Yarar",
    "Consequence": "Sonuc",
    "Decision": "Karar",
    "Emergency": "Acil durum",
    "Facility": "Tesis",
    "Generation": "Nesil",
    "Harmful": "Zararli",
    "Impact": "Etki",
    "Justice": "Adalet"
}

words_c1 = {
    "Acknowledge": "Kabul etmek",
    "Barrier": "Engel",
    "Cognitive": "Bilissel",
    "Demonstrate": "Gostermek",
    "Evaluate": "Degerlendirmek",
    "Framework": "cerceve",
    "Generate": "uretmek",
    "Hypothesis": "Hipotez",
    "Interpret": "Yorumlamak",
    "Justify": "Gerekcelendirmek"
}

words_c2 = {
    "Abstract": "Soyut",
    "Bias": "On yargi",
    "Comprehensive": "Kapsamli",
    "Discrepancy": "Celiski",
    "Empirical": "Deneysel",
    "Fluctuate": "Dalgalanmak",
    "Incentive": "Tesvik",
    "Paradigm": "Paradigma",
    "Quantitative": "Nicel",
    "Underlying": "Altinda yatan"
}

seviye_kelimeleri = {
    1: words_a1,
    2: words_a2,
    3: words_b1,
    4: words_b2,
    5: words_c1,
    6: words_c2
}

gosterilen = 0
true_point = 0
false = 0

while True:
    if seviye not in seviye_kelimeleri:
        print("Gecersiz bir seviye girdiniz. Lutfen 1 ile 6 arasinda bir deger giriniz.")
        seviye = int(input("Kelimelerini bilmek istediginiz Seviye: "))
        continue

    # Secilen seviyeye gore kelime secimi
    secme, dogru_cevap = random.sample(list(seviye_kelimeleri[seviye].items()), 1)[0]
    tahmin = input(f"{secme} kelimesinin Turkce karsiligini giriniz: ")

    if tahmin.lower() == dogru_cevap.lower():
        print("Tebrikler! Dogru bildiniz.\n")
        true_point += 1
    else:
        print(f"Tahmininiz yanlis. Dogru cevap: {dogru_cevap}\n")
        false += 1

    gosterilen += 1
    seviye_kelimeleri[seviye].pop(secme)

    # Gecis kontrolu
    if gosterilen >= 10:
        percent = true_point*10
        if true_point > 6:
            if seviye < 6:
                print(f"Tebrikler! {seviye}. seviyeyi %{percent} Doğruluk Oraniyla tamamladiniz.\n{seviye + 1}. seviyeye geciyorsunuz!\n")
                seviye += 1
                gosterilen = 0
                true_point = 0
                false = 0
            else:
                print("Tum Testi Basariyla Tamamladiniz!")
                break
        else:
            print(f"Doğruluk Oraniniz: %{percent}\nDaha fazla dogru cevap vermeniz gerekiyor.\n")
            break