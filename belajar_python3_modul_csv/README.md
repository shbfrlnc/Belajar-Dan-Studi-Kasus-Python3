# Belajar Python3 Modul csv

## Cara Mencoba Kode Ini

Pertama, pastikan Python 3.8 sudah terinstall di OS Anda.

Download folder ini.

Selanjutnya, Anda bisa langsung coba:

```
python contoh_modul_csv_read.py
python contoh_modul_csv_write.py
```

## Pendahuluan

Di Python 3, modul csv adalah modul yang berguna untuk melakukan encoding dan decoding csv. 

## Penjelasan

Penjelasannya ada pada komentar di potongan kode berikut ini.

```
# file: contoh_modul_csv_read.py

# begin: import modules
import csv
# end: import modules

# buka file contoh-read.csv
# dengan menggunakan with, tidak perlu fungsi close
# dengan menggunakan with, tidak perlu menerapkan exception handling
with open('contoh-read.csv') as csvf:
    # gunakan csv.reader untuk memparsing csv
    csvreader = csv.reader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris[0] + ", active: " + baris[1] + ", IP: " + baris[2])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))

# buka file contoh-read.csv
with open('contoh-read.csv') as csvf:
    # gunakan csv.DictReader untuk memparsing csv
    # dengan csv.DictReader, baris akan menjadi map
    csvreader = csv.DictReader(csvf, delimiter=',')

    # counter
    ctr = 0

    # print row nya
    for baris in csvreader:
        print("id: " + baris["id"] + ", active: " + baris["active"] + ", IP: " + baris["ip_address"])
        ctr += 1

    # print total barisnya
    print("Total baris:" + str(ctr))
```

```
# file: contoh_modul_csv_write.py

import csv

# cara pertama
# buka contoh-write-0.csv untuk ditulis
with open('contoh-write-0.csv', mode='w') as csvf:
    # gunakan csv.writer
    # quotechar di-set untuk double quote : '"'
    # csv.QUOTE_MINIMAL: hanya quote yang memiliki special character seperti delimiter (misal: koma), quotechar.
    csvw = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # tulis row
    csvw.writerow(['id', 'active', 'ip_address'])
    csvw.writerow(['1', 'True', '127.0.0.1'])

#cara kedua
with open('contoh-write-1.csv', mode='w') as csvf:
    # kali ini nama kolom dibuat terlebih dahulu
    namaKolom = ['id', 'active', 'ip_address']

    # gunakan dictionary writer (map writer)
    # nama kolom digunakan di sini
    csvw = csv.DictWriter(csvf, fieldnames=namaKolom)
    # nama kolom ditulis di sini
    csvw.writeheader()
    # tulis row
    csvw.writerow({'id': '1', 'active' : 'False', 'ip_address' : '192.168.0.1'})
```
