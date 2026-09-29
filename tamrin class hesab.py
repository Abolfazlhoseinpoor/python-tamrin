import random as r
class hesab:
    def __init__(self,saheb,shomare,mojodi):
        self.mojodi = mojodi
        self.saheb = saheb
        self.shomare = shomare
    def variz(self,meghdar):
        self.mojodi += meghdar
    def bardashty(self,bardasht):
        self.mojodi -= bardasht
hesabha = []
while True:
    print("+"*30)
    print("gozine 1 == injad hesab jadid \ngozine 2 == namayesh hesab ha ba mojodi \ngzoine 3 == varizi \ngozine 4 == bardasht \ngozine 5 == exit")
    print("+"*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        cart = input("lotfan esm saheb cart ro vared konid: ")
        if cart == "":
            print("shoma esm saheb cart ro vared nakarddi!")
            continue
        if not cart.isalpha():
            print("lotfan esm saheb cart ro be horof vared konid!")
            continue
        addad = "0123456789"
        number_list = "".join(r.choices(addad,k=16)) 
        number =" ".join(number_list[i:i+4] for i in range(0,16,4))
        mojodi = input(f"lotfan meghdar pooli ke mikhahid rikhte shavd dar hesab: {cart} ro vared konid:")
        if mojodi == "":
            print("shoma meghdar mojodi ro vared nakardid!")
            continue
        try:
            meghdar_mojodi = int(mojodi)
        except ValueError:
            print("lotfan meghdar mojodi ro be addad vared konid!")
            continue
        bank = hesab(cart,number,meghdar_mojodi)
        hesabha.append(bank)
        print("hesab sakhte shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        if not hesabha:
            print("hesabi dar bank vojod nadarad!")
            continue
        for i,bank in enumerate(hesabha,start=1):
            print(f"{i} ==> esm saheb cart: {bank.saheb} shomare cart: {bank.shomare} va mojodi in cart: {bank.mojodi:,} ")
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        if not hesabha:
            print("hesabi dar bank vojod nadarad!")
            continue
        for i,bank in enumerate(hesabha,start=1):
            print(f"{i} ==> {bank.saheb}")
        idx = input("shomare hesab ro vared konid: ")
        if idx == "":
            print("shoma shomare hesab ro vared nakardid!")
            continue
        try:
            index = int(idx)
        except ValueError:
            print("lotfan shomare hesab ro be addad vared konid!")
            continue
        meghdar_variz = input("lotfan meghdar varizi ro vared konid:")
        if meghdar_variz == "":
            print("shoma meghdar varizi ro vared nakardid!")
            continue
        try:
            varizi = int(meghdar_variz)
        except ValueError:
            print("shoma bayad meghdar varizi ro be addad vared konid!")
            continue
        hesabha[index-1].variz(varizi)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        if not hesabha:
            print("hesabi dar bank vojod nadarad!")
            continue
        for i,bank in enumerate(hesabha,start=1):
            print(f"{i} ==> {bank.saheb}")
        idx = input("shomare hesab ro vared konid: ")
        if idx == "":
            print("shoma shomare hesab ro vared nakardid!")
            continue
        try:
            index = int(idx)
        except ValueError:
            print("lotfan shomare hesab ro be addad vared konid!")
            continue
        meghdar_bardasht = input("lotfan meghdar bardashty ro vared konid:")
        if meghdar_bardasht == "":
            print("shoma meghdar bardashty ro vared nakardid!")
            continue
        try:
            bardashty = int(meghdar_bardasht)
        except ValueError:
            print("meghdar bardashty ro be addad vared konid!")
            continue
        hesabha[index-1].bardashty(bardashty)
    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid va az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 5 entekhab konid!")
        continue

     

