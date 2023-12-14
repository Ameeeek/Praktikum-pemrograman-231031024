namaKaryawan = input("Masukkan nama karyawan: ")
jumlahPendapatan = int(input("masukkan jumlah pendapatan karyawan tersebut: "))
status = "berhak"

if jumlahPendapatan > 1000:
    print(
f"""
Nama karyawan: {namaKaryawan}
Pendapatan: {jumlahPendapatan}
Status: {status}
        """
    )
else:
    status = "tidak berhak"
    print(
f"""
Nama karyawan: {namaKaryawan}
Pendapatan: {jumlahPendapatan}
Status: {status}
"""
    )