# Belajar Python3 wxPython Scrapy Simple Spider

## Cara Mencoba Kode Ini

Pertama, pastikan Python 3.8 sudah terinstall di OS Anda.

Download folder ini.

Selanjutnya, Anda bisa langsung coba:

```
python contoh_urllib.py
```

## Pendahuluan

Di Python 3, urllib adalah modul yang digunakan untuk menangani URL.

Selain itu, modul ini juga bisa digunakan untuk membuat request.

Dalam contoh kali ini, kita mencoba untuk membuka website:

https://quotes.toscrape.com

## Penjelasan

Penjelasannya ada pada komentar di potongan kode berikut ini.

```
# file: contoh_urllib.py

# begin: import modules
import urllib.request
# end: import modules

# memprint teks: "mulai contoh 1"
print("mulai contoh 1")

# membuka halaman homepage dari https://quotes.toscrape.com
html = urllib.request.urlopen('https://quotes.toscrape.com').read()
# memprint outputnya.
print(html)

# memprint teks: "mulai contoh 2"
print("mulai contoh 2")

# begin: memberi nilai pada http header, dalam hal ini user agent nya
headers = {}
# nilai user agent browser saya. bisa dicari di google
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"
# end: memberi nilai pada http header, dalam hal ini user agent nya

# membuka halaman homepage dari https://quotes.toscrape.com
# kali ini disertai header
req = urllib.request.Request('https://quotes.toscrape.com', headers = headers)
html = urllib.request.urlopen(req).read()
# memprint outputnya.
print(html)
```
