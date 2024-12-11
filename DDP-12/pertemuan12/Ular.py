from Animal import *

class Ular(Animal): 
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    
    def cetak_ular(self):
        print("--------------------------------------")
        super().cetak()
        print("design \t\t: ", self.design,
              "\nracun \t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Beracun")
anaconda.cetak_ular()

python = Ular("Python", "Tikus", "Amazon", "Bertelur", "Hitam Batik", "Beracun")
python.cetak_ular()