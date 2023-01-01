from animal import*

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, jenisIkan, umur):
        super().__init__(nama, makanan, hidup, berkembangBiak)
        self.jenisIkan = jenisIkan
        self.umur = umur

    def cetak(self):
        super().cetak()
        print("Jenis Ikan \t :", self.jenisIkan, 
                "\n Umur \t :", self.umur,
                "\n ------------------------------")