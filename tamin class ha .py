class mahsul:
    def __init__(self,price,name):
        self.name = name
        self.price = price
    def ghaeymat_ba_takhfif(self,precent):
        return self.price - (self.price * precent / 100)
pirahan = mahsul(150000,"pirahan")
natije = pirahan.ghaeymat_ba_takhfif(10)
print(pirahan.name)
print(pirahan.price)
print(natije)