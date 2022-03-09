data_angka = [1, 5, 1, 2, 2, 2, 2, 3, 3, 3, 5, 5, 5, 1, 1, 1, 1]

print(f"data angka = \n {data_angka}")


# count data
jumlah_data_2 = data_angka.count(2)
jumlah_data_5 = data_angka.count(5)

print(f"jumlah angka 2 = {jumlah_data_2}")
print(f"jumlah angka 5 = {jumlah_data_5}")


# ambil posisi data (index)
data = ["Ucup", "Otong", "Dudung", "Ujang"]

index_dudung = data.index("Dudung")
index_Ujang = data.index("Ujang")

print(f"index si dudung = {index_dudung}")
print(f"index si Ujang = {index_Ujang}")

# mengurutkan list
print(f"data angka sebelum sort =\n {data_angka}")
data_angka.sort()
print(f"data angka sort =\n {data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n {data_angka} \n {data}")
