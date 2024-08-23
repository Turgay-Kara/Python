    # MAP & FILTER & REDUCE

#my_list = [1, 2, 3, 4, 5]
#for i in my_list:
    #print(i + 10)


    # Map   -> Dort islem yapabiliriz.
#my_list2 = [1, 2, 3, 4, 5]
#print(list(map(lambda x: x * 10, my_list2)))  #-> Ayni isi map kullanarak daha pratik sekilde yaptik.


    # Filter    -> Filtreleyip cikti alabiliriz.
#my_list3 = [1,2,3,4,5,6,7,8,9,10]
#print(list(filter(lambda x: x % 2 == 0, my_list3)))


    # Reduce    -> Kendi icinde dort islem yapabiliriz.
#from functools import reduce
#my_list4 = [1,2,3,4]
#print(reduce(lambda a,b: a + b, my_list4))  #-> Output: 1+2+3+4 = 10