# Belajar Python3 wxPython Scrapy Simple Spider

## Cara Mencoba Kode Ini

Pertama, pastikan Python 3.8 sudah terinstall di OS Anda.

Download folder ini.

Selanjutnya, Anda bisa langsung coba:

```
python contoh_modul_os.py
```

## Pendahuluan

Di Python 3, modul os adalah modul yang berguna untuk melakukan prosedur yang tergantung pada os. 

## Penjelasan

Penjelasannya ada pada komentar di potongan kode berikut ini.

```
# file: contoh_modul_os.py

# begin: import modules
import os
# end: import modules

# memprint nama OS
print(os.name)

# memprint current working directory
print(os.getcwd())

# memprint absolute path dari directory saat ini
print(os.path.abspath('.'))

# melisting files dan sub-directory di directory saat ini
print(os.listdir('.'))

# me-rename file
if os.path.isfile("sample.txt") :
    os.rename("sample.txt","renamed.txt")
elif os.path.isfile("renamed.txt") :
    os.rename("renamed.txt","sample.txt"))
```
