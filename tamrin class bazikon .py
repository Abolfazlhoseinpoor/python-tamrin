class bazikon:
    def __init__(self,name,gol):
        self.name = name
        self.gol = gol
golha = []
bazikon1 = bazikon("ali",3)
bazikon2 = bazikon("mohsen",6)
bazikon3 = bazikon("jafar",1)

golha = [bazikon1,bazikon2,bazikon3]
for i,player in enumerate(golha,start=1):
    print(f"esm bazikon: {player.name} va tedad gol zade shode tavasot in bazikon: {player.gol}")
bishtarin = golha[0]
for i in golha:
    if i.gol > bishtarin.gol:
        bishtarin = i
print(f"bishatin gol zade shode tavasot bazikon : {bishtarin.name} tedad gol zade shode: {bishtarin.gol}")