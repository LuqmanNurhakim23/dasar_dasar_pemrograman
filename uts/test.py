a = int(input("angka 1 : "))
b = int(input("angka 2 : "))
c = input("masukan operator: ")

if c == "+" :
    print("angka 1: ", a)
    print("angka 2: ", b)
    print(a,c,b, "=",a+b)
elif c == "-" :
    print("angka 1: ", a)
    print("angka 2: ", b)
    print(a,c,b, "=",a-b)
elif c == "*" :
    print("angka 1: ", a)
    print("angka 2: ", b)
    print(a,c,b, "=",a*b)
elif c == "/" :
    print("angka 1: ", a)
    print("angka 2: ", b)
    print(a,c,b, "=",a/b)
elif c == "**" :
    print("angka 1: ", a)
    print("angka 2: ", b)
    print(a,c,b, "=",a**b)
else :
    print("operator salah")
