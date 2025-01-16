##########################################################################################
#### Data Type : Class      ##############################################################

class Araba:
    marka = "Bilinmiyor"
    model = "Bilinmiyor"
    yil = 0
    renk = "Bilinmiyor"

    def calistir(self):
        print(f"{self.marka} {self.model} {self.renk} {self.yil} çalıştırıldı.")

# Sınıf örneği (1)
araba1 = Araba()
araba1.marka = "Audi"
araba1.model = "A3"
araba1.renk = "Beyaz"
araba1.yil = 2020
araba1.calistir()


# Sınıf örneği (2)
araba2 = Araba()
araba2.calistir()