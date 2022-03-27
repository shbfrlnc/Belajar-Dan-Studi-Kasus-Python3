# Belajar Python3 wxPython Scrapy Simple Spider

Tujuan dibuatnya source code ini adalah untuk mempelajari cara mem-passing data dari scrapy ke wxPython, dalam hal ini ke rich text control nya.

## Untuk Menjalankannya

Pertama, pastikan Python 3.9 sudah terinstall di OS Anda.

Download folder ini.

Kemudian buka foldernya dengan perintah:

```
cd belajar_python3_wxpython_scrapy_simple_spider
```

Kemudian jalankan:

```
python -m venv ./venv
./venv/Scripts/activate
```

Lalu install requirements.txt:

```
pip install -r requirements.txt 
```

Selanjutnya, Anda bisa langsung coba:

```
python src/wxscrapy.py
```

## Untuk Membuild Jadi Executable

Jalankan:

```
pyinstaller src/wxscrapy.py
```

## Catatan

Hanya telah diuji di Windows 10.
