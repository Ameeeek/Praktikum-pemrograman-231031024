jumlahPendapatan = int(input("masukkan besaran pendapatan: "))
persentase = 0

if jumlahPendapatan > 0 and jumlahPendapatan <= 1000: 
    print("Maaf anda tidak mendapatkan bonus")
elif jumlahPendapatan >= 1001 and jumlahPendapatan <= 2000:
    persentase = 10
elif jumlahPendapatan >= 2001 and jumlahPendapatan <= 3000:
    persentase = 20
elif jumlahPendapatan >= 3001 and jumlahPendapatan <= 4000:
    persentase = 30
elif jumlahPendapatan >= 4001 and jumlahPendapatan <= 5000:
    persentase = 40
else:   
    persentase = 50

bonus = jumlahPendapatan * (persentase/100)

totalPendapatan = jumlahPendapatan + bonus

print(f'\nBesar pendapatan yang didapatkan: {int(jumlahPendapatan)}')
print(f"Besar persentase bonus yang diperoleh: {persentase:,.01f}%")
print(f'Besaran bonus yang diperolah: {int(bonus)}')
print(f'Jumlah total pendapatan: {int(totalPendapatan)}')