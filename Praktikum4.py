class rectangle:
    def __init__(self, panjang, lebar):
        if panjang == 0 or lebar ==  0:
            print("panjang dan lebar tidak boleh 0")
        else:
            self.panjang = panjang 
            self.lebar = lebar 

def keliling(self):
    hasil = 2 * (self.panjang + self.lebar)
    return hasil

    