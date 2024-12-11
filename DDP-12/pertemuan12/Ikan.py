from Animal import *

class Ikan(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna
    
    def cetak_ikan(self):
        print("--------------------------------------")
        super().cetak()
        print("jenis \t\t: ", self.jenis,
              "\nbunyi \t\t: ", self.warna)
        
koi = Ikan("Koi", "pelet", "air", "Bertelur", "air tawar", "Merah")
koi.cetak_ikan()

emas = Ikan("emas", "pelet", "air", "Bertelur", "air tawar", "emas")
emas.cetak_ikan()