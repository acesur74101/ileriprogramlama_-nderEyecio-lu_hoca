
#2.A kendime özel 5 sayıdan oluşan liste tanımladım. 3^n şeklinde
sayilistesi=[27,81,3,9,243]


#2.B litesyi yazdırmak için iki yöntem kullandım 1. birden yazdırma 2. for loop kullanarak

#1 
print(sayilistesi)
#2
for i in sayilistesi:
    print(i,end=" ")
print("\n")
#2.C Listedeki tüm öğelerin toplamını hesaplayın ve yazdırın.
listeElemanToplami=0

for i in sayilistesi:
    listeElemanToplami+=i

print(f"listedeki elemanlarin toplami= {listeElemanToplami}")


#2.D listeye yeni eleman eklemek.

sayilistesi.append(729)

#2.E listeyi artan düzende sıralayın, bunun için üç yöntem kullanacağım 1. hazır sort metodu,2.sorted fonksiyonu, 3. kendi sorting algoritmamı yazacağım

#1
siralanmisliste1=sayilistesi
siralanmisliste1.sort()
print(f"siralanmis liste= {siralanmisliste1}")

#2
siralanmisliste2=sorted(sayilistesi)
print(f"siralanmis liste= {siralanmisliste2}")

#3

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

siralanmisliste3= sayilistesi
siralanmisliste3 = quicksort(sayilistesi)
print(f"siralanmis liste= {siralanmisliste3}")

#2.F Dizin 2'deki ogeyi kaldirin.

sayilistesi=siralanmisliste1

sayilistesi.pop(2)


#2.G Son listeyi yazdirin

print(f"son liste= {sayilistesi}")