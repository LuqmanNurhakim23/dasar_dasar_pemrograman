menumakanan = [("nasi goreng", 15000),
               ("mie goreng", 12000),
               ("ayam geprek", 18000)]
menuminuman = [("aneka jus", 15000),
               ("soft drink", 10000),
               ("sweet ice tea", 5000)]

nama = input("nama pembeli :")
telp = int(input("no telp pembeli :"))
menu = input("menu apa :")
if menu == "makanan" :
    print(menumakanan)
elif menu == "minuman" :
    print(menuminuman)
else :
    print("tipe menu salah")