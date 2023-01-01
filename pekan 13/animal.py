class animal:
    nama = " "
    makanan = " "
    hidup = " "
    berkembangBiak = " "

    def __init__(self, nama, makanan, hidup, berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print("Nama \t :", self.nama, "\n Makanan \t :", self.makanan, "\n Hidup \t :", self.hidup, 
        "\n Berkembang biak \t :", self.berkembangBiak)