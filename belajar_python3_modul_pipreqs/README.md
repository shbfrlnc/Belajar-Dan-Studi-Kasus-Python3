# Belajar Python3 Modul pipreqs

## Cara Mencoba Kode Ini

Tidak ada kode dalam project ini.

## Pendahuluan

Di Python 3, pipreqs adalah modul yang berguna untuk membuat requirements.txt dalam scope project.

Artinya, berbeda dengan pip freeze yang juga memasukkan daftar modul Python yang tidak digunakan dalam project.

## Penjelasan

Untuk menginstall pipreqs:

```
pip install pipreqs
```

Untuk membuat requirements.txt, masuk ke dalam folder project kemudian (perhatikan ada tanda titik di sebelah pipreqs. Itu maksudnya adalah folder Anda saat ini):

```
pipreqs .
```

Nanti requirements akan dimasukkan ke requirements.txt.

Selanjutnya, saat project akan dikerjakan di komputer lain, Anda tinggal masuk ke dalam folder di mana ada requirements.txt dan jalankan perintah:

```
pip install -r requirements.txt
```
