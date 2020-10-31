# Problem 1
# Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.
# [(3,4),(10,3),(5,6),(1,9)]
# Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir
# fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu
# uygulayarak ekrana şöyle bir liste yazdırın.
# [12, 30, 30, 9]
# Not : map() fonksiyonunu kullanmaya çalışın.

liste = [(3,4),(10,3),(5,6),(1,9)]
print(list(map(lambda x: x[0] * x[1], liste)))

# Problem 2
# Elinizde şöyle bir liste bulunsun.
# [1,2,3,4,5,6,7,8,9,10]
# Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir
# fonksiyon yazın.
# Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra
# reduce() fonksiyonunu kullanın.

from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]
liste2 = list(filter(lambda x: x%2==0,liste))
print(reduce(lambda x,y:x+y,liste2))

# Problem 4
# Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.
# isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.
# Not: zip() fonksiyonunu kullanmaya çalışın.

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(isimler,soyisimler):
 print(i,j)