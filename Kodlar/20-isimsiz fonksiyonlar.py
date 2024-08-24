"""
    # isimsiz fonksiyonlar
def old_sum(a, b):
    return a + b

print(old_sum(4,5))


    # LAMBDA
new_sum = lambda a,b: a + b
print(new_sum(4,5))

sirasiz_liste = [("b",3), ("a", 8), ("d", 12), ("c", 1)]
print(sirasiz_liste)

    # Kucukten buyuge dogru siralayalim:
print(sorted(sirasiz_liste, key = lambda x: x[1]))  # Output: [('c', 1), ('b', 3), ('a', 8), ('d', 12)]
"""


"""
    # Vektorel Operasyonlar (OOP)
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a))

for i in range(len(a)):
    ab.append(a[i]*b[i])

print(ab)
"""

#   Yukaridaki ornekte ayni islemi daha cok caba harcayarak yapmistik.

#import numpy as np
#a = np.array([1,2,3,4])
#b = np.array([2,3,4,5])

#print(a*b)      #-> Output: [2  6 12 20]