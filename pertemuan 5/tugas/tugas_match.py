hitung = int(input("""""
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas persegi
masukan angkanya: 
"""""))
match hitung:
    case 1:
        a = int(input("masukan sisi: "))
        luas = a * a
        print("hasilnya: ", luas)
    case 2:
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3.14 * (r ** 2)
        print("Luas lingkaran adalah:", round(luas, 2))
    case 3:
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * alas * tinggi
        print("Luas segitiga adalah:", luas)
    case _:
        print("apa coba")
