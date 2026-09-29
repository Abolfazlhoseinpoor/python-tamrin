import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import json
product = [
    {"name":"pirahan","price": 150_000,"quantitiy":5},
    {"name":"shalvar","price":200_000,"quantitiy":0},
    {"name":"kafsh","price":350_000,"quantitiy":3}
    ]
def save_product (products,file_name):
    try:
        with open(file_name , "w") as f:
            json.dump(products,f,ensure_ascii=False,indent=4)
    except PermissionError:
        print("shoma dastrasi be neveshtan file nadarid!")
        return
    print(f"product dar file: {file_name} zakhire shod!")
def show_availabe(file_name):
    try:
        with open(file_name , "r") as f:
            khat = json.load(f)
        if not khat:
            print(F"file : {file_name} khali ast!")
            return
    except FileNotFoundError:
        print(f"file : {file_name} peyda nashod!")
        return
    print("mahsolat mojod")
    for i,ajnas in enumerate(khat,start=1):
        name = ajnas.get("name","-")
        price = ajnas.get("price",0)
        qty = ajnas.get("quantitiy")
        if qty > 0:
            print(f"{i} ===> esm kala ==> {name} gheymat ==> {price} tedad ==> {qty}" )
while True:
    print("="*30)
    print("gozine 1 == neveshtan file \ngozine 2 == namayesh file \ngozine 3 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        file_name = input("lotfan esm file ke mikahid neveshte shavd produt ro vared konid: ")
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".json"):
            file = file_name + ".json"
        else:
            file = file_name
        save_product(product,file)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        show_file = input("lotfan esm file ke mikahhid namayesh dade shavad ro vared konid: ")
        if show_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not show_file.endswith(".json"):
            file2 = show_file + ".json"
        else:
            file2 = show_file
        show_availabe(file2)
    elif choice == "3":
        print("shoma az barname kharej shodid bye bye")
        break
    else:
        print("lotfan az gozine 1 ta 3 entekhab konid")
        continue