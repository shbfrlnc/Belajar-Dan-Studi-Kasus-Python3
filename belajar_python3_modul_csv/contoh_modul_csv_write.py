import csv

#cara pertama
with open('contoh-write-0.csv', mode='w') as csvf:
    csvw = csv.writer(csvf, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvw.writerow(['id', 'active', 'ip_address'])
    csvw.writerow(['1', 'True', '127.0.0.1'])

#cara kedua
with open('contoh-write-1.csv', mode='w') as csvf:
    namaKolom = ['id', 'active', 'ip_address']
    csvw = csv.DictWriter(csvf, fieldnames=namaKolom)
    csvw.writeheader()
    csvw.writerow({'id': '1', 'active' : 'False', 'ip_address' : '192.168.0.1'})