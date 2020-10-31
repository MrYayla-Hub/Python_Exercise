def divi(num):
    divid_nums = []

    for i in range(2,num):
        if num % i == 0:
            divid_nums.append(i)
    return  divid_nums

while True:
    nums = input("Bir sayı giriniz veya Çıkmak için q' ya basınız: ")

    if nums == "q":
        print("Programdan Çıkılıyor....")
        break

    else:
        print(nums,"'ın tam bölenleri:",divi(int(nums)))