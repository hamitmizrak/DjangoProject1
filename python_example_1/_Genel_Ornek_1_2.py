"""
Gerçek Hayat Problemi: Blog Yönetim Sistemi ve İçerik Analizi
Senaryo: Bir blog yönetim sisteminiz var ve bu sistem üzerinden yazarlar içerik yayımlıyor.
Blog içeriği üzerinde çeşitli analizler yaparak yazar performansını ölçmek,
popüler içerikleri belirlemek, sık kullanılan kelimeleri analiz etmek ve kullanıcıların ilgisini çeken konuları keşfetmek istiyorsunuz.

Aşağıda Python ile bir blog yönetim sistemi için geniş kapsamlı bir içerik analizi örneği verilmiştir.
"""


# Örnek blog içerikleri
blog_icerikleri = [
    {
        "blog_id": 1,
        "yazar": "ali123",
        "baslik": "Python Programlama Rehberi",
        "icerik": "Python programlama diliyle ilgili başlangıç seviyesinden ileri düzeye kadar detaylı bilgiler içerir. Öğrenmesi kolay ve güçlü bir dildir.",
        "kategori": "Programlama",
        "goruntulenme": 1500,
        "yorumlar": [
            {"kullanici": "ayse456", "yorum": "Gerçekten harika bir rehber, çok faydalı!"},
            {"kullanici": "mehmet789", "yorum": "Bilgilendirici ama biraz daha örnek olsa iyi olurdu."},
        ],
    },
    {
        "blog_id": 2,
        "yazar": "ayse456",
        "baslik": "Web Geliştirme için HTML ve CSS",
        "icerik": "Web geliştirme dünyasına giriş yapmak isteyenler için HTML ve CSS konularında temel bilgiler sunar. İyi bir başlangıç rehberi.",
        "kategori": "Web Geliştirme",
        "goruntulenme": 1200,
        "yorumlar": [
            {"kullanici": "ali123", "yorum": "Çok net ve açıklayıcı bir yazı, teşekkürler!"},
            {"kullanici": "zeynep654", "yorum": "HTML kısmı iyi ama CSS biraz daha detaylandırılmalı."},
        ],
    },
    {
        "blog_id": 3,
        "yazar": "mehmet789",
        "baslik": "Makine Öğrenimi Nedir?",
        "icerik": "Makine öğrenimi, yapay zeka alanında bir alt daldır. Bu yazı, temel kavramlar ve uygulama alanlarını ele alır.",
        "kategori": "Yapay Zeka",
        "goruntulenme": 800,
        "yorumlar": [
            {"kullanici": "ayse456", "yorum": "Makine öğrenimi konusuna güzel bir giriş olmuş."},
            {"kullanici": "fatma321", "yorum": "Daha fazla teknik detay verilseydi çok daha faydalı olurdu."},
        ],
    },
    {
        "blog_id": 4,
        "yazar": "zeynep654",
        "baslik": "SEO Teknikleriyle Blog Trafiğini Artırma",
        "icerik": "SEO, web sitenizin arama motorlarında üst sıralarda yer almasını sağlar. Bu yazı, etkili SEO tekniklerini içerir.",
        "kategori": "Dijital Pazarlama",
        "goruntulenme": 2500,
        "yorumlar": [
            {"kullanici": "mehmet789", "yorum": "Çok işime yaradı, teşekkürler!"},
            {"kullanici": "ali123", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
        ],
    },
]

"""
1. Veri Yapıları ile Çalışma
Öğrenilecekler:
Sözlükler (Dictionaries): Blog verilerinin her bir blog için ayrıntılı bilgileri (başlık, içerik, yorumlar vb.) içermesi, sözlüklerin kullanımını gösterir.
Listeler (Lists): Bloglar ve yorumlar bir liste olarak saklanır. Bu, liste veri yapısının nasıl kullanılacağını anlamanızı sağlar.
Öğretiyor:
Karmaşık veri yapılarını modelleme.
İç içe geçmiş veri yapılarında gezinme.
2. Döngüler ve Kontroller
Öğrenilecekler:
for Döngüleri: Bloglar arasında dolaşarak bilgi toplama (örneğin, toplam blog sayısı).
Koşullar (if): Belirli kriterlere (örneğin, bir kelimenin içerikte geçmesi) dayalı kontroller.
Öğretiyor:
Verilere döngüyle erişim.
Şartlı ifadelerle kontrol mekanizmaları oluşturma.
3. Veri Analizi
Öğrenilecekler:
Sık Kullanılan Kelimeler: Metin verilerini analiz ederek en sık kullanılan kelimeleri bulma.
Popülerlik ve Görüntülenme: Görüntülenme sayısı gibi sayısal verilerle çalışarak popüler içerikleri belirleme.
Öğretiyor:
Verilerden anlamlı bilgiler çıkarma.
Metin analizi ve kelime frekansı hesaplama.
4. Fonksiyonel Programlama
Öğrenilecekler:
Lambda Fonksiyonları: Veri sıralama (örneğin, blogları uzunluğa veya görüntülenme sayısına göre sıralama) gibi durumlarda lambda fonksiyonlarını kullanma.
max ve sort: Veri kümesindeki maksimum veya sıralı değerleri bulma.
Öğretiyor:
Kodunuzu daha kısa ve etkili hale getirmek için anonim fonksiyonları kullanma.
5. Nesne Temelli Analiz
Öğrenilecekler:
Bloglar ve yorumlar gibi gerçek dünyadan alınan kavramları modellemek.
Veri yapılarıyla nesne temelli bir yaklaşımı öğrenmek.
Öğretiyor:
Kodlamada nesnelerin temsil edilmesi.
Veri organizasyonu ve işleme.
6. Kullanıcı Deneyimi ve Geri Bildirim Analizi
Öğrenilecekler:
Kullanıcıların yorumlarını analiz ederek içerik geliştirme stratejileri belirleme.
Kullanıcıların hangi bloglarla daha fazla etkileşime girdiğini ölçme.
Öğretiyor:
Kullanıcı geri bildirimlerini anlamak için metin analizi.
Müşteri odaklı geliştirme için veri toplama.
7. Gerçek Dünya Problemlerini Modelleme
Öğrenilecekler:
Blog yönetim sistemleri gibi gerçek hayat problemlerini bir yazılım çözümüne dönüştürme.
Karmaşık problemleri alt problemlere bölerek çözme.
Öğretiyor:
Gerçek dünya senaryolarında kodlama becerilerini uygulama.
Daha büyük projeleri yönetme.
8. Temel Algoritma Mantığı
Öğrenilecekler:
Belirli bir kelimenin kaç kez geçtiğini kontrol etme.
Kategorilere göre verileri gruplama ve sayma.
Yazar başına ortalama görüntülenme gibi metrikler hesaplama.
Öğretiyor:
Verileri gruplama, filtreleme ve dönüştürme.
Sayısal ve metinsel veri analizine yönelik algoritmalar geliştirme.
9. Veri Görselleştirme Hazırlığı
Öğrenilecekler:
Çıktıları daha iyi anlamak için verileri analiz etme ve özetleme.
Örneğin, bu veri analizinden bir grafik oluşturabilirsiniz.
Öğretiyor:
Çıktılardan raporlar oluşturma.
Veri analizinden sonraki adımları planlama.
10. Optimizasyon ve İyileştirme
Öğrenilecekler:
Blogları daha verimli bir şekilde sıralamak veya filtrelemek için algoritmalar geliştirme.
Çalışma süresini optimize etmek için büyük veri kümeleri üzerinde işlem yapma.
Öğretiyor:
Performansı artırma tekniklerini uygulama.
Verimli veri işleme yöntemleri.
Özet
Blog örneği, size aşağıdaki konularda pratik yapma fırsatı sunar:

Veri yapıları ve organizasyonu.
Algoritmalar ve analiz yöntemleri.
Gerçek dünyadan alınan senaryoları kodlama ile çözme.
Veri odaklı karar verme süreçlerini modelleme.
Bu bilgiler, gerçek dünya uygulamaları geliştirmek isteyen herkes için kritik bir temel oluşturur ve kodlama becerilerinizi güçlendirir! 😊

"""

"""
Kodun Özellikleri
Blog Sayısı ve Kategorilere Dağılım: Blog sayısını ve kategorilere göre dağılımını analiz eder.
Popülerlik: Görüntülenme sayısına göre en popüler blogları belirler.
Kelime Analizi: İçeriklerde sık kullanılan kelimeleri analiz ederek ilgi çekici noktaları ortaya çıkarır.
Yazar Performansı: Yazarların içeriklerini analiz ederek görüntülenme sayılarını ölçer.
Yorum Analizi: Bloglara yapılan yorum sayısını ve kullanıcıların katkılarını analiz eder.
Bu örnek, bir blog yönetim sisteminin nasıl analiz edilebileceğini gösterir ve gerçek hayatta uygulanabilir bir çözüm sunar. 😊

"""


# 1. Blogların toplam sayısı
toplam_blog = len(blog_icerikleri)
print(f"Toplam blog sayısı: {toplam_blog}")

#####################################################################################################################
# 2. Kategorilere göre blog sayısı
print("\nKategorilere göre blog sayısı:")
kategori_sayilari = {}
for blog in blog_icerikleri:
    kategori = blog["kategori"]
    kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

for kategori, sayi in kategori_sayilari.items():
    print(f"{kategori}: {sayi} blog")


#####################################################################################################################
# 3. Yazar başına yazılan blog sayısı
print("\nYazar başına yazılan blog sayısı:")
yazar_blog_sayilari = {}
for blog in blog_icerikleri:
    yazar = blog["yazar"]
    yazar_blog_sayilari[yazar] = yazar_blog_sayilari.get(yazar, 0) + 1

for yazar, sayi in yazar_blog_sayilari.items():
    print(f"{yazar}: {sayi} blog")



#####################################################################################################################
# 4. En popüler blog (görüntülenme sayısına göre)
print("\nEn popüler blog:")
en_populer_blog = max(blog_icerikleri, key=lambda x: x["goruntulenme"])
print(f"Başlık: {en_populer_blog['baslik']}, Görüntülenme: {en_populer_blog['goruntulenme']}")



#####################################################################################################################
# 5. Yorum sayısı ve en çok yorum alan blog
print("\nBloglara göre yorum sayıları:")
en_cok_yorum = 0
en_cok_yorum_blog = None

for blog in blog_icerikleri:
    yorum_sayisi = len(blog["yorumlar"])
    print(f"Başlık: {blog['baslik']}, Yorum Sayısı: {yorum_sayisi}")
    if yorum_sayisi > en_cok_yorum:
        en_cok_yorum = yorum_sayisi
        en_cok_yorum_blog = blog

print(f"\nEn çok yorum alan blog: {en_cok_yorum_blog['baslik']} ({en_cok_yorum} yorum)")



#####################################################################################################################
# 6. Sık kullanılan kelimeleri analiz etme
print("\nBlog içeriklerinde sık kullanılan kelimeler:")
from collections import Counter

tum_kelimeler = []
for blog in blog_icerikleri:
    kelimeler = blog["icerik"].lower().split()
    tum_kelimeler.extend(kelimeler)

kelime_sayilari = Counter(tum_kelimeler)
en_sik_kelimeler = kelime_sayilari.most_common(5)
for kelime, sayi in en_sik_kelimeler:
    print(f"{kelime}: {sayi} kez")


#####################################################################################################################
# 7. Kullanıcıların yaptığı toplam yorum sayısı
print("\nKullanıcıların yaptığı toplam yorum sayısı:")
kullanici_yorum_sayilari = {}
for blog in blog_icerikleri:
    for yorum in blog["yorumlar"]:
        kullanici = yorum["kullanici"]
        kullanici_yorum_sayilari[kullanici] = kullanici_yorum_sayilari.get(kullanici, 0) + 1

for kullanici, sayi in kullanici_yorum_sayilari.items():
    print(f"{kullanici}: {sayi} yorum")



#####################################################################################################################
# 8. Yazarların ortalama blog görüntülenme sayısı
print("\nYazarların ortalama blog görüntülenme sayısı:")
yazar_goruntulenmeleri = {}
for blog in blog_icerikleri:
    yazar = blog["yazar"]
    goruntulenme = blog["goruntulenme"]
    if yazar not in yazar_goruntulenmeleri:
        yazar_goruntulenmeleri[yazar] = []
    yazar_goruntulenmeleri[yazar].append(goruntulenme)

for yazar, goruntulenmeler in yazar_goruntulenmeleri.items():
    ortalama_goruntulenme = sum(goruntulenmeler) / len(goruntulenmeler)
    print(f"{yazar}: {ortalama_goruntulenme:.2f} görüntülenme")


#####################################################################################################################
# 9. Belirli bir kelimenin geçtiği blogları bulma
aranan_kelime = "Python"
print(f"\n'{aranan_kelime}' kelimesinin geçtiği bloglar:")
for blog in blog_icerikleri:
    if aranan_kelime.lower() in blog["icerik"].lower():
        print(f"Başlık: {blog['baslik']}, Yazar: {blog['yazar']}")

################################################################################################
"""
1. Kütüphane Kurulumu
Eğer bu kütüphaneler kurulu değilse, önce aşağıdaki komutlarla kurulum yapabilirsiniz:

pip install matplotlib seaborn

"""




"""
2. Görselleştirme Örnekleri
a) Blog Kategorilerine Göre Blog Sayısı
Her kategoride kaç tane blog olduğunu bir çubuk grafikle gösterebiliriz.
import matplotlib.pyplot as plt

# Kategorilere göre blog sayısını hesaplama
kategori_sayilari = {}
for blog in blog_icerikleri:
    kategori = blog["kategori"]
    kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

# Verileri hazırlama
kategoriler = list(kategori_sayilari.keys())
blog_sayilari = list(kategori_sayilari.values())

# Çubuk grafik çizimi
plt.figure(figsize=(8, 5))
plt.bar(kategoriler, blog_sayilari, color='skyblue')
plt.title("Kategorilere Göre Blog Sayısı", fontsize=14)
plt.xlabel("Kategoriler", fontsize=12)
plt.ylabel("Blog Sayısı", fontsize=12)
plt.show()
"""



"""
b) Blogların Görüntülenme Sayıları
Her bir blogun görüntülenme sayısını sütun grafik olarak gösterebiliriz.
# Verileri hazırlama
blog_basliklari = [blog["baslik"] for blog in blog_icerikleri]
goruntulenme_sayilari = [blog["goruntulenme"] for blog in blog_icerikleri]

# Çubuk grafik çizimi
plt.figure(figsize=(10, 6))
plt.barh(blog_basliklari, goruntulenme_sayilari, color='coral')
plt.title("Blogların Görüntülenme Sayıları", fontsize=14)
plt.xlabel("Görüntülenme Sayısı", fontsize=12)
plt.ylabel("Blog Başlıkları", fontsize=12)
plt.show()
"""





"""
) Yorum Sayısı Dağılımı
Her bir blogdaki yorum sayısını pasta grafiği ile gösterebiliriz.
# Yorum sayısını hazırlama
yorum_sayilari = [len(blog["yorumlar"]) for blog in blog_icerikleri]

# Pasta grafiği çizimi
plt.figure(figsize=(8, 8))
plt.pie(
    yorum_sayilari,
    labels=blog_basliklari,
    autopct='%1.1f%%',
    startangle=140,
    colors=['gold', 'lightblue', 'lightgreen', 'coral']
)
plt.title("Bloglara Göre Yorum Dağılımı", fontsize=14)
plt.show()
"""



"""
d) Sık Kullanılan Kelimeler
Blog içeriklerinde en sık kullanılan kelimelerin dağılımını çubuk grafikle görselleştirebiliriz.
from collections import Counter

# Sık kullanılan kelimeleri hesaplama
tum_kelimeler = []
for blog in blog_icerikleri:
    kelimeler = blog["icerik"].lower().split()
    tum_kelimeler.extend(kelimeler)

kelime_sayilari = Counter(tum_kelimeler)
en_sik_kelimeler = kelime_sayilari.most_common(10)

kelimeler = [kelime for kelime, _ in en_sik_kelimeler]
kullanim_sayilari = [sayi for _, sayi in en_sik_kelimeler]

# Çubuk grafik çizimi
plt.figure(figsize=(10, 6))
plt.bar(kelimeler, kullanim_sayilari, color='purple')
plt.title("En Sık Kullanılan Kelimeler", fontsize=14)
plt.xlabel("Kelime", fontsize=12)
plt.ylabel("Kullanım Sayısı", fontsize=12)
plt.xticks(rotation=45)
plt.show()
"""




"""
e) Yazarların Ortalama Görüntülenme Sayısı
Yazar başına ortalama görüntülenme sayısını sütun grafikle görselleştirebiliriz.
# Yazar başına ortalama görüntülenme hesaplama
yazar_goruntulenmeleri = {}
for blog in blog_icerikleri:
    yazar = blog["yazar"]
    goruntulenme = blog["goruntulenme"]
    if yazar not in yazar_goruntulenmeleri:
        yazar_goruntulenmeleri[yazar] = []
    yazar_goruntulenmeleri[yazar].append(goruntulenme)

ortalama_goruntulenme = {
    yazar: sum(goruntulenmeler) / len(goruntulenmeler)
    for yazar, goruntulenmeler in yazar_goruntulenmeleri.items()
}

# Verileri hazırlama
yazarlar = list(ortalama_goruntulenme.keys())
goruntulenme_ortalamalari = list(ortalama_goruntulenme.values())

# Çubuk grafik çizimi
plt.figure(figsize=(8, 5))
plt.bar(yazarlar, goruntulenme_ortalamalari, color='green')
plt.title("Yazarların Ortalama Görüntülenme Sayıları", fontsize=14)
plt.xlabel("Yazarlar", fontsize=12)
plt.ylabel("Ortalama Görüntülenme", fontsize=12)
plt.show()
"""



"""
3. Geliştirme ve Genişletme İmkanları
Seaborn ile İyileştirilmiş Grafikler: Seaborn kullanarak grafikleri daha modern bir görünüme kavuşturabilirsiniz.
Interaktif Grafikler: Plotly veya Bokeh kütüphanelerini kullanarak kullanıcıların grafikleri keşfetmesine olanak sağlayabilirsiniz.
Dashboard: Dash veya Streamlit gibi araçlarla bir dashboard oluşturarak tüm analizleri tek bir platformda sunabilirsiniz.

"""

"""


"""

"""


"""

"""


"""


"""


"""


"""


"""