import bangundatar as bd, bangunruang as br

print("=================bangun datar================")
print(f"luas dari persegi dengan sisi 3 {bd.persegi(3)}")
print(f"luas dari persegipanjang {bd.persegipanjang(2,5)}")
print(f"luas dari segitiga {bd.segitiga(6,4)}")
print(f"luas dari lingkarang {bd.lingkaran(14)}")
print(f"luas dari jajargenjang {bd.jajargenjang(13,12)}")

print("=================bangun ruang================")
print(f"volume dari kubus {br.kubus(5)}")
print(f"volume dari balok {br.balok(3, 2, 4)}")
print(f"volume dari prisma {br.prisma(12, 32)}")
print(f"volume dari tabung {br.tabung(13, 15)}")
print(f"volume dari kerucut {br.kerucut(14, 16)}")