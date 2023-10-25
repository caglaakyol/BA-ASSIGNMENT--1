#Q4:

#Kullanıcının dairenin yarıçapını bilgisinin alınması
yaricap = float(input("Lütfen Dairenin Yarıçapını Yazınız:"))

#Daire alanının hesaplanması
alan = math.pi * yaricap**2

#Daire çevresinin hesaplanması
cevre = 2 * math.pi * yaricap

#Sonuç
print("Dairenin Alanı:", alan)
print("Dairenin Çevresi", cevre)