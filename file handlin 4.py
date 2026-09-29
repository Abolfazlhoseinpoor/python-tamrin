import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def write_file  (file_name,matn):
    try:
        with open(file_name,"w") as f:
            f.write(matn + "\n")
        print(f"matn shoma dar file {file_name} zakhire shod!")
    except PermissionError:
        print("shoma hagh file nevisis nadarid!")
        return
def add_file (file_name,matn):
    try:
        with open(file_name,"a") as f:
            f.write(matn + "\n")
        print(f"matn shoma be file {file_name} ezafe shod!")
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
        return
    except PermissionError:
        print(f"shoma dastarasi be file {file_name} nadarid baraye afzodan matn be file!")
        return
def show_file (file_name):
    try:
        with open (file_name , "r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file {file_name} khali ast!")
            return
        for i,line in enumerate(khat,start= 1):
            print(f"{i} === {line}")
    except FileNotFoundError:
        print(F"file {file_name} peyda nashod!")
        return
def copy_backup(file_name1,file_name2,matn):
    try:
        with open(file_name1,"r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file {file_name1} khali ast")
            return
        with open(file_name2 , "w") as g:
            g.writelines(khat)
        with open(file_name1 , "w") as d:
            d.write(matn + "\n")
        print(f"az file {file_name1} copy gerefte shod va matn mored nazar dar on jaygozarri shod!")
    except FileNotFoundError as e:
        print(f"file {e} peyda nashod!")
        return
    except PermissionError as t:
        print(f"shoma dastrasi be taghir file {t} ro nadarid!")
        return
def edgham_file (file_name1,file_name2,final_file):
    try:
        with open(file_name1 , "r") as f:
            khat1 = f.readlines()
        if not khat1:
            print(f"file {file_name1} khali ast!")
            return
        with open(file_name2 , "r") as g:
            khat2 = g.readlines()
        if not khat2:
            print(f"file {file_name2} khali ast!")
            return
    except FileNotFoundError as e:
        print(f"file {e} peyda nashod!")
        return
    kol_khat1 = [khat.strip() for khat in khat1 if khat.strip() != "" ]
    kol_khat2 = [khat.strip() for khat in khat2 if khat.strip() != "" ]
    edgham = kol_khat1 + kol_khat2
    khatha = []
    for i in edgham:
        if i not in khatha:
            khatha.append(i)
    try:
        with open(final_file , "w") as r:
            r.write("\n".join(khatha))
    except PermissionError:
        print(f"shoma dastrasi be neveshtan file {final_file}")
        return
    tedad_khat = len(edgham)
    yekta_khat = len(khatha)
    print("edgham anjam shod!")
    print(f"edgham file aval : {file_name1} va file dovom : {file_name2} dar file: {final_file} rikhte shod!")
    print(f"tedad khatha {tedad_khat}")
    print(f"tedad khat haye yekta shode: {yekta_khat}")
def count_words (file_name):
    try:
        with open(file_name , "r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file {file_name} khali ast!")
            return
    except FileNotFoundError:
        print(f"file : {file_name} peyda nashod!")
        return
    count_line = len(khat)
    count_kalame = 0
    for i in khat:
        kalame = i.split()
        count_kalame += len(kalame)
    print(f"tedad khat haye file {file_name} : === {count_line}")
    print(f"tedad horof dar file {file_name} : === {count_kalame}")
while True:
    print("="*30)
    print("gozine 1 == neveshtan dar file  \ngozine 2 == afzodan be file \ngozine 3 == namayesh file \ngozine 4 == copuy va backup  az file \ngozine 5 == edgham file \n gozine 6 == shomaresh kalamat \ngozine 7 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid")
        file_name = input("lotfan esm file ke mikhahid mohtavayi ro dar on benevisisd ro vared konid ba passvand (.txt): ")
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".txt"):
            print(f"shoma passvand file {file_name} ro faramosh kardid!")
            continue
        matn = input(f"lotfan on matni ke mikahhid dar file {file_name} benevisid ro vared konid: ")
        if matn == "":
            print("shona matni ro vared nakardid!")
            continue
        write_file(file_name,matn)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        name_file = input("lotfan esm file ke mikhahid be on matni ezafe konid ro vared konid ba passvand (.txt): ")
        if name_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not name_file.endswith(".txt"):
            print(f"shoma passvand file {name_file} ro faramosh kardid!")
            continue
        add_matn = input(f"lotfan matni ke mikahhid be file {name_file} ezafe konid ro avred konid: ")
        if add_matn == "":
            print("shoma matni ro vared nakardid!")
            continue
        add_file(name_file,add_matn)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        esm_file = input("lotfan esm file ke mikhahid namayesh dade shavad ro vared konid ba passvand (.txt): ")
        if esm_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not esm_file.endswith(".txt"):
            print(f"passvand file {esm_file} ro afarmosh kardid!")
            continue
        show_file(esm_file)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        file = input("lotfan esm file ke mikhahid copy az on begirid ro vared konid ba passvand (.txt): ")
        if file == "":
            print("shoma esm file ro vared nakardid! ")
            continue
        if not file.endswith(".txt"):
            print(f"shoma passvand file {file} ro faramosh kardid!")
            continue
        backup_file = input(f"lotfan esm file dovom ke mikhahid backupi az file {file} bashad ro vared konid ba passvand (.txt): ")
        if backup_file == "":
            print("lotfan esm file backup ro vared nakardid!")
            continue
        if not backup_file.endswith(".txt"):
            print(f"passvnad file {file} ro faramosh kardid!")
            continue
        neveshtan_file = input(f"lotfan on mtni ke mikhahid be file {file} ezafe konid ro vared konid: ")
        if neveshtan_file == "":
            print("shoma matni ro naneveshtid!")
            continue
        copy_backup(file,backup_file,neveshtan_file)
    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid!")
        first_file = input("lotfan esm file aval ke mikhahid edgham shavad ba file dovom ro benevisid ba passvand (.txt): ")
        if first_file == "":
            print("shoma esm file aval ro vared nakardid!")
            continue
        if not first_file.endswith(".txt"):
            print(f"passvand file aval : {first_file} ro faramosh kardid!")
            continue
        second_file = input(f"lotfan esm file dovom ke mikhahid ba file aval {first_file} edgham shavd ro vared konid ba passvand (.txt): ")
        if second_file == "":
            print("shoma esm file dovom ro vared nakardid!")
            continue
        if not second_file.endswith(".txt"):
            print(f"passvand file dovom : {second_file} ro faramosh kardid!")
            continue
        final_file = input("lotfan esm file nahayi ke edgham shode file aval : {first_file} va file dovom : {second_file} ro vared konid ba passvand (.txt): ")
        if final_file == "":
            print("shoma esm file nahayi ro vared nakardid!")
            print("chon vared nakardid esm file nahayi mishe ==== final_file.txt!")
            final_file = "final_file.txt"
        if not final_file.endswith(".txt"):
            print(f"passvand file nahayi : {final_file} ro faramosh kardid!")
            continue
        edgham_file(first_file,second_file,final_file)
    elif choice == "6":
        print("shoama gozine 6 ro entekhab kardid!")
        count_file = input("lotfan esm file ke mikhahid tedad matn haye on shomorde shavad ro vared konid ba passvand (.txt): ")
        if count_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not count_file.endswith(".txt"):
            print(f"passvand file : {count_file} ro faramosh kardid!")
            continue
        count_words(count_file)
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid va az barname kharej shodid!")
        break
    else:
        print("shoma bayad gozine 1 ta 7 entekhab konid!")
        continue