from Animal import *

class Burung(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.bunyi = bunyi
    
    def cetak_burung(self):
        print("--------------------------------------")
        super().cetak()
        print("warna \t\t: ", self.warna,
              "\nbunyi \t\t: ", self.bunyi)
        
gereja = Burung("Gereja", "beras", "udara", "Bertelur", "hitam", "cutcutcut")
gereja.cetak_burung()

beo = Burung("beo", "kacang", "udara", "Bertelur", "hitam", "weoweo")
beo.cetak_burung()