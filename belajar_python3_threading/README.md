# Belajar Python3 Modul _thread dan threading

## Cara Mencoba Kode Ini

Untuk mencoba kode ini, pastikan Python 3.8 sudah terinstall.

Selanjutnya jalankan:

```
python contoh_thread.py
python contoh_threading.py
```

## Pendahuluan

Di Python 3, modul _thread dan threading digunakan untuk mengerjakan suatu task secara paralel.

Artinya, dua atau lebih task bisa berjalan bersamaan.

Perbedaan antara _thread dan threading terletak pada penggunaannya.

Penggunaan modul threading bisa dilakukan dengan class yang di-extend dari threading.Thread.

Adapun penggunaan modul _thread lebih prosedural.

## Penjelasan

Penjelasannya ada pada komentar kode.

```
# file: contoh_thread.py

# begin: import modules
import _thread
import time
# end: import modules

# buat class PenampungThread
# walaupun kita tidak sedang menggunakan modul threading.Thread, ini juga bisa
class PenampungThread:

    # class constructor dengan input nama thread
    def __init__(self, nama_thread):
        # assign nama
        self.nama = nama_thread

    # method ini dijalankan dengan thread
    # jeda adalah waktu jedanya
    def run(self, jeda):
        # counter
        ctr = 0

        # sampai selama mungkin
        while 1:
            # terapkan jeda sebesar jeda
            time.sleep(jeda)
            # print nama thread dan counter nya
            print(self.nama, ":", str(ctr))
            # naikkan counter
            ctr+=1

# begin: membuat objek PenampungThread
th1 = PenampungThread("thread-a")
th2 = PenampungThread("thread-b")
# end: membuat objek PenampungThread

try:
      # begin: mulai thread
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
      # end: mulai thread
except:
      # kalau thread tidak bisa dijalankan
      print ("Error: tidak bisa memulai thread")

# mencegah program keluar sebelum thread berjalan
while 1:
      pass
```

```
# file: contoh_threading.py

# begin: import modules
import threading
import time
# end: import modulese

# buat class PenampungThread
# kali ini kita meng-extend nya dari threading.Thread
class PenampungThreading(threading.Thread):
    # class constructor
    # inputnya: nama, jeda, dan berapa kali counter berjalan
    def __init__(self, nama, jeda, berapa_kali):
        # panggil constructor parent class: threading.Thread
        threading.Thread.__init__(self)
        # assign nama
        self.nama = nama
        # assign jeda
        self.jeda = jeda
        # assign berapa kali
        self.berapa_kali = berapa_kali

    # override method dari threading.Thread
    def run(self):
        # memprint "Thread Dimulai: namanya"
        print ("Thread Dimulai: " + self.nama)

        # selama berapa_kali lebih besar dari nol
        while self.berapa_kali:
            # terapkan jeda sebesar jeda
            time.sleep(self.jeda)
            # print nama dan berapa kali yang sedang berjalan
            print(self.nama, ":", str(self.berapa_kali))
            # kurangi berapa_kali dengan 1
            self.berapa_kali -= 1
        # setelah keluar dari while
        print ("Thread Selesai: " + self.nama)

# begin: membuat objek PenampungThread
th1 = PenampungThreading("Thread-1", 2, 5)
th2 = PenampungThreading("Thread-2", 1, 6)
# end: membuat objek PenampungThread

# begin: mulai thread
th1.start()
th2.start()
# end: mulai thread

# join di sini, tujuannya adalah agar main thread
# atau blok utama dari kode menunggu masing-masing thread selesai
th1.join()
th2.join()

# sekarang kedua thread sudah selesai, ayo keluar dari program.
print ("Keluar dari Main Thread....")

# catatan: Anda boleh coba disable kedua join di atas
# dan lihat efeknya
```
