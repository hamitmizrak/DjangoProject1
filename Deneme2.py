print("####### Örnek -1 ###################");
# Data Types (list)
arabaNotlari1= [20, 10, 50, 10];

# Eleman sayısı
len(arabaNotlari1);

print(arabaNotlari1);
print(type(arabaNotlari1));
print(arabaNotlari1[0]);

# Liste aralığıyla elemanları listelemek
print(arabaNotlari1[:3]);  # 1.YOL (0'dan 3 elemana kadar)
print(arabaNotlari1[0:3]); # 2.YOL (0'dan 3 elemana kadar)
print(arabaNotlari1[3:]);  # 3 elemanda sona kadar

# Her bir eleman için, hangi türde olduğunu bulmak içindir.
print(type(arabaNotlari1[0]))

# Liste Silmek
print(arabaNotlari1[0]);
del arabaNotlari1[0];
print(arabaNotlari1[0]);



print("####### Örnek -2 ###################");
arabaNotlari2=["Malatya", 44,"Elazığ", 23,"Ankara", 6, arabaNotlari1];
print(arabaNotlari2);
print(arabaNotlari2);
print(type(arabaNotlari2) );
print(arabaNotlari2[0]);
# dizi içindeki dizi elemanlarına erişmek
print(arabaNotlari2[6])
print(arabaNotlari2[6][0])


print("####### Örnek -3 ###################");
# Dizileri birleştirmek
yeni_list= [arabaNotlari1,arabaNotlari2];
print(yeni_list);
len(yeni_list);

