fayl = open("sinov1.txt","r")
malumot = fayl.read().split("\n")
fayl.close()
print(malumot)


for i in range(len(malumot)):
    i += 1
print(i)

