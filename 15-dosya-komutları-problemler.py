def findPass(temp):
    temp = temp[:-1]
    tempList = temp.split(">")
    stuName = tempList[0].split("-")[0]  # BURASI HAYAT KURTARAN KISIM
    # tempList2 = tempList[0].split("-")
    # stuName = tempList2[0]
    stuStatus = tempList[1]

    if stuStatus == "AA" or stuStatus == "BA" or stuStatus == "BB" or stuStatus == "CB" or stuStatus == "CC" :
        passStatus = "Başarılı"

    elif stuStatus == "DC"  or stuStatus == "DD" or stuStatus == "FD":
        passStatus = "Koşullu"

    else:
        passStatus = "Başarısız"

    return  stuName + "----" + passStatus + "\n"


with open("C:/Users/cfrkn/OneDrive/Masaüstü/notlar.txt","r+", encoding = "utf-8") as file:
    stuInfo = []
    for i in file:
        stuInfo.append(findPass(i))

    with open("C:/Users/cfrkn/OneDrive/Masaüstü/Ogrenci-Durumu.txt", "w", encoding="utf-8") as file2:

        for i in stuInfo:
            file2.write(i)



