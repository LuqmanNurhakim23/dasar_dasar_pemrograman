a = int(input("pilih angka: "))

match a:
    case 1 :
        input = int(input("masukan saldo: "))
        print("saldo anda: ", input)
    case 2 :
        print("tampilkan saldo")
    case 3 :
        print("tarik tunai")
    case _ :
        print("salah input")
