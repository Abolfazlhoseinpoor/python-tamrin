import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#tamrin 1 log activate
'''from datetime import datetime
time = datetime.now().strftime("%Y - %m - %d - %H:%M")
def log_action(file_name,time):
    with open(file_name,"a") as f:
        f.writelines(time +"\n")
    print("log zakhire shod!")
def namayesh_file (file_name):
    try:
        with open(file_name,"r") as f:
            khat = f.readlines()
        if not khat:
            print("file khali ast!")
            return
        for i,line in enumerate(khat,start=1):
            print(f"{i} === {line}") 
    except FileNotFoundError:
        print(f"{file_name} peyda nashod!")
        return
while True:
    file_name = input("lotfan esm file ke mikhahid log save shavad ro vared konid ba passvand (.txt): ").strip()
    if file_name == "":
        print("shoma esm file ro vared nakardid!")
        continue
    if not file_name.endswith(".txt"):
        print(f"passvand file {file_name} ro faramosh kardid!")
        continue
    break
while True:
    print("="*30)
    print("gozine 1 == log_action\ngozine 2 == namayesh file \ngozine 3 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        log_action(file_name,time)
    elif choice == "2":
        print("shoma goizne 2 ro entekhab kardid!")
        namayesh_file(file_name)
    elif choice == "3":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan gozine 1 ta 3 ro entekhab konid!")
        continue'''
# tamrin 2 copy and backup
'''def write_file(file_name,word):
    with open(file_name, "w") as f:
        f.write(word + "\n")
    print(f"{word} dar {file_name} zakhire shod!")
def show_file(file_name):
    try:
        with open(file_name,"r") as f:
            khat = f.readlines()
        if not khat:
            print(f"{file_name} khali ast!")
            return
        for i,line in enumerate(khat,start=1):
            print(f"{i} === {line}")
    except FileNotFoundError:
        print(f"{file_name} peyda nashod!")
        return
def add_file(file_name,word):
    try:
        with open(file_name,"a") as f:
            f.writelines(word + "\n")
        print(f"matn be {file_name} ezafe shod!")
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
        return
def copy_backup(file_name,new_file):
    try:
        with open(file_name,"r") as f:
            khat = f.readlines()
        if not khat:
            print(f"file {file_name} khali ast!")
            return
        with open(new_file,"w") as n:
            n.writelines(khat + "\n") 
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
        return
while True:
    print("="*30)
    print("gozine 1 == neveshtan file\ngozine 2 == namayesh file \ngozine 3 == ezafe kardan be file \ngozine 4 == copy and backup \ngozine 5 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        file_name = input("lotfan esm file ke mikhahid dar on chizi zakhire konid ro vared konid ba passvand (.txt): ").strip()
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".txt"):
            print(f"passvand {file_name} ro faramosh kardid!")
            continue
        matn = input("lotfan matni ke mikhahid dar on zakhire konid ro vared konid: ").strip()
        if matn == "":
            print("shoma matni ro vared nakardid!")
            continue
        write_file(file_name,matn)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        esm_file = input("lotfan esm file ke mikhahid namayesh dade shavad ro vared konid ba passvand (.txt): ").strip()
        if esm_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not esm_file.endswith(".txt"):
            print(f"passvand {esm_file} ro faramosh kardid!")
            continue
        show_file(esm_file)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        name_file = input("lotfan esm file ke mikhahid be on chizi ezafe konid ro vared konid ba passvand (.txt): ").strip()
        if name_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not name_file.endswith(".txt"):
            print("passvand ro faramosh kardid!")
            continue
        new_matn = input(f"lotfan matn ro vared konid baraye ezafe kardan be file {name_file}: ")
        if new_matn == "":
            print("shoma matni ro vared nakardid!")
            continue
        add_file(name_file,new_matn)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        file = input("lotfan esm file ke mikhahid az on backup begiri do vared konid ba passvand(.txt): ").strip()
        if file == "":
            print("shoma esm file ke mikhahid az on backup begirid ro vared nakardid!")
            continue
        if not file.endswith(".txt"):
            print(f"passvand {file} ro faramosh kardid!")
            continue 
        new_file = input("lotfan esm file jadid ro vared konid ba passvand (.txt): ").strip()
        if new_file == "":
            print("shoma esm file jadid ro vared nakardid!")
            continue
        if not new_file.endswith(".txt"):
            print(f"passvand {new_file} ro faramosh kardid!")
            continue
        copy_backup(file,new_file)
    elif choice == "5":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 5 entekhab konid!")
        continue'''
# tamrin 3 shomaresh kalamt
def write_file (file_name,matn):
    with open(file_name , "w") as f:
        f.write(matn + "\n")
    print(f"{matn} dar file {file_name} zakhire shod!")
def show_file (file_name):
    try:
        with open (file_name , "r") as f:
            line = f.readlines()
        if not line:
            print(f"file {file_name} khali ast!")
            return
        for i,khat in enumerate(line , start=1):
            print(f"{i} === {khat}")
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
        return
def afzodan_be_file (file_name,matn):
    try:
        with open (file_name , "a") as f:
            f.writelines(matn + "\n")
        print(f"matn {matn} be file {file_name} ezafe shod!")
    except  FileNotFoundError:
        print(f"file {file_name} payda nashod!")
        return
def copy_backup(file_name1,file_name2):
    try:
        with open (file_name1 , "r") as f:
            line = f.readlines()
        if not line:
            print(f"file {file_name1} khali ast!")
            return
        with open (file_name2 , "w") as g:
            g.writelines(line)
        print(f"matn dakhle file {file_name1} yek backup be esm {file_name2} be vojod amad va matn file {file_name1} be file {file_name2} copy shod!")
    except FileNotFoundError:
        print(f"file {file_name1} peyda nashod!")
        return
def shoamresh_harf (file_name):
    try:
        with open (file_name , "r") as f:
            line = f.readlines()
        if not line:
            print(f"file {file_name} khali ast")
            return
        shomaresh_khat = len(line)
        kalamat = 0
        for khat in line:
            words = khat.split()
            kalamat += len(words)
        print(f"mohtaviyat file {file_name}")
        print(f"tedad khat {shomaresh_khat}")
        print(f"tedad kalamt {kalamat}")
    except FileNotFoundError:
        print(f"file {file_name} peyda nashod!")
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
    hazf_khat = [line.strip() for line in khat1 if line.strip() != ""]
    hazf_khat2 = [line.strip() for line in khat2 if line.strip() != ""]
    kol_khat = hazf_khat + hazf_khat2
    khatha = []
    for line in kol_khat:
        if line not in khatha:
            khatha.append(line)
    with open (final_file , "w") as l:
        for khat in khatha:
            l.write(khat + "\n")
    jam_khat = len(kol_khat)
    yekta_khat = len(khatha)
    print("edgham anjam shod !")
    print(f"file haye vorodi {file_name1} va {file_name2}")
    print(f"file edgham shode : {final_file}")
    print(f"tedad khat {jam_khat}")
    print(f"tedad khat yekta {yekta_khat}")
while True:
    print("="*30)
    print("goizne 1 == neveshtan file \ngozine 2 == namayesh etelaat zakhire shode dar file \ngozine 3 == ezafe kardan etelaati be file \ngozine 4 == copy va backup file \ngozine 5 == shomaresh kalamt dar file \n gozine 6 == edagham file \n gozine 7 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip().lower()
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro enetkhab kardid!")
        esm_file = input("lotfan esm file ke mikhahid be on matni chizi ezafe konid ro vared konid ba passvand (.txt): ")
        if esm_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not esm_file.endswith(".txt"):
            print(f"passvand file {esm_file} ro faramosh kardid!")
            continue
        matn = input(f"lotfan on matni ke mikhahid be file {esm_file} ro vared konid: ")
        if matn == "":
            print(f"shoma matni ro baraye afzodan be file {esm_file} vared nakardid!")
            continue
        write_file(esm_file,matn)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        file_name = input("lotfan esm file ro kemikhahid namayesh dade shavd ro vared konid ba passvand (.txt): ")
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".txt"):
            print(f"passvand file {file_name} ro faramosh kardid!")
            continue
        show_file(file_name)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        file = input("lotfan esm file ke mikhahid be on matni ezafe konid ro vared konid ba passvand (.txt): ")
        if file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file.endswith(".txt"):
            print(f"passvand file {file} ro faramosh kardid!")
            continue
        add_matn = input(f"lotfan matni ke mikhahid be file {file} ezafe konid ro vared konid: ")
        if add_matn == "":
            print("shoma  matni ro vared nakardid!")
            continue
        afzodan_be_file(file,add_matn)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        name_file = input("lotfan esm file ro vared konid ke mikhahid az on backup begirid ba passvand (.txt): ")
        if name_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not name_file.endswith(".txt"):
            print(f"passvand file {name_file} ro faramosh kardid!")
            continue
        new_file = input(f"lotfan esm file ke mikhahid mohtaviyat file {name_file} dar on zakhire shavad rovared konid ba passvand (.txt): ")
        if new_file == "":
            print("shoma esm file jadid ro vared nakardid!")
            continue
        if not new_file.endswith(".txt"):
            print(f"passvand file {new_file} ro faramosh kardid!")
            continue
        copy_backup(name_file,new_file)
    elif choice == "5":
        print("shoma gozine 5 ro entkhab kardid!")
        filename = input("lotfan esm file ke mikhahid tedad kamatesh ro shomrde shavad ro vared konid ba passvand  (.txt): ")
        if filename == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not filename.endswith(".txt"):
            print(f"shoma passvand file {filename} ro faramosh kardid!")
            continue
        shoamresh_harf(filename) 
    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        file_aval = input("lotfan esm file shomare 1 ro vared konid ba passvand (.txt): ")
        if file_aval == "":
            print("shoma esm file aval ro vared nakardid!")
            continue
        if not file_aval.endswith(".txt"):
            print(f"passvand file {file_aval} ro faramosh kardid!")
            continue
        file_dovom = input("lotfan esm file dovom ro vared konid ba passvand (.txt): ")
        if file_dovom == "":
            print("shoma esm file dovom ro vared nakardid!")
            continue
        if not file_dovom.endswith(".txt"):
            print(f"passvand file {file_dovom} ro faramosh kardid!")
            continue
        final_file = input(f"lotfan esm file ke mikhahid {file_aval} va {file_dovom} ke edgham shavand vared konid ba passvand (.txt): ")
        if final_file == "":
            print("shoma esm file nahayi ro vared nakardid!")
            continue
        if not final_file.endswith(".txt"):
            print(f"passvand file {final_file} ro faramosh kardid!")
            continue
        edgham_file(file_aval,file_dovom,final_file)
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid va az barname kharej shodid bye bye!")
        break
    else:
        print("lotfan az gozine 1 ta 7 entekhab konid!")
        continue
