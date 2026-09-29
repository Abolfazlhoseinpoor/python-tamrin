import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def save_fruit(file_name,miveha):
    with open(file_name,"a") as f:
        f.write(miveha + "\n")
def show_fruit(file_name):
    try:
        with open(file_name,"r") as f:
            khat = f.readlines()
        if not khat:
            print("file khali ast!")
            return
        print(f"list mive ha dar file {file_name}")
        for i,mive in enumerate(khat,start=1):
            print(f"{i}--{mive}")
    except FileNotFoundError:
        print(f"file be esm {file_name} peyda nashod!")
        return
def virayesh(file_name,mive):
    while True:
        noye_virayesh = input("lotfan noye viryaesh (hazf ya taghir ya baraye khorg as halat virayesh exit ro vared konid): ").strip()
        if noye_virayesh == "":
            print("lotfan noye virayesh ro vared konid!")
            continue
        if noye_virayesh == "hazf":
            print("shoma gozine hazf ro entekhab kardid!")
            try:
                with open(file_name,"r") as f:
                    khat = f.readlines()
                if not khat:
                    print(f"file {file_name} khali ast!")
                    break
                khat_jadid = []
                shomaresh_hazf = 0
                for i in khat:
                    if i.strip() == mive:
                        shomaresh_hazf += 1
                    else:
                        khat_jadid.append(i)
                if shomaresh_hazf == 0:
                    print(f"mive {mive} dar file peyda nashod")
                    break
                with open(file_name,"w") as f:
                    f.writelines(khat_jadid)
                print(f"{shomaresh_hazf} mored as {mive} dar file {file_name} hazf shod!")
            except FileNotFoundError:
                print(f"{file_name} peyda nashod!")
                break
        elif noye_virayesh == "taghir":
            print("shoma halat taghir ro entekhab kardid!")
            new_mive = input(f"lotfan esm mive ke mikahhid jaygozin {mive} ro vared konid: ").strip()
            if new_mive == "":
                print("shoma esm ive ro baraye jaygozin vared nakardid!")
                continue
            if not new_mive.isalpha():
                print("lotfan esm jaygozine ba mive ghabli ro ba horof vared konid!")
                continue
            try:
                with open(file_name, "r") as f:
                    line = f.readlines()
                if not line:
                    print(F"{file_name} khali ast!")
                    break
                new_khat = []
                shomaresh_jaygozari = 0
                for m in line:
                    if m.strip() == mive:
                        new_khat.append(new_mive + "\n")
                        shomaresh_jaygozari += 1
                    else:
                        new_khat.append(m)
                if shomaresh_jaygozari == 0:
                    print(f"{new_mive} dar {file_name} peyda nashod!")
                    continue
                with open(file_name,"w") as f:
                    f.writelines(new_khat)
                print(f"{new_mive} ba {mive} jaygozin shod!")
            except FileNotFoundError:
                print(f"{file_name} peyda nashod!")
                break
        elif noye_virayesh == "exit":
            print("shoma az halat virayesh kharej shodid!")
            break
        else:
            print("taghir ya hazf ya exit ro vared konid!")
            continue
def amar (file_name):
    try:
        with open(file_name,"r") as f:
            khat = f.readlines()
        if not khat:
            print(f"{file_name} khali ast!")
            return
        miveha = []
        for i in khat:
            name = i.strip()
            if name:
                miveha.append(name)
        dictha = {}
        for mive in miveha:
            if mive in dictha:
                dictha[mive] += 1
            else:
                dictha[mive] = 1
        mive_yekta = len(dictha)
        balatarin = 0
        bishtarin_mive = None
        for fruit , shomaresh in dictha.items():
            if shomaresh > balatarin:
                balatarin = shomaresh
                bishtarin_mive = fruit
        print(f"tahill {file_name}")
        print(f"tedad mive haye yekta: {mive_yekta}")
        if bishtarin_mive is not None:
            print(f"portekrar tarin mive {bishtarin_mive} ba {balatarin} bar tekrar!")
    except FileNotFoundError:
        print(f"{file_name} peyda nashod!")
        return
while True:
    print("="*30)
    print("gozine 1 == neveshtan mive ha dar file \ngozine 2 namayesh file ke mive ha rar on zakhire shodand \ngozine 3 == virayesh \ngozine 4 == shomaresh va amar \ngozine 5 == exit")
    print("="*30)  
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma goizne 1 ro entekhab kardid!")
        file_name = input("lotfan esm file ke mikhahid sakhte beshe ta mive ha dar on zakhire shavad ro vared konid ba passvand(.txt): ").strip()
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".txt"):
            print("shoma passvand (.txt) ro faramosh kardid!")
            continue
        mive = input("lotfan esm mive haro vared konid ba fasele: ")
        if mive == "":
            print("shoma mive ie ro vared nakardid!")
            continue
        miveha = mive.split()
        for i in miveha:
            save_fruit(file_name,i)
        print(f"mive ha dar {file_name} zakhire shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        esm_file = input("lotfan esm file ie ke mikhahid namayesh dade shavad ro vared konid ba passvand (.txt): ").strip()
        if esm_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not esm_file.endswith(".txt"):
            print("passvand (.txt) ro faramosh kardid!")
            continue
        show_fruit(esm_file)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        name_file = input("lotfan esm file ke mikhahid virayesh konid ro vared konid ba passvand(.txt): ").strip()
        if name_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not name_file.endswith(".txt"):
            print("passvand (.txt) ro faramosh kardid!")
            continue
        name_mive = input("lotfan esm mive ke mikahid taghir dahid ro vared konid: ").strip()
        if name_mive == "":
            print("shoma esm mive ro vared nakardid!")
            continue
        if not name_mive.isalpha():
            print("lotfan esm mive ro baraye virayesh be horof vared konid!")
            continue
        virayesh(name_file,name_mive)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        file = input("lotfan esm file ke mikhahid amar begirid ro vared konid ba passvand (.txt): ").strip()
        if file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file.endswith(".txt"):
            print("shoma passvand (.txt) ro faramosh kardid!")
            continue
        amar(file)
    elif choice == "5":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 5 entekhab konid!")
        continue
