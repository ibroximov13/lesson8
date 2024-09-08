fayl = open("sinov2.txt", "r")
malumot = fayl.read()
fayl.close()

fayl2 = open("kochirma.txt", "w")
fayl2.write(malumot)
fayl2.close()
