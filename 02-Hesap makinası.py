
opr = int(input("Bir işlem seçiniz: \n1.Toplama \n2.Çıkarma \n3.Çarpma \n4.Bölme \nİşlem: "))
num1 = float(input("İlk değeri giriniz: "))
num2 = float(input("İkinci değeri giriniz: "))
temp = None
if opr == 1:
    temp = num1 + num2
    print("İşleminizin sonucu: {}".format(temp))
elif opr == 2:
    temp = num1 - num2
    print("İşleminizin sonucu: {}".format(temp))
elif opr == 3:
    temp = num1 * num2
    print("İşleminizin sonucu: {}".format(temp))
else:
    temp = num1 / num2
    print("İşleminizin sonucu: {}".format(temp))