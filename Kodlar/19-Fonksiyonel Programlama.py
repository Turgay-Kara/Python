    # Fonksiyonel Programlama

# Yan Etkisiz Fonksiyon Ornek-1 (basit yan etki)

"""
A = 9

def impure_sum(b):
    return b + A

def pure_sum(a, b):
    return a + b

print(impure_sum(6))    #-> Sonuc A'ya bagli olarak degisir. (Yan Etki)
print(pure_sum(3,4))    #-> Sonuc her zaman 7 olur.

"""



# Yan Etkisiz Fonksiyon Ornek-2 (olumcul yan etki)
# Islem sonucunda C:\Users\Turgay> klasoru icerisindeki deneme.txt adli metin dosyasisin verilerini output olarak verecektir.

#class LineCounter:
    #def __init__(self, filename):
        #self.file = open(filename, 'r')
        #self.lines = []
    
    #def read(self):
        #self.lines = [line for line in self.file]
    
    #def count(self):
        #return len(self.lines)


#lc = LineCounter('deneme.txt') 

#print(lc.lines) 
#print(lc.count())

#lc.read()

#print(lc.lines)
#print(lc.count())

#FP

#def read(filename):
  #with open(filename, 'r') as f:
      #return [line for line in f]

#def count(lines):
  #return len(lines)

#example_lines = read('deneme.txt')
#lines_count = count(example_lines)
#lines_count