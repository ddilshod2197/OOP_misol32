class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Supermarket:
    def __init__(self, nomi):
        self.nomi = nomi
        self.mahsulotlar = []
    
    def mahsulot_qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)
    
    def arzon_mahsulot(self):
        if not self.mahsulotlar:
            print("Mahsulotlar yo‘q")
            return None
        arzon = min(self.mahsulotlar, key=lambda m: m.narx)
        print(f"💰 Eng arzon mahsulot: {arzon.nom} — {arzon.narx} so‘m")
        return arzon

# Test
sup = Supermarket("Korzinka")
sup.mahsulot_qosh(Mahsulot("Non", 5000))
sup.mahsulot_qosh(Mahsulot("Sut", 12000))
sup.mahsulot_qosh(Mahsulot("Tuxum", 18000))
sup.arzon_mahsulot()
