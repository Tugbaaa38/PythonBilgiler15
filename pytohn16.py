
#init fonksiyonu ve self

#Eger bir classtan bir nesne ureteceksek init, classin ilk metodu olmak zorundadir.
#self, init metodu ile gelen ve class icinden turetmis oldugumuz nesnelere ulasmamizi saglayan bir kavramdir.

#simdi bir class olusturalim 

class Ogrenci():
    def __init__(self,isim,soyisim,ogr_no,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.ogr_no=ogr_no
        self.yas=yas

 #tum ogrenciler farklidir ama hepsinin  ismi,soyismi,numarasi farkli farklidir.
 

ogrenci1=Ogrenci("Tugba","Kirac","6053",21)
ogrenci2=Ogrenci("Silanur","Kirac","2525",18)

print(ogrenci1.isim)
print(ogrenci2.ogr_no)
#buraya istedigimiz kadar ogrenci ekleyebiliriz.
