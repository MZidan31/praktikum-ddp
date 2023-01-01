from animal import*

class badak(animal):
    umur = 0
    jenisKelamin = " "

    def __init__(self, nama, makanan, hidup, berkembangBiak, umur, jenisKelamin):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.umur = umur
        self.jenisKelamin = jenisKelamin

    def cetak(self):
        super().cetak()
        print("Umur \t :", self.umur, "\n Jenis Kelamin \t :", self.jenisKelamin, 
        "\n-----------------------------")