#Q5:

#Kullanıcıdan bir sayı girmesinin istenmesi
sayi = input("Bir Sayı Yazınız: ")

#Girilen sayının tersinin alınması
tersSayi = sayi[::-1]   

#Palindrom kontrolünün uygulanması
if sayi == tersSayi:
    print("Bu sayı bir palindrom sayıdır.")
else: 
    print("Bu sayı bir palindrom sayı değildir.")