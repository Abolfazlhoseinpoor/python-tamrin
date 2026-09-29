class mahsul:
    def __init__(self,name,price,quantity,sold = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sold = sold
    def gheymat_ba_takhfif(self,precent):
        return self.price - (self.price * precent /100)
    def forush(self,tedad):
        if tedad > self.quantity:
            return "mojodi kafi nis!"
        else:
            self.quantity -= tedad
            self.sold +=  tedad
            return f"{tedad} forkhte shod!"
    def dar_anbar(self):
        return self.quantity > 0
    def gozaresh(self):
        print(f"name jens: {self.name} gheymat jense: {self.price} tedad: {self.quantity} jens frokhte shode: {self.sold}")
mahsulat = []
while True:
    print("="*30)
    print("gozine 1 == injad mahsul jadid \ngoizne 2 == foroush \ngozine 3 == namyayesh mojodi anbar \ngozine 4 == gozaresh hame mahsulat \ngzoine 5 == ghaymat ba takhfif \ngozine 6 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab karidd!")
        name = input("lotfan esm mahsul ro vared konid: ")
        if name == "":
            print("shoma esm mahsul ro vared nakardid!")
            continue
        price = input(f"lotfan gheymat : {name} ro vared konid: ")
        if price == "":
            print(f"shoma gheymat kala : {name} ro vared nakardid! ")
            continue
        try:
            gheyamt = float(price)
        except ValueError: 
            print(f"lotfan gheymat kala : {name} ro be addad vared konid: shoma ino vared kardid ==> {price}")
            continue
        tedad = input(f"lotfan mojodi kala : {name} ro vared konid: ")
        if tedad == "":
            print("tedad kala ro vared nakardid!")
            continue
        try:
            tedad_kala = int(tedad)
        except ValueError:
            print("lotfan tedad kala ro be addad vared konid ")
            continue
        p = mahsul(name,gheyamt,tedad_kala)
        mahsulat.append(p)
        print(f"{name} be anbar ezafe shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        if not mahsulat:
            print("anbar khali ast!")
            continue
        for i,p in enumerate(mahsulat,start=1):
            print(f"{i} === {p.name} mojodi === {p.quantity}")
        try:
            index = int(input("lotfan shomare mahsul ro vared konid :"))
            if index == "":
                print("shoma shomare mahsul ro vared nakardid!")
                continue
            tedad_froush = int(input(f"lotfan tedad kala {p.name} ke mikhahid befroshid ro vared konid: "))
            if tedad_froush == "":
                print("shoma tedad kala ro vared nakardid!")
                continue
            result = mahsulat[index].forush(tedad_froush)
            print(result)
        except ValueError as e:
            print(f"shoma {e} ro bayad be addad vared konid!")
            continue
        except IndexError:
            print(f"shomare mahsul eshtebah!")
            continue
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        if not mahsulat:
            print("anbar khali ast!")
            continue
        for p in mahsulat:
            vaziyat = "mojod" if p.dar_anbar() else "sefr"
            print(f"{p.name} : {vaziyat} {p.quantity} ta")
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        if not mahsulat:
            print("anbar khali ast!")
            continue
        for p in mahsulat:
            p.gozaresh()
    elif choice == "5":
        print("shoma gzoine 5 ro entekhab kardid!")
        if not mahsulat:
            print("anbar khali ast!")
            continue
        for i,p in enumerate(mahsulat,start=1):
            print(f"{i} : {p.name} gheymat : {p.price}")
        try:
            idx = int(input("lotfan shomare kala ro vared konid: "))
            idx += 1
            if idx == "":
                print("shoma shomare mahsul ro vared nakardid!")
                continue
            precent = float(input("darsad takhfif ke mikhahid bedid ro vared konid: "))
            if precent == "":
                print("shoma darsad takhfif ro vared nakardid!")
                continue
            new_price = mahsulat[idx].gheymat_ba_takhfif(precent)
            print(f"gheyamt ba : %{precent} darsad takhfif mishe : {new_price}")
        except ValueError as e:
            print(f"lotfan {e} ro be addad vared konid! ")
            continue
        except IndexError:
            print("shomare mahsul eshteba ast!")
            continue
    elif choice == "6":
        print("bye bye")
        break
    else:
        print("lotfan az gozine 1 ta 6 entekhab konid!")
        continue
        