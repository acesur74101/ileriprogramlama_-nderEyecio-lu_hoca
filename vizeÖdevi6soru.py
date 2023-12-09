# 6.A. Kitap sınıfı tanımı
class Kitap:
    def __init__(self, baslik, yazar, isbn):
        self._baslik = baslik  # Kapsülleme için underscore kullanımı
        self._yazar = yazar
        self._isbn = isbn

    # 6.C. Kitap ayrıntılarını görüntülemek için yöntem
    def kitap_detaylari(self):
        print(f"Başlık: {self._baslik}")
        print(f"Yazar: {self._yazar}")
        print(f"ISBN: {self._isbn}")

# 6.B. EBook sınıfı tanımı (Kitap sınıfından miras alır)
class EBook(Kitap):
    def __init__(self, baslik, yazar, isbn, dosya_boyutu):
        super().__init__(baslik, yazar, isbn)
        self._dosya_boyutu = dosya_boyutu

    # 6.C. EBook ayrıntılarını görüntülemek için yöntem
    def ebook_detaylari(self):
        self.kitap_detaylari()  # Kitap sınıfının kitap_detaylari metodunu çağırır
        print(f"Dosya Boyutu: {self._dosya_boyutu} MB")

# Kütüphane örnekleri
kitap1 = Kitap("yeni başlayanlar için java", "Bülent Çobanoğlu", "9786052263310")
ebook1 = EBook("Machine Learning Algorithms", "Aman Kharwal", "9789356484832", 5)

# 6.C. Kitap ve EBook ayrıntılarını görüntüleme
kitap1.kitap_detaylari()
ebook1.ebook_detaylari()
