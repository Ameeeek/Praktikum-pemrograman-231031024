pw_benar = "si23a"
percobaan = 3
a = True
while a:
    masukan = input("masukkan password: ")
    if masukan == pw_benar:
        print("selamat anda login!")
        a = False
    else: 
        if percobaan == 0: 
            print("password yang anda masukkan salah! dan anda sudah kehabisan percobaan.\nAnda dibanned!")
            a = False
        else:
            print("password yang anda masukkan salah! coba lagi", percobaan)
            percobaan -= 1

            