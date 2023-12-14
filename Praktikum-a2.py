print("Praktikum-2\n")

print("Nama     : Khumaedi")
print("Nim      : 23013104")
print("Prodi    : Sistem Informasi 23 A\n")

# Ini operator Assignment

a = 19
print(f"nilai a adalah {a}")
a += 3
print(f"nilai a+=3 adalah {a}\n")
a = 19
print(f"nilai a adalah {a}")
a -= 3
print(f"nilai a-=3 adalah {a}\n")
a = 19
print(f"nilai a adalah {a}")
a *= 2
print(f"nilai a*=2 adalah {a}\n")
a = 19
print(f"nilai a adalah {a}")
a /= 2
print(f"nilai a/=2 adalah {a}\n")
a = 3
print(f"nilai a adalah {a}")
a **= 2
print(f"nilai a**=2 adalah {a}\n")
a = 35
print(f"nilai a adalah {a}")
a %= 32
print(f"nilai a%=32 adalah {a}\n")
a = 35
print(f"nilai a adalah {a}")
a //= 32
print(f"nilai a//=32 adalah {a}\n")

# Tugas melanjutkan untuk operator selanjutnya
# line 25-59

# OR
b = True
print("Nilai b =", b)
b |= False
print(f"Nilai b |= false akan menjadi {b}\n")
b = False
print(f"Nilai b = {b}")
b |= False
print(f"Nilai b |= false akan menjadi {b}\n")
# AND
b = True
print(f"nilai b = {b}")
b &= False
print(f"nilai b&=False akan menjadi {b}\n")
# Xor
b = True
print(f"Nilai b = {b}")
b ^= False
print(f"Nilai b^=False akan menjadi {b}\n")
b = False
print(f"Nilai b = {b}")
b ^= False
print(f"Nilai b^=False akan menjadi {b}\n")
# Shifting
c = 0b0100
print(f'nilai c = {format(c,"04b")}')
c >>= 1
print(f'Nilai c>>=1 akan menjadi {format(c,"04b")}\n')
c = 0b0100
print(f'nilai c = {format(c,"04b")}')
c <<= 1
print(f'Nilai c <<=1 akan menjadi {format(c,"04b")}\n')
# Operator perbandingan
a = 9
b = 13
print("\n---------- Besar dari 24")
hasil = a > 24
print(f"{a} > 24 adalah {hasil}")
hasil = b > 24
print(f"{b} > 24 adalah {hasil}")

print("\n---------- Kecil dari 24")
hasil = a < 24
print(f"{a} < 24 adalah {hasil}")
hasil = b < 24

print(f"{b} < 24 adalah {hasil}")

print("\n---------- Sama dengan 24")
hasil = a == 24
print(f"{a} == 24 adalah {hasil}")
hasil = b == 24
print(f"{b} == 24 adalah {hasil}")

print("\n---------- Tidak Sama dengan 24")
hasil = a != 24
print(f"{a} != 24 adalah {hasil}")
hasil = b != 24
print(f"{b} != 24 adalah {hasil}")

print("\n---------- Besar atau sama dari 24")
hasil = a >= 24
print(f"{a} >= 24 adalah {hasil}")
hasil = b >= 24
print(f"{b} >= 24 adalah {hasil}")

print("\n---------- Kecil atau sama dari 24")
hasil = a <= 24
print(f"{a} <= 24 adalah {hasil}")
hasil = b <= 24
print(f"{b} <= 24 adalah {hasil}")


# Operator Logika
a = True
b = False
print("\n=========AND========\n")
hasil = a and a
print(f"{a} and {a} hasilnya sama dengan {hasil}")
hasil = a and b
print(f"{a} and {b} hasilnya sama dengan {hasil}")
hasil = b and a
print(f"{b} and {a} hasilnya sama dengan {hasil}")
hasil = b and b
print(f"{b} and {b} hasilnya sama dengan {hasil}")

print("\n=========OR========\n")
hasil = a or a
print(f"{a} or {a} hasilnya sama dengan {hasil}")
hasil = a or b
print(f"{a} or {b} hasilnya sama dengan {hasil}")
hasil = b or a
print(f"{b} or {a} hasilnya sama dengan {hasil}")
hasil = b or b
print(f"{b} or {b} hasilnya sama dengan {hasil}")

#Tugas Tulis Operator Logika XOR
print("\n=========XOR========\n")
hasil = a ^ a
print(f"{a} xor {a} hasilnya sama dengan {hasil}")
hasil = a ^ b
print(f"{a} xor {b} hasilnya sama dengan {hasil}")
hasil = b ^ a
print(f"{b} xor {a} hasilnya sama dengan {hasil}")
hasil = b ^ b
print(f"{b} xor {b} hasilnya sama dengan {hasil}")

print('\n=========NOT=========\n')
hasil = not a 
print(f'not {a} hasilya = {hasil}\n')
hasil = not b 
print(f'not {b} hasilya = {hasil}')

# Operator Membership 
print("\n=======================IN==================")
nama = "Khumaedi"
test = "Kh"
cek = test in nama 
print(f'{test} terdapat di {nama} = {cek}')
nama = "Khumaedi"
test = "hk"
cek = test in nama 
print(f'{test} terdapat di {nama} = {cek}\n')

test1 = 'a'
test2 = 'e'
test3 = 'i'
test4 = 'u'
test5 = 'o'
cek = test1 in nama 
print(f'{test1} terdapat di nama {nama} adalah {cek}')
cek = test2 in nama 
print(f'{test2} terdapat di nama {nama} adalah {cek}')
cek = test3 in nama 
print(f'{test3} terdapat di nama {nama} adalah {cek}')
cek = test4 in nama 
print(f'{test4} terdapat di nama {nama} adalah {cek}')
cek = test5 in nama 
print(f'{test5} terdapat di nama {nama} adalah {cek}')

# Tugas lanjut not in 
print("\n=======================NOT IN==================")
nama = "Khumaedi"
test = "Kh"
cek = test not in nama 
print(f'{test} tidak terdapat di {nama} = {cek}')
nama = "Khumaedi"
test = "hk"
cek = test not in nama 
print(f'{test} tidak terdapat di {nama} = {cek}\n')

test1 = 'a'
test2 = 'e'
test3 = 'i'
test4 = 'u'
test5 = 'o'
cek = test1 not in nama 
print(f'{test1} tidak terdapat di nama {nama} adalah {cek}')
cek = test2 not in nama 
print(f'{test2} tidak terdapat di nama {nama} adalah {cek}')
cek = test3 not in nama 
print(f'{test3} tidak terdapat di nama {nama} adalah {cek}')
cek = test4 not in nama 
print(f'{test4} tidak terdapat di nama {nama} adalah {cek}')
cek = test5 not in nama 
print(f'{test5} tidak terdapat di nama {nama} adalah {cek}')