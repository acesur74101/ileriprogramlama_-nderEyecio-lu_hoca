# 4.A. Fonksiyon tanımı: dikdörtgen_alani
def dikdortgen_alani(uzunluk, genislik):
    # 4.B. Değerlerin pozitif olup olmadığını kontrol etme
    if uzunluk <= 0 or genislik <= 0:
        raise ValueError("Uzunluk ve genişlik pozitif olmalıdır.")

    # 4.C. Dikdörtgenin alanını hesapla ve döndür
    alan = uzunluk * genislik
    return alan

# 4.D. Fonksiyonu kullanarak en az iki dikdörtgenin alanını bulma
try:
    # İlk dikdörtgen
    uzunluk1 = 5.4
    genislik1 = 12.6
    alan1 = dikdortgen_alani(uzunluk1, genislik1)
    print(f"Ilk dikdörtgenin alanı: {alan1}")

    # İkinci dikdörtgen
    uzunluk2 = 7
    genislik2 = 15
    alan2 = dikdortgen_alani(uzunluk2, genislik2)
    print(f"İkinci dikdörtgenin alanı: {alan2}")
    
    uzunluk3 = -15.5
    genislik3 = 22.6
    alan3 = dikdortgen_alani(uzunluk3, genislik3)
    print(f"Üçüncü dikdörtgenin alanı: {alan3}")

except ValueError as e:
    print(f"Hata: {e}")
