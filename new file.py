import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def write_file(file_name,word):
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
        continue