#12 katlı bir binanın her katında 3 daire bulunmaktadır.
#Girilen daira numarasına göre o dairenin kaçıncı katta olduğunu gösteren programı yazınız.

daireNo = 5
if daireNo < 1 or daireNo > 12:
    print("Lütfen 1-12 arasında bir değer giriniz.")
elif daireNo > 9 <= 12:
    print("3. KAT")
elif daireNo > 6 <= 9:
    print("2. KAT")
elif daireNo > 3 <= 6:
    print("1. KAT")
elif daireNo > 0 <= 3:
    print("0. KAT")
else:
    print("Lütfen 1-12 arasında bir değer giriniz.")
