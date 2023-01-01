#tambah
def tambah(*angka):
    total - 0
    for num in angka:
        total += num
    print(total)

#kurang
def kurang(*angka):
    total = angka[0]
    for num in angka[1:]:
        total -= num
    print(total)

#kali
def kali(*angka):
    total - angka[0]
    for num in angka[1:]:
        total *= num
    print(total)

tambah(4,2,4,5)
kurang(2,10,2)
kali(6,5,2,1)