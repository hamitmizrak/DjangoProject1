
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

#  Üyelik Operatörleri ==> in, not in
#  Kimlik Operatörleri ==> is, is not
