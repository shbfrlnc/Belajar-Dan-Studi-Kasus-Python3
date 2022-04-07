import _thread
import time

class PenampungThread:
    def __init__(self, nama_thread):
        self.nama = nama_thread

    def run(self, jeda):
        ctr = 0
        while 1:
            time.sleep(jeda)
            print(self.nama, ":", str(ctr))
            ctr+=1

th1 = PenampungThread("thread-a")
th2 = PenampungThread("thread-b")

try:
      _thread.start_new_thread(th1.run, (2,))
      _thread.start_new_thread(th2.run, (4,))
except:
      print ("Error: tidak bisa memulai thread")

while 1:
      pass