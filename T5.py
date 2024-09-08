l1 = [2,4,3]
l2 = [5,6,4]
nat1 = ''
nat2 = ''
nat = 0
lst = list()
def func2(teskari1, teskari2):
    global nat1, nat2, nat
    for i in teskari1:
        nat1 += str(i)
    for j in teskari2:
        nat2 += str(j)
    nat = int(nat1)+int(nat2)
    for v in str(nat):
        lst.append(v)
    return lst[::-1]

ds = func2(l1[::-1], l2[::-1])
print(ds)

