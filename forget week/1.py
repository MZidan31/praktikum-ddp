#Muhammad Zidan

#Modul / function nya
import math

def luas_kubus(panjang):
    return 6 * panjang**2

def luas_prisma_segitiga(alas, tinggi, panjang):
    return 2 *alas + tinggi * 3 * alas * panjang

def luas_tabung(jari, tinggi):
    return 2 * math.pi * jari * tinggi *2 * math.pi * jari**2

def luas_bola(jari):
    return 4 * math.pi * jari**2

def luas_kerucut(jari, tinggi):
    return math.pi * jari * (jari * math.sqrt(tinggi**2 + jari**2))

#input properti bangun ruang + output
print("------------------------------------------------------")
a = int(input("sisi kubus = "))
print("luas permukaan kerucut = " ,luas_kubus(a))

print("-----------------------------------------------------")

a = int(input("alas prisma segitiga = "))
b = int(input("tinggi prisma segitiga = "))
c = int(input("panjang prisma segitiga = "))
print("luas permukaan prisma segitiga = " , luas_prisma_segitiga(a, b, c))

print("-------------------------------------------------")

a = int(input("jari jari alas tabung adalah = "))
b = int(input("tinggi tabung adalah = "))
print("luas permukaan tabung = " , luas_tabung(a, b))

print("-------------------------------------------------")

a = int(input("jari-jari bola adalah = "))
print("luas permukaan bola = " , luas_bola(a))

print("-------------------------------------------------")


a = int(input("jari jari alas kerucut adalah = "))
b = int(input("tinggi kerucut adalah = "))
print("luas permukaan kerucut = " , luas_kerucut(a, b))

print("--------------------------------------------------")