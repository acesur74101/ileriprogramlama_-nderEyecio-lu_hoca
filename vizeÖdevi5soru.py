# 5.A. Kitap sınıfı tanımı
class Kitap:
    def __init__(self, baslik, yazar, isbn):
        self.baslik = baslik
        self.yazar = yazar
        self.isbn = isbn

    # 5.C. Kitap ayrıntılarını görüntülemek için yöntem
    def kitap_detaylari(self):
        print(f"Başlık: {self.baslik}")
        print(f"Yazar: {self.yazar}")
        print(f"ISBN: {self.isbn}")
        print()

# 5.B. Kitap sınıfının bir örneği
ornek_kitap = Kitap("Yeni Başlayanlar için java", "Bülent Çobanoğlu", "9786052263310")

# C. Kitap ayrıntılarını görüntüleme
ornek_kitap.kitap_detaylari()
