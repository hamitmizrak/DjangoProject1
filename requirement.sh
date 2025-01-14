#!/bin/bash

################################################################
# Sanal ortam oluşturma
# Python projelerinde, bağımlılıkları yönetmek için bir sanallaştırılmış ortam (virtual environment) kullanmak önemlidir.
# Bu, projeniz için bir venv adlı sanal ortam oluşturur.
python -m venv venv
ls venv

################################################################
# Platforma göre sanal ortamı aktifleştirme
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate  # Linux/MacOS
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    venv\Scripts\activate  # Windows
else
    echo "Platform desteklenmiyor."
    exit 1
fi

################################################################
# Bağımlılıkları Yükleme
#pip install Flask
#pip install matplotlib
#pip install seaborn
#pip install matplotlib seaborn
pip install -r requirements.txt

