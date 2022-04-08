# Belajar Python3 Modul os

## Cara Mencoba Kode Ini

Pertama, pastikan Python 3.8 sudah terinstall di OS Anda.

Download folder ini.

Selanjutnya, Anda bisa langsung coba:

```
python pengguna_modul_sendiri.py
```

## Pendahuluan

Di Python 3, modul sendiri adalah modul Python 3 yang dibuat oleh kita sendiri. Sebagai modul, modul bisa dijalankan juga sebagai program utama selain menjadi program sampingan yang baru dijalankan setelah diimport. 

## Penjelasan

Penjelasannya ada pada komentar di potongan kode berikut ini.

```
# file: contoh_modul_sendiri.py

# buat fungsi untuk memprint "modul yang bagus"
def nama_modul_saya():
    print("modul yang bagus")

# jika ini program utama
if __name__ == "__main__":
    # jalankan fungsi nama_modul_saya()
    # coba anda jalankan langsung:
    # python contoh_modul_sendiri.py
    nama_modul_saya()
```

```
# file: pengguna_modul_sendiri.py

# import modul sendiri: contoh_modul_sendiri
# kemudian ambil fungsi nama_modul_saya
from contoh_modul_sendiri import nama_modul_saya

# jalankan fungsi nama_modul_saya
# maka hanya ada satu baris teks,
# karena eksekusi kode di bagian terbawah script contoh_modul_sendiri.py
# terproteksi oleh:
# if __name__ == "__main__":
# pada script contoh_modul_sendiri.py
nama_modul_saya()
```
