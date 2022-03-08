# Operasi

# index   0        1       2
data = ["ucup", "Otong", "Dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil jumlah data pada list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list
# menambahkan item pada list sesuai dengan posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1, "asep")  # posisi index
print(f"data sesudah ditambah= \n {data}")

data.append("jajang")
print(f"data sesudah ditambah = \n {data}")

# menambahkan list dengan list
data_baru = ["ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n {data}")

# merubah data
data[2] = "Micheel"
print(f"data rubah = \n {data}")

# meremove data
data.remove("ujang")
print(f"data remove = \n {data}")
# data.remove("Ujang")  # akan error data tidak di temukan

# meremove data paling belakang
data.pop()
print(f"data akhir = \n {data}")
