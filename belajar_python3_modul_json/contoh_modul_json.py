import json

print("json ke python")

data_json = '{"nama" : "toko buku", "produk":"buku", "jumlahProduk" : "3"}'
data_di_python = json.loads(data_json)

print(data_di_python)
print(data_di_python["nama"])
print(data_di_python["jumlahProduk"])

print("python ke json")

data_python = {
  "nama": "suatu_aplikasi",
  "kode_versi": 40,
  "portable": True,
  "requirement": ("opencv","numpy")
}

data_di_json = json.dumps(data_python)
print(data_di_json)