# Belajar Python3 Modul json

## Cara Mencoba Kode Ini

Pertama, pastikan Python 3.8 sudah terinstall di OS Anda.

Download folder ini.

Selanjutnya, Anda bisa langsung coba:

```
python contoh_modul_json.py
```

## Pendahuluan

Di Python 3, modul json adalah modul yang berguna untuk melakukan encoding dan decoding json. 

## Penjelasan

Penjelasannya ada pada komentar di potongan kode berikut ini.

```
# file: contoh_modul_json.py

# begin: import modules
import json
# end: import modules

# memprint teks "json ke python"
print("json ke python")

# data dalam format json
data_json = '{"nama" : "toko buku", "produk":"buku", "jumlahProduk" : "3"}'

# data barusan dikonversi ke python
data_di_python = json.loads(data_json)

# print semuanya
print(data_di_python)

# print nama
print(data_di_python["nama"])

# print jumlahProduk
print(data_di_python["jumlahProduk"])

# memprint teks "python ke json"
print("python ke json")

# data dalam python
data_python = {
  "nama": "suatu_aplikasi",
  "kode_versi": 40,
  "portable": True,
  "requirement": ("opencv","numpy")
}

# data barusan dikonversi menjadi json
data_di_json = json.dumps(data_python)

# mem-print hasilnya
print(data_di_json)
```
