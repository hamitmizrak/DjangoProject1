##########################################################################################
#### Data Type : Class      ##############################################################

# Python'da yapıcı metot, __init__ adlı özel bir metotla tanımlanır.
# Yapıcı Metot Nasıl Çalışır?
# Bir sınıfın örneği oluşturulduğunda (class_name()) Python otomatik olarak __init__ metodunu çağırır.
# __init__, sınıfın içindeki özelliklere (attributes) başlangıç değerlerini atamak için kullanılır.
# Yapıcı metot, bir sınıfın tüm nesneleri için ortak bir başlangıç noktası sağlar.
# class ClassName:
#     def __init__(self, parametreler):
#         # Nesne özelliklerini başlat
#         self.attribute_name = parametre_degeri
# self:
# Yapıcı metodun (ve diğer sınıf metotlarının) ilk parametresi self olmalıdır.
# self, metot içinde sınıfın örneğine (instance) erişimi sağlar.
# Bu, sınıfın özelliklerini tanımlamak ve onlara değer atamak için kullanılır.
# Parametreler:
# Yapıcı metot, nesne oluşturulurken dışarıdan parametreler alabilir.


class Araba:
    def __init__(self, marka="Bilinmiyor", model="Bilinmiyor", yil=0, renk="Bilinmiyor"):
        # Yapıcı metot (constructor) ile özellikler başlatılıyor
        self.marka = marka
        self.model = model
        self.yil = yil
        self.renk = renk

    def calistir(self):
        print(f"{self.marka} {self.model} {self.renk} {self.yil} çalıştırıldı.")


# Constructor kullanarak sınıf örneği oluşturma
araba1 = Araba("Audi", "A3", 2020, "Beyaz")
araba1.calistir()  # Çıktı: Audi A3 Beyaz 2020 çalıştırıldı.

# Varsayılan değerler kullanılarak sınıf örneği oluşturma
araba2 = Araba()
araba2.calistir()  # Çıktı: Bilinmiyor Bilinmiyor Bilinmiyor 0 çalıştırıldı.
