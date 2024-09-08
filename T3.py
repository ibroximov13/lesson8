fayl = open("sinov1.txt", "r")
malumot = fayl.read().split()
fayl.close()
print(malumot)
maxSoz = ""
for i in malumot:
    if len(i) > len(maxSoz):
        maxSoz = i
print(f"sinov1.txt faylidagi eng uzun so'z: {maxSoz}, uning uzunligi: {len(maxSoz)} ga teng")
