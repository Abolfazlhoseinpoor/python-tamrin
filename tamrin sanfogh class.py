class sandogh:
    def __init__(self,sandogh_name,pool):
        self.sandogh_name = sandogh_name
        self.pool = pool
    def fourosh(self,meghdar):
        self.pool += meghdar
    def khali_kon(self,meghdar):
        if self.pool < meghdar:
            return "pool kafi dar sandogh nadarim!"
        else: 
             self.pool -= meghdar
khazane = []
while True:
    print("="*30)
    print("gozine 1 == vared kardan sandogh jadid be meghdar pool sandogh \ngozine 2 == meghdar pool dar sandogh \ngozine 3 == forosh \ngozine 4 == khali kon \ngozine 5 == exit!")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro entekhab konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        name_sandogh = input("lotfan esm sandogh ro vared konid: ")
        if name_sandogh == "":
            print("shoma esm sandogh ro vared nakardid!")
            continue
        meghdar_pool = input(f"lotfan meghdar pool dar sandogh {name_sandogh} ro vared konid:  ")
        if meghdar_pool == "":
            print("shoma meghdar pool ro vared nakardid!")
            continue
        try:
            pool = int(meghdar_pool)
        except ValueError:
            print("lotfan meghdar pool sandogh ro be addad vared konid!")
            continue
        etelat = sandogh(name_sandogh,pool)
        khazane.append(etelat)
        print("esm sandogh ve meghdar poolash sabt shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        if not khazane:
            print("sandoghy vojod nadarad!")
            continue
        for i,etelat in enumerate(khazane,start=1):
            print(f"{i} === esm sandogh: {etelat.sandogh_name} meghdar pool: {etelat.pool:,} ")
    elif choice == "3":
        print("shoma gozien 3 ro entekhab kardid!")
        if not khazane:
            print("sandoghy vojod nadarad!")
            continue
        for i,etelat in enumerate(khazane,start=1):
            print(f"{i} === {etelat.sandogh_name}")
        idx = input("lotfan shomare sandogh ro vared konid:")
        if idx == "":
            print("shoma shomare sandogh ro moshakhas nakardid!")
            continue
        try:
            index = int(idx)
        except ValueError:
            print("lotfan shomare sandogh ro be addad vared konid!")
            continue
        sell = input("lotfan meghdar foroush ro vared konid:")
        if sell == "":
            print("shoma meghdar forosh ro vared nakardid!")
            continue
        try:
            isell = int(sell)
        except ValueError:
            print("lotfan meghdar forosh ro be addad vared konid!")
            continue
        khazane[index-1].fourosh(isell)  
        print("forosh movafaghiyat amiz bood")
    elif choice =="4":
        print("shoma gozine 4 ro entekhab kardid!")
        if not khazane:
            print("sandoghy vojod nadarad!")
            continue
        for i,etelat in enumerate(khazane,start=1):
            print(f"{i} === {etelat.sandogh_name}")
        idx = input("lotfan shomare sandogh ro vared konid:")
        if idx == "":
            print("shoma shomare sandogh ro moshakhas nakardid!")
            continue
        try:
            index = int(idx)
        except ValueError:
            print("lotfan shomare sandogh ro be addad vared konid!")
            continue
        buy = input("lotfan meghdar foroush ro vared konid:")
        if buy == "":
            print("shoma meghdar forosh ro vared nakardid!")
            continue
        try:
            ibuy = int(buy)
        except ValueError:
            print("lotfan meghdar forosh ro be addad vared konid!")
            continue
        natije = khazane[index-1].khali_kon(ibuy)
        if natije:
            print(natije)
            continue
        else:
            print("kharid movafaghiyat amiz bood!")
    elif choice =="5":
        print("shoma gozine 5 ro entekhab kardid! \naz barnam ekharej shodid bye bye!!")
        break
    else:
        print("lotfan az gozine 1 ta 5 entekhab konid!")
        continue
