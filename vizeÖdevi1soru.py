# A. Kullanıcının adını girdi olarak alır
kullanici_adi = input("Adınızı girin: ")

# B. Kullanıcıyı kişiselleştirilmiş bir mesajla karşılar
print(f"Merhaba, {kullanici_adi}! Hoş geldin.")

# C. Kullanıcıdan iki sayı girmesini ister
num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

# D.İki sayının toplamını, farkını, çarpımını ve bölümünü hesaplar ve yazdırır
toplama_islemi = num1 + num2
fark_islemi = num1 - num2
carpma_islemi = num1 * num2

# D.Bölme işlemi için sıfıra bölme hatasını kontrol et
if num2 != 0:
    bolme_islemi = num1 / num2
    print(f"Toplam: {toplama_islemi}")
    print(f"Fark: {fark_islemi}")
    print(f"Çarpım: {carpma_islemi}")
    print(f"Bölüm: {bolme_islemi}")
else:
    print("Bir sayıyı sıfıra bölemezsiniz. Lütfen ikinci sayıyı sıfırdan farklı bir değer girin.")
