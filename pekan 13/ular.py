from animal import*

class ular(animal):
    jenisUlar = ""
    umur = 0

    def __init__(self, nama, makanan, hidup, berkembangBiak, jenisUlar, umur):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenisUlar = jenisUlar
        self.umur = umur

    def cetak(self):
        super().cetak()
        print("Jenis Ular \t :", self.jenisUlar, 
                "\n Umur \t :", self.umur,
                "\n ------------------------------")