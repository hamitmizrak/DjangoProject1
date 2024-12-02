# Single Comment

"""
Multiple Comment
"""

'''
Multiple Comment
'''

# Hello World
print("Hello World");

# SAYILAR
sayi1=10
sayi2=20
toplam=sayi1+sayi2
print(toplam)

# Type
print(type(9));
print(type(9.1));
print(type("Merhabalar"));
print(type('Merhabalar'));

# string
kelime='malatya'
print(kelime)
print(type(kelime))

# HATA: print('Kelime sayısı:'+len(kelime))
print('Kelime sayısı:',len(kelime))


multiple="merhaba "*3
print(multiple)

# Upper, Lower
print(kelime.upper());
print("Hepsi küçük mü ?: ",kelime.islower());
print(kelime.lower());
print("Hepsi büyük mü ?: ",kelime.islower());

# Replace
kelime=kelime.replace("a","e");
print(kelime);

# Capitalize
kelime="malatya_yeşilyurt"
print(kelime.capitalize());
print(kelime.title());

# Trim
kelime2= " boşluk ";
print(kelime2);
print(kelime2.strip());
kelime3="*kelime3*" # pattern göre tıraşlamak
print(kelime3.strip("*"));

# Metot () dir: Fonksiyon okur yazarlığı için
print(dir("java"));
print(dir(str));

# substrings
print(kelime[0])
print(kelime[0:3]) # 0<=X<3

# Type Convesition
sayi1= input("1.sayıyı giriniz\n");
sayi2=input('2.sayıyı giriniz\n');
toplam=int(sayi1)+int(sayi2); # int(), float(), str(),
print("toplam sonuc",toplam)

is_result=True;
print(is_result)
