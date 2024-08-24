    #STRİNG "METOTLAR"
#isim = "Turgay Kara"
#text1 = isim.center(10, '*')            #-> turgay = 6 karakterli, .center parantezine 10yazdik 6 turgayda var kaldi 4, bu 4 karakteri isim'in yanlarina dağitir.
#text2 = isim.rjust(10, '*')             #-> .center'a benziyor ama turgay'in sağina 4 karakter * yazdirir.
#text3 = isim.ljust(10, '*')             #-> .center'a benziyor ama turgay'in soluna 4 karakter * yazdirir.
#text4 = isim.startswith("t")            #-> değişkenimiz küçük t ile mi başliyor?
#text5 = isim.endswith("y")              #-> değişkenim küçük y ile mi bitiyor?
#text6 = isim.title()                    #-> Tüm kelimelerin baş harfini büyük yapar.
#text7 = isim.split(" ")                 #-> Parantez içine yazilan ifadeyi her gördüğünde değişkeni parçalar ve bir listeye atar.
#text8 = "-".join(isim)                  #-> Her karakter arasina istenilen elemani yazar.
#text9 = isim.swapcase()                 #-> Büyük harfleri küçük, küçük harfleri büyük yapar.
#text10 = isim.upper()                   #-> Tüm harfleri Büyük yapar.
#text11 = isim.lower()                   #-> Tüm harfleri Küçük yapar.
#text12 = isim.capitalize()              #-> Cümlenin ilk kelimesinin baş harfini büyük yapar(Diğerlerini küçültür.)
#text13 = isim.count("a")                #-> Istenilen elemanin kaç tane olduğunu söyler. -> 1
#text14 = isim.lower().count("t")        #-> Tüm harfleri küçültür ve istenilen elemanin cümlede kaç kere geçtiğini sayar.
#text15 = isim.upper().count("T")        #-> İstenilen elemani büyülterek istenilen elemani sayar.
#text16 = isim.find("Kara")              #-> Bulmamiza yarar. -> 7.indexten itibaren başladiğini bize söyler.
#text17 = isim.index("g")                #-> Kaçinci indexten itibaren olduğunu bize söyler. -> 3
#text18 = isim.replace("Kara", "Beyaz")  #-> .replace("Değiştirmek istediğin.", "Yerine koyacağin.")
#text19 = '  - Hello World  '.lstrip()   #-> Sol taraftaki boşluğu sil. -> .lstrip()
#text20 = '  - Hello World  '.rstrip()   #-> Sağ taraftaki boşluğu sil. -> .rstrip()
#text21 = '  - Hello World  '.strip()    #-> Her iki taraftaki boşluğu sil. -> #.strip()
#print(text20)