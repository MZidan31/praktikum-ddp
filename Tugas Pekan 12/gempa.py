class Gempa:
    lokasi = ""
    skala = 0

    def _init_(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if (self.skala < 2):
             ket = "gempa tidak berasa"
        elif (self.skala >= 2 and self.skala < 4):
            ket = "Bangunan retak retak"
        elif (self.skala >= 4 and self.skala < 6):
            ket = "Bangunan roboh"
        else:
            ket = "Bangunan roboh dan berpotensi tsunami"

        print("\nLokasi gempa\t:",self.lokasi,"\nSkala\t\t:",self.skala,"richter""\nDampak\t\t:",ket,"\n----------------------------------")