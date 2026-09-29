class ketab:
    def __init__(self,ketab,nevisande,page):
        self.ketab = ketab
        self.nevisande = nevisande
        self.page = page
    def is_long(self):
        if self.page < 300:
            return "tedad safe ha kam tar az 300 ta"
        else:
            return "tedad safe ha bishtar az 300 ta"
majmoe = []
while True:
    print("="*30)
    print("gozine 1 == ezafe kardan nevsiande ba ketbash \ngozine 2 == namayesh esm nevisandegan \ngozine 3 == namayesh ketab ha \ngozine 4 == namayesh nevisande ba ketabash \ngozien 5 == vaziyat safe ketab \ngozine 6 == exit ")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro entekhab konid: ")
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        nevisande = input("lotfan esm nevisande ro vared konid: ")
        if nevisande == "":
            print("shoma esm nevisande ro vared nakardid!")
            continue
        if not nevisande.isalpha():
            print(f"lotfan esm nevisande ro be horof vared konid shoma ino vared kardid!: {nevisande}")
            continue
        ketabash = input(f"lotfan esm ketabi ro ke {nevisande} neveshte ro vared konid: ")
        if ketabash == "":
            print(f"shoma esm ketabi ro ke {nevisande} neveshte ro vared nakardid!")
            continue
        if not ketabash.isalpha():
            print("lotfan esm ketab ro be horof vared konid ")
            continue
        safe = input(f"lotfan tedad safe haye ketab : {ketabash} ro vared konid: ")
        if safe == "":
            print("shoma tedad safe haye ketab ro moshakhas nakardid!")
            continue
        try:
            tedad_safe = int(safe)
        except ValueError:
            print("lotfan tedad safe haye ketab ro be addad vared konid!")
            continue 
        book = ketab(ketabash,nevisande,tedad_safe)
        majmoe.append(book)
        print("nevisande ba ketabsh be majmoe ezafe shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        if not majmoe:
            print("majmoe nevisandegan khali ast!")
            continue
        for i,book in enumerate(majmoe,start=1):
            print(f"{i} === {book.nevisande}")
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        if not majmoe:
            print("majmoe nevisandegan khali ast!")
            continue
        for i,book in enumerate(majmoe,start=1):
            print(f"{i} === {book.ketab}")
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        if not majmoe:
            print("majmoe nevisandegan khali ast!")
            continue
        for i,book in enumerate(majmoe,start=1):
            print(f"{i} ===> nevisande :{book.nevisande} ===> name ketab :{book.ketab} tedad safe ha : {book.page}" )
    elif choice == "5":
        print("shoma gozine 5 ro ro entekhab kardid!")
        if not majmoe:
            print("majmoe nevisandegan khali ast!")
            continue
        name_book = input("lotfan esm ketab ro vared konid: ")
        if name_book == "":
            print("shoma esm ketab ro vared nakardid!!")
            continue
        if not name_book.isalpha():
            print("lotfan esm ketab ro be horof vared konid! ")
            continue
        found = None
        for book in majmoe:
            if book.ketab == name_book:
                found = book
                break
        if found is None:
            print(f"ketabe be esm : {name_book} peyda nashod!")
            continue
        natije = found.is_long()
        print(f"ketab : {found.ketab} tedad safe ha : {found.page} va vaziyat = {natije}")
    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid va az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 6 entekhab konid!")
        continue

