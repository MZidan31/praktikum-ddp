hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40},
]

siswa_lulus = []
for siswa in hasil_akhir:
    if siswa['nilai'] > 65:
        siswa_lulus.append(siswa['nama'])
print(siswa_lulus)
