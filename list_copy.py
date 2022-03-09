# teknik mengduplikat list
a = ["Ucup", "Otong", "Dudung"]
print(f"a = {a}")

b = a  # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a k

# ini akan merubah kedua list
b[1] = "Micheal"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"a = {hex(id(a))}")
print(f"b = {hex(id(b))}")

# menduplikasi list dengan copy
print("membuat list c dengan copy")

c = a.copy()  # full duplikat
print(f"a = {hex(id(a))}")
print(f"b = {hex(id(b))}")
print(f"c = {hex(id(c))}")

print("kita ubah data")
c[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
