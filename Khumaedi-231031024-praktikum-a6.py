# kode simpel 
# a = True # inisalisasi variabel a berniali True yang akan menjadi kondisi perulangan while


# while a: # perulangan dimulai  
#     pilih = input("Pilihan: ") # inisialisasi variabel pilih yang akan meminta input dari pengguna 
#     if pilih == "ya": # percabangan untuk mengecek apakah input dari user berupa "ya" maka,
#         print("selamat Datang") # cetak "selamat datang"
#     elif pilih == "tidak": # percabangan untuk mengecek apakah input dari user berupa "tidak" maka,
#         print("Sampai Jumpa") # Cetak "sampai jumpa"


## kode tersebut akan terus berjalan karena tidak adanya stop condition di dalam perulangan tersebuut

# Tugas

a = True # inisialisasi variabel a dengan nilai True yang akan menjadi kondisi pada perulangan while 
while a: # perulangan dimulai  
    pilih = input("Pilihan: ") # inisialisasi variabel pilih yang akan meminta input dari pengguna 
    if pilih == "ya": # percabangan untuk mengecek apakah input dari user berupa "ya" maka,
        print("selamat Datang") # cetak "selamat datang"
        break # menghentikan program, break berfungsi sama seperti a = False, yang akan menghentikan perulangan
    elif pilih == "tidak": # percabangan untuk mengecek apakah input dari user berupa "tidak" maka,
        print("Sampai Jumpa") # Cetak "sampai jumpa"
        break# menghentikan program, break berfungsi sama seperti a = False, yang akan menghentikan perulangan
    else: # jika semua kondisi diatas tidak terpenuhi maka, 
        print("masukkan input yang benar! (ya/tidak)") # mencetak pesan tersebut, dan mengulangi perulangan tersebut tanpa henti

