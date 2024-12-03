# Single Comment

"""
Multiple Comment (Docstringler)
"""
import math
from random import randint, uniform

from django.template.defaultfilters import random

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
3-) Python'da girintileme zorunludur. Girinti, bir kod bloğunu belirtmek için kullanılır ve doğru girintileme olmadan Python kodu hata verecektir.
- Standart girinti genellikle 4 boşluk karakteri ile yapılır. Tab tuşunu kullanmak yerine boşluk karakterleri kullanmak daha yaygın ve önerilen bir yaklaşımdır.
if x > 10:
    print("x is greater than 10")   4 boşluk kullanılarak girintilendi
4-) Bir satırın uzunluğu en fazla 79 karakter olmalıdır. 
5-) Fonksiyonlar ve sınıflar arasında iki boş satır bırakılmalıdır.
def first_function():
    pass


def second_function():
    pass
6-) Fonksiyon ve değişken isimleri küçük harflerden oluşmalı ve kelimeler arasına alt çizgi (_) konulmalıdır (snake_case).

7-) Sabit değerler için kullanılan değişken isimleri büyük harflerle yazılmalıdır. 
MAX_CONNECTIONS = 100

8-) Global değişken kullanılması gerekiyorsa, global anahtar kelimesiyle belirtilmelidir. 
global total
total = 0

9-) - Python'da listeleri daha kısa ve verimli bir şekilde oluşturmak için list comprehension kullanmak iyi bir uygulamadır.
squares = [x  2 for x in range(10)]
10-) Kod modüllere ayrılmalı, yani işlevler küçük ve tek bir görevi yerine getirecek şekilde yazılmalıdır.

11-) Koşullu ifadelerde gereksiz boolean ifadelerden kaçının. 

Örneğin if x == True: yerine if x: yazmak daha kısa ve anlaşılırdır.

12-) Döngüler yazarken Python'un sunduğu iterator ve generator yapılarından faydalanmak, kodu daha verimli ve temiz hale getirir.
for i in range(10):
    print(i)


"""

#####################################################################################
#### print ##########################################################################
# Kelime yazdırmak
print("Merhabalar, Nasılsınız")

# Sayı yazdırmak
print(44)



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
#### formatter ######################################################################
# Formatter
name="Hamit"
surname="Mızrak"
school="Firat University"
# f-string
print(f"formatter: Benim adım:{name} Soyadım:{surname} okulum:{school}")

#####################################################################################
#### Escape Character ######################################################################
# Escape Character
"""
Kaçış karakterleri, programlama dillerinde özel bir anlam ifade eden ve genellikle bir karakterin, 
komutun veya sembolün, sıradan bir metin içinde kullanılması gerektiğinde ortaya çıkan problemleri 
çözmek için kullanılan karakter dizileridir

\r	Satır başı (Carriage Return)
\t	Sekme (tab)
\n	Yeni satır
"""
print(f"formatter:\n Benim adım:{name}\n Soyadım:{surname}\n okulum:{school}\n\n")
print(f"formatter:\n \rBenim adım:{name}\n\r Soyadım:{surname}\n \rokulum:{school}")


#####################################################################################
#### seperate ########################################################################
# sep: datalar arasında hangi karaktere göre göstersin
print("java","javascript","python") #default boşluk
print("java","javascript","python",sep="-")
print("java","javascript","python",sep="+")


#####################################################################################
#### end  ########################################################################
# end parametresi, print() fonksiyonu her çağrıldığında varsayılan olarak yeni bir satıra geçmeyi engeller ve
# bunun yerine belirtilen değeri kullanır.
print("birinci","ikinci",end=" son satır\n")
print("alt satır")

#####################################################################################
#### boolean ########################################################################
# True ve False, Python'da boolean veri tipleridir.
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


#####################################################################################
#### None ###########################################################################
# None: Python'da None özel bir veri türüdür ve boş veya tanımsız bir değeri ifade eder.
data = None    #Tanımsız veya boş değeri temsil eder
print("boş değer: ", data)

# - is None: None'un aynı nesne olup olmadığını kontrol eder.
# - == None: None'a eşit olup olmadığını kontrol eder.

"""
x = None

 Doğru kullanım
if x is None:
    print("x gerçekten None")

 Yanlış olmasa da önerilmeyen kullanım
if x == None:
    print("x None'a eşit")

"""


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
#### Operator #######################################################################
#  Aritmetik Operatörler: Temel matematiksel işlemleri gerçekleştirir (toplama, çıkarma, çarpma vb.).
#  Atama Operatörleri: Değişkenlere değer atar ve karmaşık işlemlerle kısayol atamalarını sağlar.
#  Karşılaştırma Operatörleri: İki değeri karşılaştırır ve mantıksal sonuçlar döndürür.
#  Mantıksal Operatörler: Birden fazla koşulun doğru olup olmadığını kontrol eder.
#  Bit Düzeyinde Operatörler: Sayılar üzerinde bit bazında işlem yapar.
#  Üyelik Operatörleri: Bir değerin bir veri yapısının üyesi olup olmadığını kontrol eder.
#  Kimlik Operatörleri: İki nesnenin aynı bellek adresine sahip olup olmadığını kontrol eder.


#####################################################################################
#### Sayısal İşlemler Dört İşlem ####################################################
a=15
b=4
print("Toplama= ",a+b)
print("Çıkarma= ",a-b)
print("Çarpma= ",a*b)
print("Virgüllü Bölme= ",a/b)
print("Tam Sayıya Bölme= ",a//b)
print("Module Bölme= ",a%b)
print("Üslü Sayılar= ",a**b)


#####################################################################################
#### Sayısal İşlemler Mantıksal İşlem ###############################################
print("Eşit mi ",a==b)
print("Eşit Değil mi ",a!=b)
print("Büyük mü ",a>b)
print("Büyük mü, Eşit mi ",a>=b)
print("Küçük mü ",a<b)
print("Küçük mü, Eşit mi  ",a<=b)

#####################################################################################
#### Atama  #####################################################

# Atama
data=10
print(data)

# Topla ve Ata
data+=15
print("Topla ve Ata: ",data)

# Çıkar ve Ata
data-=10
print("Çıkar ve Ata: ",data)

# &=     | Bit düzeyinde VE ve Ata      | x &= 3          |
# |=     | Bit düzeyinde VEYA ve Ata    | x |= 3          |
# ^=     | Bit düzeyinde XOR ve Ata     | x ^= 3          |
# >>=    | Bit kaydırma sağa ve Ata     | x >>= 3         |
# <<=    | Bit kaydırma sola ve Ata     | x <<= 3         |



#####################################################################################
#### Sayısal İşlemler Rastgele  #####################################################
print("Rastgele Tam sayı: ",randint(1,100))
print("Rastgele Ondalık sayı: ",uniform(0,1))


#####################################################################################
#### Sayısal İşlemler Math ##########################################################
print("karekök: ",math.sqrt(16))
print("üslü: ",math.pow(2,5))
print("faktöriyel: ",math.factorial(4))
print("Ceil Aşağı Yuvarlamak: ",math.ceil(4.3))
print("Floor Yukarı Yuvarlamak: ",math.floor(4.3))
print("PI: ",math.pi)
print("SINUS: ",math.sin(math.pi/2))


#####################################################################################
#### Sayısal İşlemler Cast ##########################################################
print("Cast")
x = 44.23
y= int(x)
z= str(x)
print(x)
print(y)
print(z)


