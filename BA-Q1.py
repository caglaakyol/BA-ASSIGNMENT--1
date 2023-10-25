# Q1:

#Kullanıcının boy ve ağırlık değerlerinin girilmesi
boy = float(input("Lütfen boyunuzu (santimetre cinsinde) yazınız: ")) 
agirlik = float(input("Lütfen ağırlığınızı (kilogram cinsinde) yazınız: "))

#Vücut Kitle İndeksinin (VKİ) hesaplanması
VKİ = agirlik / (boy * boy)

#Sonuç
print("Vücut Kitle İndeksiniz:", VKİ)