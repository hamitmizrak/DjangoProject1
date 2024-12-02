# Single Comment

"""
Multiple Comment
"""

#####################################################################################
#### lessons #################################################################
"""
 1. Python’a Giriş
   - Python Nedir?
   - Python’un Özellikleri
   - Python Kurulumu
   - Python İle İlk Program


 2. Python Yapıları
   - Değişkenler ve Veri Türleri
   - Operatörler (Aritmetik, Karşılaştırma, Mantıksal)
   - Koşul Yapıları (if-else)
   - Döngüler (for, while)
   - Listeler (Lists)
   - Demetler (Tuples)
   - Sözlükler (Dictionaries)
   - Kümeler (Sets)

 3. Fonksiyonlar (FP: Function Programming)
   - Fonksiyon Tanımlama
   - Parametre ve Geri Dönüş Değerleri
   - Lambda Fonksiyonları
   - Recursion (Özyinelemeli Fonksiyonlar)

 4. Modüller ve Kütüphaneler
   - Modül Nedir?
   - Dahili Python Modülleri (math, random, datetime, os)
   - Kütüphane Kullanımı (pip ve dış kütüphaneler)

 5. Dosya İşlemleri
   - Dosya Açma ve Kapama
   - Dosya Okuma ve Yazma İşlemleri
   - Dosya Kapatma

 6. Hata Yakalama ve İstisnalar
   - Try-Except Yapısı
   - İstisna Türleri
   - Hata Fırlatma (raise)

 7. Python ile Nesne Yönelimli Programlama (OOP)
   - Sınıflar ve Nesneler
   - Yapıcı (Constructor) ve Yıkıcı (Destructor) Metodlar
   - Miras Alma (Inheritance)
   - Polimorfizm
   - Kapsülleme (Encapsulation)
   - Soyut Sınıflar (Abstract Classes)

 8. Python Veri Yapıları ve Algoritmalar
   - Listeler, Yığınlar, Kuyruklar
   - Ağaçlar, Graf Yapıları
   - Algoritmalar (Arama, Sıralama)

 9. Python ile Veri Analizi ve Görselleştirme
   - NumPy ile Matris İşlemleri
   - Pandas ile Veri Analizi
   - Matplotlib ve Seaborn ile Veri Görselleştirme

 10. Python ile Web Geliştirme
   - Django ve Flask Giriş
   - REST API Oluşturma
   - HTML, CSS ve JavaScript ile Entegrasyon

 11. Python ile Veritabanı İşlemleri
   - SQLite, MySQL ve PostgreSQL ile Veritabanı Bağlantısı
   - SQL Sorguları Çalıştırma
   - ORM (Object-Relational Mapping) Kullanımı (SQLAlchemy, Django ORM)

 12. Python ile Makine Öğrenmesi
   - Scikit-learn Kütüphanesi
   - Veri Ön İşleme ve Temizleme
   - Regresyon, Sınıflandırma ve Kümeleme Modelleri
   - Model Değerlendirme ve Optimizasyon

 13. Python ile Web Scraping
   - BeautifulSoup ve Requests Kütüphaneleri ile Web Kazıma
   - Selenium ile Dinamik Web Kazıma

 14. Python ile Otomasyon
   - Python ile Dosya ve Sistem Otomasyonu
   - Web Üzerinde Otomatik İşlem Yürütme
   - Zamanlanmış Görevler

 15. Python ile Oyun Geliştirme
   - Pygame ile 2D Oyun Geliştirme
   - Temel Oyun Mantığı ve Yapıları

 16. Python’da Paralel Programlama ve Çoklu İş Parçacığı
   - Threading ve Multiprocessing
   - Asenkron Programlama (asyncio)

 17. Python Test ve Debugging Araçları
   - Unittest ve PyTest Kullanımı
   - Hata Ayıklama (Debugging) Yöntemleri

 18. Python ile API Entegrasyonları
   - RESTful API Kullanımı
   - JSON ve XML ile Çalışma
   - HTTP İstekleri (GET, POST, PUT, DELETE)


"""

#####################################################################################
#### best practices #################################################################
"""
1-) Noktalı virgül yazabilirsiniz veya yazmayabilirsiniz.
2-) Python’da değişken isimleri büyük ve küçük harfe duyarlıdır. 

"""

#####################################################################################
#### print ##########################################################################
print("Merhabalar Nasılsınız")

#####################################################################################
#### değişken #######################################################################
# a) Tek Değişken Atama
x = 5
print(x)

#  b) Birden Fazla Değişken Atama
x, y, z = 1, 2, 3   # x=1, y=2, z=3
print(x, y, z)

# c) Aynı değeri birden fazla değişkene atayabilirsiniz.
a = b = c = 0   # a=0, b=0, c=0
print(a, b, c)

# d) Değişkenlerin Değerlerini Değiştirme
x, y = 5, 10
print(x,y)
x, y = y, x
print(x,y)



#####################################################################################
#### boolean ########################################################################
isLogin= True
admin="Login mi ? {isLogin}"
print(admin)

#####################################################################################
#### sayılar ########################################################################
tamSayi= 44
print(tamSayi)

virgulluSayi=44.23
print(virgulluSayi)

#####################################################################################
#### type ###########################################################################
numberData= 44
print(type(numberData))

typeString="Merhabalar"
print(type(typeString))


######################################################################################
#### const ###########################################################################
# Python’da sabitleri korumak için özel bir dil özelliği yoktur,
# ancak büyük harflerle yazmak, sabitin değiştirilmemesi gerektiğini belirten bir konvansiyondur.
PI = 3.14159
print(PI)

MAX_CONNECTIONS = 100
print(MAX_CONNECTIONS)


#####################################################################################
#### Type Convesition ###############################################################
sayi1= input("1.sayıyı giriniz\n")
sayi2= input('2.sayıyı giriniz\n')
toplam=int(sayi1)+int(sayi2); # int(), float(), str(),
print("toplam sonuc",toplam)



#####################################################################################
#### string #########################################################################
kelime= ' malatya elazığ Bingöl malatya '
print(type(kelime))
print(kelime)

# Harf Sayısı
# HATA: print("kelime sayısı: "+len(kelime))
print("kelime sayısı: ",len(kelime))

# Cümle Sayısı
print("kelime adeti",kelime*3)

# UPPER
print("Büyük Harf: ",kelime.upper())
print("Hepsi Büyük Harf: ",kelime.isupper())
print("Hepsi Büyük Harf: ",kelime.upper().isupper())

# LOWER
print("Küçük Harf: ",kelime.lower())
print("Hepsi Küçük Harf: ",kelime.islower())
print("Hepsi Küçük Harf: ",kelime.lower().islower())

# REPLACE
print(kelime.replace("a","e"))

# CAPITALIZE
print("capitalize:",kelime.capitalize())

# TITLE
print("title:", kelime.title())

# TRIM
print("trimsiz: ",kelime)
print("trimsiz len: ",len(kelime))
print("trimli: ",kelime.strip())
print("trimli len: ",len(kelime.strip()))

# substrings
print(kelime[0])
kelime=kelime.strip();
print(kelime[0])
print(kelime[0:5])  # 0<=X<5

# Metot () dir: Fonksiyon okur yazarlığı için
# print(dir("java"));
