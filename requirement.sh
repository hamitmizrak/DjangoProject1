#!/bin/bash

# Renk Kodları
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
#############################################################################

# Script Ayarları
set -e  # Hata durumunda scripti durdur

#############################################################################
# 1. GLOBAL YÜKLEME: Sisteme global kütüphane yükleme
function install_global() {
    echo -e "${GREEN}Global olarak Python kütüphaneleri yükleniyor...${NC}"
    pip install matplotlib
    #pip install matplotlib seaborn numpy pandas scipy requests flask django
    echo -e "${GREEN}Global yükleme tamamlandı!${NC}"
    ls venv
}

#############################################################################
# 2. LOKAL YÜKLEME: Sanal ortam oluştur ve kütüphaneleri yükle
# Python projelerinde, bağımlılıkları yönetmek için bir sanallaştırılmış ortam (virtual environment) kullanmak önemlidir.
function linux_create_and_install_local() {
    python --version
    local ENV_NAME="myenv"

    echo -e "${YELLOW} Linux ortamı için Yerel (sanal ortam) yükleme başlatılıyor...${NC}"
    python3 -m venv $ENV_NAME
    source $ENV_NAME/bin/activate
    echo "Sanal ortam aktif: $ENV_NAME"
    # echo -e "${YELLOW}Sanal ortam aktif: $ENV_NAME${NC}"
    pip install matplotlib
    #pip install matplotlib numpy pandas scipy requests flask django
    echo -e "${YELLOW}Kütüphane yüklemeleri tamamlandı!${NC}"
    ls venv

}

#############################################################################
# 3. LOKAL YÜKLEME: Sanal ortam oluştur ve kütüphaneleri yükle
# Python projelerinde, bağımlılıkları yönetmek için bir sanallaştırılmış ortam (virtual environment) kullanmak önemlidir.
function windows_create_and_install_local() {
    python --version
    local ENV_NAME="myenv"

    echo -e "${YELLOW}Windows ortamı için Yerel (sanal ortam) yükleme başlatılıyor...${NC}"
    python -m venv $ENV_NAME

    # Sanal ortamı etkinleştir (Windows için uygun yol)
    source $ENV_NAME/Scripts/activate

    echo -e "${YELLOW}Sanal ortam aktif: $ENV_NAME${NC}"
    pip install matplotlib
    # pip install matplotlib numpy pandas scipy requests flask django
    echo -e "${YELLOW}Kütüphane yüklemeleri tamamlandı!${NC}"
    ls $ENV_NAME
}


#############################################################################
# 3. LOKAL SANAL KAPATMA: SGenel kurulum yapmak istiyorsak local kapatmalısın
function deactivate_local() {
    echo -e "${BLUE}Sanal ortam kapatılıyor...${NC}"
    deactivate
    echo -e "${BLUE}Sanal ortam kapatıldı!${NC}"
}


#############################################################################
# 4. MEVCUT KÜTÜPHANELERİ LİSTELEME: Yüklü paketleri listele
function list_installed_packages() {
    echo -e "${CYAN}Yüklü Python kütüphaneleri listeleniyor...${NC}"
    pip list
}


#############################################################################
# 5. KÜTÜPHANE BİLGİSİ: Belirli bir kütüphanenin detaylarını görüntüle
function show_package_info() {
    python --version
    read -p "Bilgilerini görmek istediğiniz kütüphanenin adını girin: " PACKAGE_NAME
    echo "Kütüphane bilgileri: $PACKAGE_NAME"
    pip show $PACKAGE_NAME
}


#############################################################################
# 6. KÜTÜPHANE KALDIRMA: Belirli bir kütüphaneyi kaldır
function uninstall_package() {
    read -p "Kaldırmak istediğiniz kütüphanenin adını girin: " PACKAGE_NAME
    echo -e "${RED}$PACKAGE_NAME kütüphanesi kaldırılıyor...${NC}"
    pip uninstall -y $PACKAGE_NAME
    echo -e "${RED}$PACKAGE_NAME başarıyla kaldırıldı.${NC}"
}


#############################################################################
# 7. KÜTÜPHANE GÜNCELLEME: Belirli bir kütüphaneyi güncelle
function upgrade_package() {
    read -p "Güncellemek istediğiniz kütüphanenin adını girin: " PACKAGE_NAME
    echo -e "${GREEN}$PACKAGE_NAME kütüphanesi güncelleniyor...${NC}"
    pip install --upgrade $PACKAGE_NAME
    echo -e "${GREEN}$PACKAGE_NAME başarıyla güncellendi.${NC}"
}


#############################################################################
# 8. MEVCUT SANAL ORTAMLARI LİSTELEME
function list_virtualenvs() {
    python --version
    echo -e "${YELLOW}Mevcut sanal ortamlar:${NC}"
    ls -d */ | grep "env"
}


#############################################################################
# 9. SANAL ORTAM SİLME
function delete_virtualenv() {
    read -p "Silmek istediğiniz sanal ortamın adını girin: " ENV_NAME
    if [ -d "$ENV_NAME" ]; then
        rm -rf $ENV_NAME
        echo -e "${RED}$ENV_NAME silindi.${NC}"
    else
        echo -e "${RED}Sanal ortam bulunamadı.${NC}"
    fi
}

#############################################################################
# 10. TÜM KÜTÜPHANELERİ GÜNCELLEME
function upgrade_all_packages() {
    echo -e "${GREEN}Tüm kütüphaneler güncelleniyor...${NC}"
    pip list --outdated | awk '{print $1}' | tail -n +3 | xargs -n1 pip install --upgrade
    echo -e "${GREEN}Güncellemeler tamamlandı!${NC}"
}


#############################################################################
# 11. GEREKSİNİMLERİ YÜKLEME: requirements.txt dosyasından yükle
function install_requirements() {
    if [ -f "requirements.txt" ]; then
        echo -e "${BLUE}requirements.txt dosyasından kütüphaneler yükleniyor...${NC}"
        pip install -r requirements.txt
    else
        echo -e "${RED}requirements.txt bulunamadı.${NC}"
    fi
}


#############################################################################
# 12. YÜKLÜ KÜTÜPHANELERİ requirements.txt OLARAK KAYDETME
function export_requirements() {
    echo -e "${CYAN}Yüklü kütüphaneler requirements.txt dosyasına kaydediliyor...${NC}"
    pip freeze > requirements.txt
    echo -e "${CYAN}requirements.txt oluşturuldu.${NC}"
}


#############################################################################
# 13. PYTHON VE pip SÜRÜM KONTROLÜ
function check_versions() {
    echo -e "${BLUE}Python sürümü:${NC}"
    python3 --version
    echo -e "${BLUE}pip sürümü:${NC}"
    pip --version
}


#############################################################################
# ANA MENU
while true; do
    # Menü Başlığı
    echo -e "\n${CYAN}Python kütüphane yönetim scriptine hoş geldiniz!${NC}"

    # Menü Seçenekleri
    echo -e "${GREEN}1 - Global yükleme${NC}"
    echo -e "${YELLOW}2 - Linux Local - Yerel (sanal ortamda) yükleme${NC}"
    echo -e "${YELLOW}3 - Windows Local - Yerel (sanal ortamda) yükleme${NC}"
    echo -e "${YELLOW}4 - Local - Yerel (sanal ortamda) Kapatma${NC}"
    echo -e "${BLUE}5 - Yüklü kütüphaneleri listele (pip list)${NC}"
    echo -e "${CYAN}6 - Kütüphane bilgilerini görüntüle (pip show)${NC}"
    echo -e "${RED}7 - Kütüphane kaldır (pip uninstall)${NC}"
    echo -e "${GREEN}8 - Kütüphane güncelle (pip install --upgrade)${NC}"
    echo -e "${YELLOW}9 - Mevcut sanal ortamları listele${NC}"
    echo -e "${YELLOW}10 - Sanal ortamı sil${NC}"
    echo -e "${BLUE}11 - Gereksinimleri yükle (requirements.txt)${NC}"
    echo -e "${CYAN}12 - Yüklü kütüphaneleri kaydet (requirements.txt)${NC}"
    echo -e "${GREEN}13 - Tüm kütüphaneleri güncelle${NC}"
    echo -e "${BLUE}14 - Python ve pip sürüm kontrolü${NC}"
    echo -e "${RED}15 - Çıkış${NC}"

    read -p "Seçiminizi yapın (1-13): " CHOICE

    case $CHOICE in
        1)
            install_global
            ;;
        2)
            windows_create_and_install_local
            ;;
        3)
            linux_create_and_install_local
            ;;
        4)
            list_installed_packages
            ;;
        5)
            list_installed_packages
            ;;
        6)
            show_package_info
            ;;
        7)
            uninstall_package
            ;;
        8)
            upgrade_package
            ;;
        9)
            list_virtualenvs
            ;;
        10)
            delete_virtualenv
            ;;
        11)
            install_requirements
            ;;
        12)
            export_requirements
            ;;
        13)
            upgrade_all_packages
            ;;
        14)
            check_versions
            ;;
        15)
            echo "Çıkış yapılıyor..."
            exit 0
            ;;
        *)
            echo "Geçersiz seçim! Lütfen 1-13 arasında bir değer girin."
            ;;
    esac
done
