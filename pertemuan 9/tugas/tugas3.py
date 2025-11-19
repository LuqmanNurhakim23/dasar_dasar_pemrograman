def nilai(n = 0):
    if n <= 60:
        print(f"nilai {n} tidak lulus")
    elif n > 60 and n <= 100:
        print(f"nilai {n} lulus")
    else:
        print("abcd")
    
nilai(80)
nilai(60)