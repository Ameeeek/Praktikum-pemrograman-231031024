a = True # inisialisasi variabel a bernilai True yang akan menjadi kondisi pada perulangan while
jalan = 0 # inisialisasi variabel jalan bernilai nol yang akan menghitung berapa banyak program telah berulang
while a: # perulangan dimulai
    if jalan != 5: # percabangan dengan kondisi jika jalan tidak sama dengan 5 maka,
        jalan += 1 # nilai jalan akan ditambah 1 
        print(f"Menjalankan program sebanyak {jalan} kali") # kemudian menjalankan perintah print disamping
    else: # jika kondisi bernilai False atau jika nilai jalan sudah sama dengan 5 maka
        a = False #nilai a akan di inisialisasi ulang dan diganti dengan boolean bernilai False untuk mengehentikan perulangan 


### Kode simpel 


# a = True # inisalisasi variabel a bernilai True yang akan menjadi kondisi pada perulangan

# while a: # perulangan dimulai 
#     print("Menjalankan program") # print menjalankan program terus menerus
# # kode diatas bukan best practice penggunaan perulangan while 
# # karena perulangan while tidak memiliki stop condition, yang akan menghentikan perulangan
# # mengakibatkan perulangan akan terus berjalan tanpa henti. 