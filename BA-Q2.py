#Q2:

#İşçinin mevcut maaşı ve zam oranının girilmesi:
maas = float(input("Lütfen mevcut maaşınızı yazınız: "))
zamOrani = float(input("Lütfen zam oranınızı (% şeklinde) yazınız: "))

#Zam oranının hesaplanması
zamMiktari = maas * (zamOrani / 100)

#Zamlı maaş hesaplanması
zamliMaas = maas + zamMiktari 

#Sonuç
print("Zamlı Maaşınız:", zamliMaas)