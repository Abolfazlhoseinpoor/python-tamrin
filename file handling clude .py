import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def save_fruit(esm_file,name):
    with open(esm_file, "a") as f:
        f.write(name + "\n")
def namayesh_fruit(esm_file):
    try:
        with open(esm_file,"r") as f:
            khat = f.readlines()
        if not khat:
            print("file khali ast")
            return
        print(F"list mive ha dar file {esm_file}")
        for i,khatha in enumerate(khat,start=1):
            print(f"{i}======{khatha.strip()}")
    except FileNotFoundError:
        print(f"file be esm {esm_file} peyda nashod!")
        return
while True:
    print("="*30)
    print("gozine 1 == neveshtan file \ngozine 2 == namayesh file\ngozine 3 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        file_name = input("lotfan esm fili ke mikhahid list mive ha dar on zakhire shavad ro vared konid va akharesh (.txt) ro vared konid: ")
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".txt"):
            print("lotfan passvand (.txt ro vared konid!)")
            continue
        mive = input("lotfan esm mive haro vared konid ba fasele: ").split()
        if not mive: 
            print("shoma mive ie ro vared nakardid!")
            continue
        for miveha in mive:
            save_fruit(file_name,miveha)
        print(f"mive ha be file {file_name} zakhire shod!")
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        esm_file = input("lotfan esm file ki mikhahhid namayesh dade shavad ro vared konid ba passvand (.txt): ").strip()
        if esm_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not esm_file.endswith(".txt"):
            print(f"lotfan passvand (.txt) ro dar akhar {esm_file} ezafe konid!")
            continue
        namayesh_fruit(esm_file)
    elif choice == "3":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 3 ro entekhab konid!")
        continue
    

