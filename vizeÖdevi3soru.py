# Dosyanın adı
input_dosyasi = "sample.txt"
output_dosyasi = "output.txt"

# 3.A. Dosyanın içeriğini açın ve okuyun.
with open(input_dosyasi, 'r', encoding='utf-8') as file:
    dosya_icerik = file.read()

# 3.B. Dosyadaki satır sayısını sayın ve yazdırın.
satir_say = dosya_icerik.count('\n') + 1
print(f"Dosyadaki satır sayısı: {satir_say}")

# 4.C. Dosyadaki sözcük sayısını sayın ve yazdırın.
kelime_say = len(dosya_icerik.split())
print(f"Dosyadaki sözcük sayısı: {kelime_say}")

# 5.D. Yeni dosyayı oluşturun ve her satırın tersini bu dosyaya yazın.
with open(output_dosyasi, 'w', encoding='utf-8') as output_dosyasi:
    satirlar = dosya_icerik.split('\n')
    ters_satirlar = [satir[::-1] for satir in satirlar]
    ters_icerik = '\n'.join(ters_satirlar)
    output_dosyasi.write(ters_icerik)

print(f"Ters çevrilen satırlar {output_dosyasi} adlı dosyaya yazıldı.")
