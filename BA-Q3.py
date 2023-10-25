#Q3: 

#Kullanıcıdan sırasıyla üç sayının alınacağı alan
sayi1 = (float(input("Lütfen Birinci Sayıyı Yazınız:")))
sayi2 = (float(input("Lütfen İkinci Sayıyı Yazınız:")))
sayi3 = (float(input("Lütfen Üçüncü Sayıyı Yazınız:")))

#En büyük sayının bulunacağı alan
enBuyukSayi = max(sayi1, sayi2, sayi3)

#Sonuç
print("En büyük sayı:", enBuyukSayi)