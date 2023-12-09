class Kitap:
    def __init__(self, baslik, yazar, isbn):
        self._baslik = baslik  
        self._yazar = yazar
        self._isbn = isbn

    def kitap_detaylari(self):
        print(f"Başlık: {self._baslik}")
        print(f"Yazar: {self._yazar}")
        print(f"ISBN: {self._isbn}")

class EBook(Kitap):
    def __init__(self, baslik, yazar, isbn, dosya_boyutu):
        super().__init__(baslik, yazar, isbn)
        self._dosya_boyutu = dosya_boyutu


    def kitap_detaylari(self):
        super().kitap_detaylari()  
        print(f"Dosya Boyutu: {self._dosya_boyutu} MB")
        
# 7.A. Ortak bir arayüz sağlamak için kitap_detaylari metodunu kullanabiliriz
def kitap_detaylarini_goruntule(kitap):
    kitap.kitap_detaylari()

# B. Kitap ve EBook örnekleri oluşturun
kitap1 = Kitap("yeni başlayanlar için java", "Bülent Çobanoğlu", "9786052263310")
ebook1 = EBook("Machine Learning Algorithms", "Aman Kharwal", "9789356484832", 5)

# 7.B. Polimorfizmi gösteren fonksiyonu kullanarak ayrıntıları görüntüleme
kitap_detaylarini_goruntule(kitap1)
kitap_detaylarini_goruntule(ebook1)
