"""
Gerçek Hayat Problemi: Blog Yönetim Sistemi ve İçerik Analizi
Senaryo: Bir blog yönetim sisteminiz var ve bu sistem üzerinden yazarlar içerik yayımlıyor.
Blog içeriği üzerinde çeşitli analizler yaparak yazar performansını ölçmek,
popüler içerikleri belirlemek, cok kullanılan kelimeleri analiz etmek ve kullanıcıların ilgisini çeken konuları keşfetmek istiyorsunuz.

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
    },{
        "blog_id": 2,
        "yazar": "ayse123",
        "baslik": "Web Geliştirme için HTML ve CSS",
        "icerik": "Web geliştirme dünyasına giriş yapmak isteyenler için HTML ve CSS konularında temel bilgiler sunar. İyi bir başlangıç rehberi.",
        "kategori": "Web Geliştirme",
        "goruntulenme": 2000,
        "yorumlar": [
            {"kullanici": "ali123", "yorum": "Çok net ve açıklayıcı bir yazı, teşekkürler!"},
            {"kullanici": "zeynep654", "yorum": "HTML kısmı iyi ama CSS biraz daha detaylandırılmalı."},
        ],
    },
    {
        "blog_id": 3,
        "yazar": "mehmet123",
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
        "yazar": "zeynep123",
        "baslik": "SEO Teknikleriyle Blog Trafiğini Artırma-1",
        "icerik": "SEO, web sitenizin arama motorlarında üst sıralarda yer almasını sağlar. Bu yazı, etkili SEO tekniklerini içerir.",
        "kategori": "Dijital Pazarlama",
        "goruntulenme": 2500,
        "yorumlar": [
            {"kullanici": "mehmet789", "yorum": "Çok işime yaradı, teşekkürler!"},
            {"kullanici": "ali123", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
        ],
    }, {
        "blog_id": 5,
        "yazar": "zeynep456",
        "baslik": "SEO Teknikleriyle Blog Trafiğini Artırma-2",
        "icerik": "SEO, web sitenizin arama motorlarında üst sıralarda yer almasını sağlar. Bu yazı, etkili SEO tekniklerini içerir.",
        "kategori": "Dijital Pazarlama",
        "goruntulenme": 2800,
        "yorumlar": [
            {"kullanici": "mehmet789", "yorum": "Çok işime yaradı, teşekkürler!"},
            {"kullanici": "ali123", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
            {"kullanici": "ali1234", "yorum": "SEO'yu iyi anlatmışsınız, pratik teknikler için güzel bir rehber."},
        ],
    },
]

"""
    Kodun Özellikleri
    Blog Sayısı ve Kategorilere Dağılım: Blog sayısını ve kategorilere göre dağılımını analiz eder.
    Popülerlik: Görüntülenme sayısına göre en popüler blogları belirler.
    Kelime Analizi: İçeriklerde cok kullanılan kelimeleri analiz ederek ilgi çekici noktaları ortaya çıkarır.
    Yazar Performansı: Yazarların içeriklerini analiz ederek görüntülenme sayılarını ölçer.
    Yorum Analizi: Bloglara yapılan yorum sayısını ve kullanıcıların katkılarını analiz eder.
    Bu örnek, bir blog yönetim sisteminin nasıl analiz edilebileceğini gösterir ve gerçek hayatta uygulanabilir bir çözüm sunar. 
"""

# 1. Blogların toplam sayısı listeleyerek görselleştirin.
# 2. Kategorilere göre blog sayısı  listeleyerek görselleştirin.
# 3. Yazar başına yazılan blog sayısı listeleyerek görselleştirin.
# 4. En popüler blog (görüntülenme sayısına göre) listeleyerek görselleştirin.
# 5. Yorum sayısı ve en çok yorum alan blog listeleyerek görselleştirin.
# 6. Sık kullanılan kelimeleri analiz etme listeleyerek görselleştirin.
# 7. Kullanıcıların yaptığı toplam yorum sayısı listeleyerek görselleştirin.
# 8. Yazarların ortalama blog görüntülenme sayısı listeleyerek görselleştirin.
# 9. Belirli bir kelimenin geçtiği blogları bularak  listeleyerek görselleştirin.
# 10 Bloglarda En Çok Görüntülenme Sayısına Göre İlk 3 Blog
# 11. Bloglarda yorum sayılarının ortalamasını hesaplayın.



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
cok Kullanılan Kelimeler: Metin verilerini analiz ederek en cok kullanılan kelimeleri bulma.
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
Bu bilgiler, gerçek dünya uygulamaları geliştirmek isteyen herkes için kritik bir temel oluşturur ve kodlama becerilerinizi güçlendirir! 
"""

######################################################################################
import matplotlib.pyplot as plt
from collections import Counter

######################################################################################
# 1. Blogların toplam sayısı
toplam_blog = len(blog_icerikleri)
print(f"Toplam blog sayısı: {toplam_blog}")


#####################################################################################################################
# 2. Kategorilere göre blog sayısı
# Kategorilere göre blog sayısını hesaplama
def kategorilere_gore_blog_sayisi_grafik(blog_icerikleri):
    """
    Blog içeriklerini alır ve kategorilere göre blog sayısını bir çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.
    """
    print("\nKategorilere göre blog sayısı:")

    # Kategorilere göre blog sayısını hesaplama
    kategori_sayilari = {}
    for blog in blog_icerikleri:
        kategori = blog["kategori"]
        # Sözlükte belirtilen bir anahtarın değerini döndürür.
        # Eğer anahtar mevcutsa, o anahtara ait değeri döndürür.
        # Eğer anahtar sözlükte yoksa, varsayılan bir değer döndürür (burada varsayılan değer 0).
        # Eğer kategori zaten sözlükte varsa, mevcut değeri bir artırır.
        kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

    for kategori, sayi in kategori_sayilari.items():
        print(f"{kategori}: {sayi} blog")

    # Verileri hazırlama
    kategoriler = list(kategori_sayilari.keys())  # Kategorilerin isimleri
    blog_sayilari = list(kategori_sayilari.values())  # Blog sayıları

    # Çubuk grafik çizimi
    #  Grafik alanının boyutunu 8 birim genişlik ve 5 birim yükseklik olarak ayarlar.
    #
    plt.figure(figsize=(8, 5))  # Grafik boyutu

    # Color: skyblue (şerit rengi) ve edgecolor: black (arka plan rengi) ile çubukların çizgilerinin ekranda gösterilmesini sağlar.
    # plt.bar: Çubuk grafik oluşturur.
    # kategoriler: X eksenindeki kategoriler.
    # blog_sayilari: Her kategorinin çubuk yüksekliği (Y ekseni).
    # color: Çubukların rengini belirler (skyblue).
    # edgecolor: Çubuk kenarlarının rengini belirler (black).
    plt.bar(kategoriler, blog_sayilari, color='skyblue', edgecolor='black', alpha=0.9)  # Çubuk grafiği

    # plt.title: Grafiğin başlığını belirler.
    # fontsize: Başlık metninin boyutunu ayarlar.
    plt.title("Kategorilere Göre Blog Sayısı", fontsize=16, fontweight='bold', color='darkblue')  # Grafik başlığı

    # plt.xlabel: X ekseninin açıklama metnini belirler.
    plt.xlabel("Kategoriler", fontsize=14, labelpad=10, fontweight='bold')  # X ekseni etiketi

    # plt.ylabel: Y ekseninin açıklama metnini belirler.
    plt.ylabel("Blog Sayısı", fontsize=14, labelpad=10, fontweight='bold')  # Y ekseni etiketi

    # rotation=30: Kategori isimlerini 30 derece eğimle yazdırır.
    # fontsize=10: X ekseni yazılarının boyutunu belirler.
    plt.xticks(rotation=30, fontsize=12, color='darkred')  # X ekseni yazıları
    for i, val in enumerate(blog_sayilari):
        plt.text(i, val + 0.2, str(val), ha='center', fontsize=12, color='darkgreen', fontweight='bold')


    # Arka plan rengi ve ızgara
    plt.gca().set_facecolor('whitesmoke')  # Arka plan rengi

    # X ve Y ekseni çizgileri
    plt.gca().spines['bottom'].set_linewidth(1.5)
    plt.gca().spines['left'].set_linewidth(1.5)

    # axis='y': Sadece Y ekseni boyunca ızgara çizgileri çizer.
    # linestyle='--': Çizgi stilini kesik çizgi olarak ayarlar.
    # alpha=0.7: Izgara çizgilerinin saydamlığını belirler.
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara

    # plt.tight_layout: Grafik elemanlarının düzenini optimize eder.
    plt.tight_layout()  # Grafik düzeni

    # Grafik kaydetme
    plt.savefig("kategorilere_gore_blog_sayisi.png", dpi=300)

    # plt.show: Grafiği ekranda gösterir.
    plt.show()

# Fonksiyonu çağırarak grafik oluşturma
kategorilere_gore_blog_sayisi_grafik(blog_icerikleri)

# @@@@@@@@@@@@@@@@
# Soru: Blogların kategorilere göre yüzdesel dağılımı nedir?
# Çözüm: Her kategori için yüzdesel dağılım hesaplanır ve pasta grafikte gösterilir.
def kategorilere_gore_yuzde(blog_icerikleri):
    kategori_sayilari = {}
    for blog in blog_icerikleri:
        kategori = blog["kategori"]
        kategori_sayilari[kategori] = kategori_sayilari.get(kategori, 0) + 1

    # Verileri hazırlama
    kategoriler = list(kategori_sayilari.keys())
    blog_sayilari = list(kategori_sayilari.values())

    # Pasta grafiği çizimi
    plt.figure(figsize=(8, 8))
    plt.pie(blog_sayilari, labels=kategoriler, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Kategorilere Göre Blogların Yüzdesel Dağılımı", fontsize=14)
    plt.show()

kategorilere_gore_yuzde(blog_icerikleri)

#####################################################################################################################
# 3. Yazar başına yazılan blog sayısı

def yazar_basina_blog_sayisi_grafik(blog_icerikleri):
    """
    Blog içeriklerini alır, yazar başına yazılan blog sayısını hesaplar ve çubuk grafik olarak görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.
    """
    print("\nYazar başına yazılan blog sayısı:")

    # Yazar başına blog sayısını hesaplama
    yazar_blog_sayilari = {}
    for blog in blog_icerikleri:
        yazar = blog["yazar"]
        yazar_blog_sayilari[yazar] = yazar_blog_sayilari.get(yazar, 0) + 1

    # Hesaplanan sonuçları yazdırma
    for yazar, sayi in yazar_blog_sayilari.items():
        print(f"{yazar}: {sayi} blog")

    # Verileri hazırlama
    yazarlar = list(yazar_blog_sayilari.keys())  # Yazar isimleri
    blog_sayilari = list(yazar_blog_sayilari.values())  # Blog sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(8, 5))  # Grafik boyutu
    plt.bar(yazarlar, blog_sayilari, color='orange', edgecolor='black')  # Çubuk grafiği
    plt.title("Yazar Başına Blog Sayısı", fontsize=14)  # Grafik başlığı
    plt.xlabel("Yazarlar", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Blog Sayısı", fontsize=12)  # Y ekseni etiketi
    plt.xticks(rotation=30, fontsize=10)  # X ekseni yazılarının döndürülmesi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    # Grafik kaydetme
    plt.savefig("yazar_basina_blog_sayisi_grafik.png", dpi=300)
    plt.show()


# Fonksiyonu çağırarak grafik oluşturma
# yazar_basina_blog_sayisi_grafik(blog_icerikleri)


#####################################################################################################################
# 4. En popüler blog (görüntülenme sayısına göre)
import matplotlib.pyplot as plt


def en_populer_blog_grafik(blog_icerikleri):
    """
    Blog içeriklerini analiz ederek en popüler blogu belirler ve tüm blogların görüntülenme sayılarını görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.

    Çıktı:
        En popüler blog başlık ve görüntülenme sayısını konsola yazdırır.
        Görüntülenme sayılarını çubuk grafikle görselleştirir.
    """
    # En popüler blogu belirleme
    print("\nEn popüler blog:")
    en_populer_blog = max(blog_icerikleri, key=lambda x: x["goruntulenme"])
    print(f"Başlık: {en_populer_blog['baslik']}, Görüntülenme: {en_populer_blog['goruntulenme']}")

    # Verileri hazırlama
    blog_basliklari = [blog["baslik"] for blog in blog_icerikleri]  # Blog başlıkları
    goruntulenme_sayilari = [blog["goruntulenme"] for blog in blog_icerikleri]  # Görüntülenme sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.barh(blog_basliklari, goruntulenme_sayilari, color='lightgreen', edgecolor='black')  # Yatay çubuk grafik
    plt.title("Blogların Görüntülenme Sayıları", fontsize=14)  # Grafik başlığı
    plt.xlabel("Görüntülenme Sayısı", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Blog Başlıkları", fontsize=12)  # Y ekseni etiketi
    plt.grid(axis='x', linestyle='--', alpha=0.7)  # X ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("en_populer_blog_grafik.png", dpi=300)
    plt.show()


# Fonksiyonu çağırma
# en_populer_blog_grafik(blog_icerikleri)

#####################################################################################################################
# 5. Yorum sayısı ve en çok yorum alan blog

def blog_yorum_sayilari_grafik(blog_icerikleri):
    """
    Blog içeriklerini analiz ederek her blogun yorum sayısını hesaplar,
    en çok yorum alan blogu belirler ve çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.

    Çıktı:
        Her blogun yorum sayısı ve en çok yorum alan blog konsola yazdırılır.
        Yorum sayıları çubuk grafikle görselleştirilir.
    """
    print("\nBloglara göre yorum sayıları:")

    # En çok yorum alan blogu belirlemek için değişkenler
    en_cok_yorum = 0
    en_cok_yorum_blog = None

    # Yorum sayılarını hesaplama
    yorum_sayilari = {}
    for blog in blog_icerikleri:
        yorum_sayisi = len(blog["yorumlar"])
        print(f"Başlık: {blog['baslik']}, Yorum Sayısı: {yorum_sayisi}")
        yorum_sayilari[blog["baslik"]] = yorum_sayisi

        if yorum_sayisi > en_cok_yorum:
            en_cok_yorum = yorum_sayisi
            en_cok_yorum_blog = blog

    # En çok yorum alan blogu yazdırma
    print(f"\nEn çok yorum alan blog: {en_cok_yorum_blog['baslik']} ({en_cok_yorum} yorum)")

    # Verileri hazırlama
    blog_basliklari = list(yorum_sayilari.keys())  # Blog başlıkları
    yorum_sayilari_listesi = list(yorum_sayilari.values())  # Yorum sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.bar(blog_basliklari, yorum_sayilari_listesi, color='lightblue', edgecolor='black')  # Çubuk grafik
    plt.title("Bloglara Göre Yorum Sayıları", fontsize=14)  # Grafik başlığı
    plt.xlabel("Blog Başlıkları", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Yorum Sayısı", fontsize=12)  # Y ekseni etiketi
    plt.xticks(rotation=30, fontsize=10)  # X ekseni yazılarının döndürülmesi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("blog_yorum_sayilari_grafik.png", dpi=300)
    plt.show()

# Fonksiyonu çağırma
# blog_yorum_sayilari_grafik(blog_icerikleri)

#####################################################################################################################
# 6. cok kullanılan kelimeleri analiz etme

def cok_kullanilan_kelimeler_grafik(blog_icerikleri, kelime_sayisi=5):
    """
    Blog içeriklerinde cok kullanılan kelimeleri analiz eder ve çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.
        kelime_sayisi (int): Görselleştirilmek istenen en cok kullanılan kelime sayısı (varsayılan: 5).

    Çıktı:
        En cok kullanılan kelimeler konsola yazdırılır.
        cok kullanılan kelimeler çubuk grafikle görselleştirilir.
    """
    print("\nBlog içeriklerinde cok kullanılan kelimeler:")

    # Tüm kelimeleri toplama
    tum_kelimeler = []
    for blog in blog_icerikleri:
        kelimeler = blog["icerik"].lower().split()  # İçeriği küçük harfe çevir ve kelimelere ayır
        tum_kelimeler.extend(kelimeler)

    # Kelime frekanslarını hesaplama
    kelime_sayilari = Counter(tum_kelimeler)
    en_cok_kelimeler = kelime_sayilari.most_common(kelime_sayisi)

    # En cok kullanılan kelimeleri konsola yazdırma
    for kelime, sayi in en_cok_kelimeler:
        print(f"{kelime}: {sayi} kez")

    # Verileri hazırlama
    kelimeler = [kelime for kelime, _ in en_cok_kelimeler]
    kullanim_sayilari = [sayi for _, sayi in en_cok_kelimeler]

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.bar(kelimeler, kullanim_sayilari, color='salmon', edgecolor='black')  # Çubuk grafik
    plt.title(f"En cok Kullanılan {kelime_sayisi} Kelime", fontsize=14)  # Grafik başlığı
    plt.xlabel("Kelime", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Kullanım Sayısı", fontsize=12)  # Y ekseni etiketi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("kullanici_yorum_sayilari_grafik.png", dpi=300)  # Grafik kaydetme
    plt.show()

# Fonksiyonu çağırma
# cok_kullanilan_kelimeler_grafik(blog_icerikleri, kelime_sayisi=5)

#####################################################################################################################
# 7. Kullanıcıların yaptığı toplam yorum sayısı
def kullanici_yorum_sayilari_grafik(blog_icerikleri):
    """
    Blog içeriklerinden kullanıcıların yaptığı toplam yorum sayılarını analiz eder
    ve bunu çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.

    Çıktı:
        Kullanıcıların yaptığı toplam yorum sayısı konsola yazdırılır.
        Kullanıcıların yaptığı yorum sayıları çubuk grafikle görselleştirilir.
    """
    print("\nKullanıcıların yaptığı toplam yorum sayısı:")

    # Kullanıcı yorum sayılarını hesaplama
    kullanici_yorum_sayilari = {}
    for blog in blog_icerikleri:
        for yorum in blog["yorumlar"]:
            kullanici = yorum["kullanici"]
            kullanici_yorum_sayilari[kullanici] = kullanici_yorum_sayilari.get(kullanici, 0) + 1

    # Kullanıcıların yaptığı toplam yorum sayılarını yazdırma
    for kullanici, sayi in kullanici_yorum_sayilari.items():
        print(f"{kullanici}: {sayi} yorum")

    # Verileri hazırlama
    kullanicilar = list(kullanici_yorum_sayilari.keys())  # Kullanıcı isimleri
    yorum_sayilari = list(kullanici_yorum_sayilari.values())  # Yorum sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.bar(kullanicilar, yorum_sayilari, color='lightblue', edgecolor='black')  # Çubuk grafik
    plt.title("Kullanıcıların Yaptığı Toplam Yorum Sayısı", fontsize=14)  # Grafik başlığı
    plt.xlabel("Kullanıcılar", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Yorum Sayısı", fontsize=12)  # Y ekseni etiketi
    plt.xticks(rotation=30, fontsize=10)  # X ekseni yazılarının döndürülmesi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("kullanici_yorum_sayilari.png", dpi=300)  # Grafik kaydetme
    plt.show()

# Fonksiyonu çağırma
# kullanici_yorum_sayilari_grafik(blog_icerikleri)

#####################################################################################################################
# 8. Yazarların ortalama blog görüntülenme sayısı

def yazar_ortalama_goruntulenme_grafik(blog_icerikleri):
    """
    Blog içeriklerinden yazarların ortalama blog görüntülenme sayılarını analiz eder
    ve bunu çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.

    Çıktı:
        Yazarların ortalama blog görüntülenme sayısı konsola yazdırılır.
        Ortalama görüntülenme sayıları çubuk grafikle görselleştirilir.
    """
    print("\nYazarların ortalama blog görüntülenme sayısı:")

    # Yazarların görüntülenme sayılarını toplama
    yazar_goruntulenmeleri = {}
    for blog in blog_icerikleri:
        yazar = blog["yazar"]
        goruntulenme = blog["goruntulenme"]
        if yazar not in yazar_goruntulenmeleri:
            yazar_goruntulenmeleri[yazar] = []
        yazar_goruntulenmeleri[yazar].append(goruntulenme)

    # Ortalama görüntülenme sayılarını hesaplama
    yazar_ortalama_goruntulenme = {}
    for yazar, goruntulenmeler in yazar_goruntulenmeleri.items():
        ortalama_goruntulenme = sum(goruntulenmeler) / len(goruntulenmeler)
        yazar_ortalama_goruntulenme[yazar] = ortalama_goruntulenme
        print(f"{yazar}: {ortalama_goruntulenme:.2f} görüntülenme")

    # Verileri hazırlama
    yazarlar = list(yazar_ortalama_goruntulenme.keys())  # Yazar isimleri
    ortalama_goruntulenmeler = list(yazar_ortalama_goruntulenme.values())  # Ortalama görüntülenmeler

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.bar(yazarlar, ortalama_goruntulenmeler, color='lightgreen', edgecolor='black')  # Çubuk grafik
    plt.title("Yazarların Ortalama Blog Görüntülenme Sayısı", fontsize=14)  # Grafik başlığı
    plt.xlabel("Yazarlar", fontsize=12)  # X ekseni etiketi
    plt.ylabel("Ortalama Görüntülenme", fontsize=12)  # Y ekseni etiketi
    plt.xticks(rotation=30, fontsize=10)  # X ekseni yazılarının döndürülmesi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("yazar_ortalama_goruntulenme.png", dpi=300)  # Grafik kaydetme
    plt.show()

# Fonksiyonu çağırma
# yazar_ortalama_goruntulenme_grafik(blog_icerikleri)

#####################################################################################################################
# 9. Belirli bir kelimenin geçtiği blogları bulma
def kelime_gecen_bloglar_grafik(blog_icerikleri, aranan_kelime):
    """
    Belirli bir kelimenin geçtiği blogları analiz eder ve bu blogları çubuk grafikle görselleştirir.

    Parametre:
        blog_icerikleri (list): Blog verilerinin bulunduğu liste.
        aranan_kelime (str): Aranan kelime.

    Çıktı:
        Kelimenin geçtiği blog başlıkları ve yazarları konsola yazdırılır.
        Blog başlıkları çubuk grafikle görselleştirilir.
    """
    print(f"\n'{aranan_kelime}' kelimesinin geçtiği bloglar:")

    # Kelimenin geçtiği blogları bulma
    kelime_gecen_bloglar = [blog for blog in blog_icerikleri if aranan_kelime.lower() in blog["icerik"].lower()]

    # Kelimenin geçtiği blogları konsola yazdırma
    if not kelime_gecen_bloglar:
        print(f"Hiçbir blogda '{aranan_kelime}' kelimesi geçmiyor.")
        return

    for blog in kelime_gecen_bloglar:
        print(f"Başlık: {blog['baslik']}, Yazar: {blog['yazar']}")

    for blog in kelime_gecen_bloglar:
        print(f"goruntulenme Sayısı: {blog["goruntulenme"]}")

    # Verileri hazırlama
    blog_basliklari = [blog["baslik"] for blog in kelime_gecen_bloglar]  # Blog başlıkları
    goruntulenme_sayilari = [blog["goruntulenme"] for blog in kelime_gecen_bloglar]  # Görüntülenme sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))  # Grafik boyutu
    plt.bar(blog_basliklari, goruntulenme_sayilari, color='lightcoral', edgecolor='black')  # Çubuk grafik
    plt.title(f"'{aranan_kelime}' Kelimesinin Geçtiği Bloglar", fontsize=14)  # Grafik başlığı
    plt.xlabel("Blog Başlıkları ve Yazar:" + blog['yazar'], fontsize=12)  # X ekseni etiketi
    plt.ylabel("Görüntülenme Sayısı", fontsize=12)  # Y ekseni etiketi
    plt.xticks(rotation=20, fontsize=10)  # X ekseni yazılarının döndürülmesi
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara
    plt.tight_layout()  # Grafik düzeni
    plt.savefig("kelime_gecen_bloglar.png", dpi=300)  # Grafik kaydetme
    plt.show()

# Fonksiyonu çağırma
# kelime_gecen_bloglar_grafik(blog_icerikleri, "Python")

################################################################################################
#  10 Bloglarda En Çok Görüntülenme Sayısına Göre İlk 3 Blog
def birlestirilmis_goruntulenme(blog_icerikleri):
    """
    Aynı başlığa sahip blogların görüntülenme sayılarını birleştirir.
    """
    birlestirilmis = {}
    for blog in blog_icerikleri:
        baslik = blog["baslik"]
        goruntulenme = blog["goruntulenme"]
        birlestirilmis[baslik] = birlestirilmis.get(baslik, 0) + goruntulenme

    # Blogları sözlükten listeye çevir
    birlestirilmis_bloglar = [{"baslik": k, "goruntulenme": v} for k, v in birlestirilmis.items()]
    return birlestirilmis_bloglar


def en_populer_uc_blog(blog_icerikleri):
    # Aynı başlıkları birleştirme
    birlestirilmis_bloglar = birlestirilmis_goruntulenme(blog_icerikleri)

    # En popüler ilk 3 blogu seçme
    en_populer_bloglar = sorted(birlestirilmis_bloglar, key=lambda x: x["goruntulenme"], reverse=True)[:3]

    # Sonuçları yazdırma
    print("\nEn Popüler İlk 3 Blog:")
    for blog in en_populer_bloglar:
        print(f"Başlık: {blog['baslik']}, Görüntülenme: {blog['goruntulenme']}")

    # Görselleştirme
    blog_basliklari = [blog["baslik"] for blog in en_populer_bloglar]
    goruntulenme_sayilari = [blog["goruntulenme"] for blog in en_populer_bloglar]

    plt.figure(figsize=(10, 6))
    plt.bar(blog_basliklari, goruntulenme_sayilari, color='gold', edgecolor='black')
    plt.title("En Çok Görüntülenen İlk 3 Blog", fontsize=14)
    plt.xlabel("Blog Başlıkları", fontsize=12)
    plt.ylabel("Görüntülenme Sayısı", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# en_populer_uc_blog(blog_icerikleri)

################################################################################################
# 11-) Bloglarda yorum sayılarının ortalamasını hesaplayın.
# Bu ortalamanın üstünde veya altında kalan blogları tespit edin.

def ortalama_yorum_sayisi_grafik(blog_icerikleri):
    # Toplam yorum sayısını ve ortalamayı hesaplama
    toplam_yorum = sum(len(blog["yorumlar"]) for blog in blog_icerikleri)
    ortalama = toplam_yorum / len(blog_icerikleri)
    toplam_blog = len(blog_icerikleri)

    print(f"Toplam Blog Sayısı: {toplam_blog}")
    print(f"Ortalama Yorum Sayısı: {ortalama:.2f}")

    # Blogları gruplandırma
    ust_bloglar = [blog for blog in blog_icerikleri if len(blog["yorumlar"]) > ortalama]
    alt_bloglar = [blog for blog in blog_icerikleri if len(blog["yorumlar"]) <= ortalama]

    # Sonuçları yazdırma
    print("\nOrtalamanın Üzerinde Yorum Alan Bloglar:")
    for blog in ust_bloglar:
        print(blog["baslik"])

    print("\nOrtalamanın Altında veya Eşit Yorum Alan Bloglar:")
    for blog in alt_bloglar:
        print(blog["baslik"])

    # Görselleştirme verileri hazırlama
    blog_kategorileri = ["Üzerinde", "Altında veya Eşit"]
    blog_sayilari = [len(ust_bloglar), len(alt_bloglar)]

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 7))
    plt.bar(blog_kategorileri, blog_sayilari, color=['green', 'red'], edgecolor='black')

    # Başlık ve açıklamalar
    plt.title(
        f"Blogların Ortalama Yorum Sayısına Göre Dağılımı\n"
        f"Toplam Blog Sayısı: {toplam_blog} | Ortalama Yorum Sayısı: {ortalama:.2f}",
        fontsize=14,
    )
    plt.xlabel("Yorum Durumu", fontsize=12)
    plt.ylabel("Blog Sayısı", fontsize=12)

    # Y ekseni için ızgara çizgileri
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Değerlerin çubuk üzerine eklenmesi
    for i, sayi in enumerate(blog_sayilari):
        plt.text(i, sayi + 0.1, str(sayi), ha='center', fontsize=12, color='black', fontweight='bold')

    # Grafik düzeni ve gösterimi
    plt.tight_layout()
    plt.show()

#
# ortalama_yorum_sayisi_grafik(blog_icerikleri)
################################################################################################
# 12- Kullanıcıların Yorum Yaptığı Blog Sayıları
# Her bir kullanıcının kaç farklı bloga yorum yaptığını analiz edin.
# Kullanıcıların en çok hangi kategorilerde yorum yaptığına dair bilgiler sunun.
import matplotlib.pyplot as plt

def kullanici_blog_sayilari_grafik(blog_icerikleri):
    """
    Kullanıcıların yorum yaptığı blog sayılarını analiz eder ve görselleştirir.
    """
    # Kullanıcıların blog sayısını hesaplama
    kullanici_blog_sayilari = {}
    for blog in blog_icerikleri:
        for yorum in blog["yorumlar"]:
            kullanici = yorum["kullanici"]
            kullanici_blog_sayilari[kullanici] = kullanici_blog_sayilari.get(kullanici, set())
            kullanici_blog_sayilari[kullanici].add(blog["blog_id"])

    # Kullanıcı ve yorum yaptığı blog sayısını konsola yazdırma
    for kullanici, bloglar in kullanici_blog_sayilari.items():
        print(f"{kullanici}: {len(bloglar)} bloga yorum yapmış.")

    # Verileri hazırlama
    kullanicilar = list(kullanici_blog_sayilari.keys())  # Kullanıcı isimleri
    blog_sayilari = [len(bloglar) for bloglar in kullanici_blog_sayilari.values()]  # Blog sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))
    plt.bar(kullanicilar, blog_sayilari, color='skyblue', edgecolor='black')

    # Grafik başlık ve etiketleri
    plt.title("Kullanıcıların Yorum Yaptığı Blog Sayıları", fontsize=14)
    plt.xlabel("Kullanıcılar", fontsize=12)
    plt.ylabel("Blog Sayısı", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)  # X ekseni yazılarını döndürme
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara çizgileri

    # Çubukların üstüne değer ekleme
    for i, sayi in enumerate(blog_sayilari):
        plt.text(i, sayi + 0.1, str(sayi), ha='center', fontsize=10, color='black', fontweight='bold')

    # Grafik düzeni ve gösterimi
    plt.tight_layout()
    plt.show()

#
# kullanici_blog_sayilari_grafik(blog_icerikleri)
################################################################################################
# 13-)
# Her kategorinin toplam ve ortalama görüntülenme sayılarını hesaplayın.
# En çok görüntülenme ortalamasına sahip kategoriyi bulun.

def kategori_ortalama_goruntulenme_grafik(blog_icerikleri):
    """
    Kategorilere göre ortalama görüntülenme sayısını hesaplar ve çubuk grafikle görselleştirir.
    Ayrıca toplam blog ve kategori sayısını grafiğe ekler.
    """
    # Kategorilere göre görüntülenme verilerini toplama
    kategori_goruntulenme = {}
    for blog in blog_icerikleri:
        kategori = blog["kategori"]
        kategori_goruntulenme.setdefault(kategori, []).append(blog["goruntulenme"])

    # Kategorilere göre ortalama görüntülenme hesaplama
    kategori_ortalama = {}
    toplam_blog = len(blog_icerikleri)
    toplam_kategori = len(kategori_goruntulenme)
    for kategori, goruntulenmeler in kategori_goruntulenme.items():
        ortalama = sum(goruntulenmeler) / len(goruntulenmeler)
        kategori_ortalama[kategori] = ortalama
        print(f"{kategori}: Ortalama Görüntülenme = {ortalama:.2f}")

    print(f"\nToplam Blog Sayısı: {toplam_blog}")
    print(f"Toplam Kategori Sayısı: {toplam_kategori}")

    # Verileri hazırlama
    kategoriler = list(kategori_ortalama.keys())  # Kategorilerin isimleri
    ortalamalar = list(kategori_ortalama.values())  # Ortalama görüntülenme sayıları

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))
    plt.bar(kategoriler, ortalamalar, color='lightcoral', edgecolor='black')

    # Grafik başlık ve etiketleri
    plt.title(
        f"Kategorilere Göre Ortalama Görüntülenme\n"
        f"Toplam Blog Sayısı: {toplam_blog} | Toplam Kategori Sayısı: {toplam_kategori}",
        fontsize=14
    )
    plt.xlabel("Kategoriler", fontsize=12)
    plt.ylabel("Ortalama Görüntülenme Sayısı", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)  # X ekseni yazılarını döndürme
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Y ekseni için ızgara çizgileri

    # Çubukların üstüne değer ekleme
    for i, ortalama in enumerate(ortalamalar):
        plt.text(i, ortalama + 10, f"{ortalama:.2f}", ha='center', fontsize=10, color='black', fontweight='bold')

    # Grafik düzeni ve gösterimi
    plt.tight_layout()
    plt.show()


#kategori_ortalama_goruntulenme_grafik(blog_icerikleri)
################################################################################################
# 14-) Blog içeriklerinden en çok kullanılan ikili kelimeleri bulun ve sıklıklarını görselleştirin.

import matplotlib.pyplot as plt
from collections import Counter

import matplotlib.pyplot as plt
from collections import Counter


def en_cok_ikili_kelimeler_grafik(blog_icerikleri, kelime_sayisi=5):
    tum_bigrames = []

    # Tüm blog içeriklerinden bigram'leri toplama
    for blog in blog_icerikleri:
        kelimeler = blog["icerik"].lower().strip().split()
        tum_bigrames.extend(zip(kelimeler, kelimeler[1:]))

    # Bigram frekanslarını hesaplama
    bigram_sayilari = Counter(tum_bigrames)
    en_cok_bigrames = bigram_sayilari.most_common(kelime_sayisi)

    # En çok kullanılan bigram'leri konsola yazdırma
    print("\nEn Çok Kullanılan İkili Kelimeler:")
    for bigram, sayi in en_cok_bigrames:
        print(f"{' '.join(bigram)}: {sayi} kez")

    # Verileri hazırlama
    bigram_kelimeler = [' '.join(bigram) for bigram, _ in en_cok_bigrames]
    bigram_frekanslari = [sayi for _, sayi in en_cok_bigrames]

    # Kontrol
    print("Bigram Kelimeler (Grafik):", bigram_kelimeler)
    print("Bigram Frekansları (Grafik):", bigram_frekanslari)

    # Çubuk grafik çizimi
    plt.figure(figsize=(10, 6))
    plt.bar(bigram_kelimeler, bigram_frekanslari, color='lightblue', edgecolor='black')

    # Grafik başlık ve etiketleri
    plt.title("En Çok Kullanılan İkili Kelimeler", fontsize=14)
    plt.xlabel("İkili Kelimeler", fontsize=12)
    plt.ylabel("Frekans", fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Çubukların üstüne değer ekleme
    for i, frekans in enumerate(bigram_frekanslari):
        plt.text(i, frekans + 0.5, str(frekans), ha='center', fontsize=10, color='black', fontweight='bold')

    # Grafik düzeni ve gösterimi
    plt.tight_layout()
    plt.show()

#
# en_cok_ikili_kelimeler_grafik(blog_icerikleri, kelime_sayisi=5)


################################################################################################
################################################################################################
"""
1. Kütüphane Kurulumu
Eğer bu kütüphaneler kurulu değilse, önce aşağıdaki komutlarla kurulum yapabilirsiniz:
pip install matplotlib seaborn
"""
