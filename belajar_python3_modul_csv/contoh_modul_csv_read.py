import csv

with open('contoh-read.csv') as csvf:
    csvreader = csv.reader(csvf, delimiter=',')
    ctr = 0
    for baris in csvreader:
        print("id: " + baris[0] + ", active: " + baris[1] + ", IP: " + baris[2])
        ctr += 1
    print("Total baris:" + str(ctr))

with open('contoh-read.csv') as csvf:
    csvreader = csv.DictReader(csvf, delimiter=',')
    ctr = 0
    for baris in csvreader:
        print("id: " + baris["id"] + ", active: " + baris["active"] + ", IP: " + baris["ip_address"])
        ctr += 1
    print("Total baris:" + str(ctr))