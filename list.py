# kumpulan data numbers
data_angka = [1, 2, 3]
print(data_angka)

#kumpulan data strings
data_string =["heri","santoso","uwais"]
print(data_string)

#kumpulan data boolean
data_boolean = [True, False, True]
print(data_boolean)

#kumpulan data campuran
data_campuran = [1,"heri",True,2,"santoso",False,3,"uwais",False]
print(data_campuran)

## cara alternatif membuat list
data_range = range(0,10,2) #range(start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehensi
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

list_pake_for_kuadrat = [i**2 for i in range(0,10)]
print(list_pake_for_kuadrat)

# membuat list pake for pake if 
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if_genap = [i for i in range(0,10) if i%2 ==0]
print(list_pake_for_if_genap)

list_pake_for_if_ganjil = [i for i in range(0,10) if i%2 !=0]
print(list_pake_for_if_ganjil)


