# Proje
# Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler
# ekleyin ve bu class'ı kullanmaya çalışın.

# Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.

import time

class compSpec():

    def __init__(self,cpu = "Stock",gpu = "Stock",ram = "Stock",hdd = "Yok",ssd = "Yok",main_board = "Stock",power_supply = "Stock"):

        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.hdd = hdd
        self.ssd = ssd
        self.main_board = main_board
        self.power_supply = power_supply

    def slctCPU(self):
        replyCPU = int(input("""
        
            Hangi Markayı Kullanacaksınız:
                    
                    1-INTEL
                    
                    2-RYZEN
                    
            ****************************
                    SEÇİM: 
            ****************************
                    
             """))

        if replyCPU == 1:
            print("İntel Markasını seçtiniz")
            mdlCPU = input("""
            
                1- i3
                2- i5
                3- i7
                4- i9
                
                *****************************************
                BİR ÖNCEKİ MENÜYE DÖNMEK İÇİN Q' YA BASINIZ
                
                **********************************************
            
                SEÇİMİNİZİ GİRİNİZ: 
                
                **********************************************""")

            if mdlCPU == "Q":
                print("Bir Önceki Menüye Dönülüyor...")
                time.sleep(1)
                break

            elif mdlCPU == "1":
                self.cpu = "i3"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "2":
                self.cpu = "i5"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "3":
                self.cpu = "i7"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "4":
                self.cpu = "i9"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            else:
                print("Geçersiz İşlem")
                time.sleep(1)

        elif replyCPU == 2:
            print("Ryzen Markasını seçtiniz")
            mdlCPU = input("""
            
                1- Ryzen 3
                2- Ryzen 5
                3- Ryzen 7
                4- Ryzen 9

                **********************************************
                
                BİR ÖNCEKİ MENÜYE DÖNMEK İÇİN Q' YA BASINIZ
                
                **********************************************
            
                SEÇİMİNİZİ GİRİNİZ: 
                
                **********************************************""")

            if mdlCPU == "Q":
                print("Bir Önceki Menüye Dönülüyor...")
                time.sleep(1)
                break

            elif mdlCPU == "1":
                self.cpu = "Ryzen 3"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "2":
                self.cpu = "Ryzen 5"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "3":
                self.cpu = "Ryzen 7"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            elif mdlCPU == "4":
                self.cpu = "Ryzen 9"
                print("İşlemci Seçilmiştir...")
                time.sleep(1)

            else:
                print("Geçersiz İşlem")
                time.sleep(1)

        else:
            print("Geçersiz İşlem")
            time.sleep(1)

    def slctMain_Board(self):
        replyMain_Board = input("""
            
            1-Extended ATX
            
            2-ATX
            
            3-Micro ATX
            
            4-Mini ATX
        
            **********************************************
                
            BİR ÖNCEKİ MENÜYE DÖNMEK İÇİN Q' YA BASINIZ
            
            **********************************************
            
            SEÇİMİNİZİ GİRİNİZ: 
            
            **********************************************""")

        if replyMain_Board == "Q":
            print("Bir Önceki Menüye Dönülüyor...")
            time.sleep(1)
            break

        elif replyMain_Board == "1":
            self.main_board ="Extended ATX"
            print("Ana Kart Seçilmiştir...")
            time.sleep(1)

        elif replyMain_Board == "2":
            self.main_board ="ATX"
            print("Ana Kart Seçilmiştir...")
            time.sleep(1)

        elif replyMain_Board == "3":

            if self.cpu == "Ryzen 9" and self.cpu == "i9":
                print("İşlemciniz Ana Kart İle Uyuşmuyor...")
                time.sleep(1)
                print("Bir Önceki Menüye Dönülüyor...")
                time.sleep(1)

            else:
                self.main_board ="Micro ATX"
                print("Ana Kart Seçilmiştir...")
                time.sleep(1)

        elif replyMain_Board == "4":

            if self.cpu == "Ryzen 9" and self.cpu == "i9":
                print("İşlemciniz Ana Kart İle Uyuşmuyor...")
                time.sleep(1)
                print("Bir Önceki Menüye Dönülüyor...")
                time.sleep(1)

            else:
                self.main_board ="Mini ATX"
                print("Ana Kart Seçilmiştir...")
                time.sleep(1)

        else:
            print("Geçersiz İşlem")
            time.sleep(1)

    def slctRAM(self):
        replyRAM = input("""
            
            1- 4 GB 2666 MHz
            
            2- 8 GB 2888 MHz
            
            3- 16 GB 3666 MHz
            
            4- 32 GB 4200 MHz
            
            **********************************************
                
            BİR ÖNCEKİ MENÜYE DÖNMEK İÇİN Q' YA BASINIZ
            
            **********************************************
            
            SEÇİMİNİZİ GİRİNİZ: 
            
            **********************************************""")

        if replyRAM == "Q":
            print("Bir Önceki Menüye Dönülüyor...")
            time.sleep(1)
            break

        elif replyRAM == "1":
            replyRAM_pcs = int(input("Adet Giriniz:  "))

            if (self.main_board == "Stock" or self.main_board == "Mini ATX" or self.main_board == "Micro ATX") and replyRAM_pcs >= 3:
                print("Ana Kartınıza Maksimum 2 RAM Takılabilir...")
                time.sleep(1)
                break

            else:
                if replyRAM_pcs == 1:
                    self.ram = "1 x 4 GB 2666 MHz"
                    print("RAM Seçilmiştir...")
                    time.sleep(1)


        elif replyRAM == "2":
            replyRAM_pcs = int(input("Adet Giriniz:  "))

            if (self.main_board == "Stock" or self.main_board == "Mini ATX" or self.main_board == "Micro ATX") and replyRAM_pcs >= 3:
                print("Ana Kartınıza Maksimum 2 RAM Takılabilir...")
                time.sleep(1)
                break

            else:
                if replyRAM_pcs == 1:
                    self.ram = "1 x 8 GB 2888 MHz"
                    print("RAM Seçilmiştir...")
                    time.sleep(1)

        elif replyRAM == "3":
            replyRAM_pcs = int(input("Adet Giriniz:  "))

            if (self.main_board == "Stock" or self.main_board == "Mini ATX" or self.main_board == "Micro ATX") and replyRAM_pcs >= 3:
                print("Ana Kartınıza Maksimum 2 RAM Takılabilir...")
                time.sleep(1)
                break

            else:
                if replyRAM_pcs == 1:
                    self.ram = "1 x 16 GB 3666 MHz"
                    print("RAM Seçilmiştir...")
                    time.sleep(1)

        elif replyRAM == "4":
            replyRAM_pcs = int(input("Adet Giriniz:  "))

            if (self.main_board == "Stock" or self.main_board == "Mini ATX" or self.main_board == "Micro ATX") and replyRAM_pcs >= 3:
                print("Ana Kartınıza Maksimum 2 RAM Takılabilir...")
                time.sleep(1)
                break

            else:
                if replyRAM_pcs == 1:
                    self.ram = "1 x 32 GB 4200 MHz"
                    print("RAM Seçilmiştir...")
                    time.sleep(1)

                elif



    def __str__(self):
        return " Ana Kart: {}\n İşlemci: {}\n RAM: {}\n Ekran Kartı: {}\n SSD: {}\n HDD: {}\n Güç Kaynağı: {}".format(self.main_board,self.cpu,self.ram,self.gpu,self.ssd,self.hdd,self.power_supply)