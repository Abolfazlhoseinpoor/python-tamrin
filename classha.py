class daneshamooz:
    def __init__(self,name,nomarat):
        self.name = name
        self.nomarat = nomarat
    def miangin(self):
        return sum(self.nomarat) / len(self.nomarat)
    def vaziyat(self):
        if self.miangin() > 10:
            return"ghabol"
        else:
            return"radi"
ali = daneshamooz("ali",[12,15,18])
hasan = daneshamooz("hasan",[12,15,18])
daneshamoozan = [ali,hasan]
for d in daneshamoozan:
    print(d.name,d.miangin(),d.vaziyat())
