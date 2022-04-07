import threading
import time

class PenampungThreading(threading.Thread):
    def __init__(self, nama, jeda, berapa_kali):
        threading.Thread.__init__(self)
        self.nama = nama
        self.jeda = jeda
        self.berapa_kali = berapa_kali

    def run(self):
        print ("Thread Dimulai: " + self.nama)
        while self.berapa_kali:
            time.sleep(self.jeda)
            print(self.nama, ":", str(self.berapa_kali))
            self.berapa_kali -= 1
        print ("Thread Selesai: " + self.nama)

th1 = PenampungThreading("Thread-1", 2, 5)
th2 = PenampungThreading("Thread-2", 1, 6)

th1.start()
th2.start()

th1.join()
th2.join()

print ("Keluar dari Main Thread....")