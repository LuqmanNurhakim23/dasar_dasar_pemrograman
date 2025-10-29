j = 0
s = ""

b = 1
while b <= 19:
    j += b
    s += str(b)
    if b < 19:
        s += "+"
    b += 2
print(s, "=", j)