#tamrin 1 module
import product_tool
while True:
    print("="*30)
    print("goizne 1 == ghyamat bad az takhfif \ngozine 2 == joda konnade\ngozine 3 == tedad jens kala  \ngozine 4 == exit")
    print("="*30) 
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro enetkhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro enetkhab kardid!")
        gheymat = input("lotfan mablagh kala ro vared konid: ")
        if gheymat == "":
            print("shoma mablagh kala ro vared nakardid!")
            continue
        try:
            mablagh = int(gheymat)
        except ValueError:
            print(f"lotfan mablagh kala ro be addad vared konid! shoma {gheymat} ino vared kardid!")
            continue
        takhfif = input("lotfan darsad takhfif kala ro vared konid: ")
        if takhfif == "":
            print("shoma darsad takhfif ro vared nakardid!")
            continue
        try:
            percent = float(takhfif)
        except ValueError:
            print(f"lotfan darsad takhfif ro be addad vared konid! shoma {takhfif} ino vared kardid!")
            continue
        mablagh_final = product_tool.add_dicount(mablagh,percent)
        print(f"mablagh nahayi mishe === {mablagh_final}")
    elif choice == "2":
        print("shoma gozine 2 ro entkhab kardid!")
        price = input("lotfan mablagh kala ro vared konid ta sysytem joda konad tabdil konad masalan === (150000 === 150,000) : ")
        if price == "":
            print("shoma gheymat kala ro vared nakardid baraye jodasazi!")
            continue
        try:
            price_int = int(price)
        except ValueError:
            print(f"shoma bayad gheymat kala ro be addad vared konid!")
            continue
        joda_price = product_tool.format_price(price_int)
        print(f"mabalagh {price} mishe === {joda_price}")
    elif choice == "3":
        print("shoma goizne 3 ro entekhab kardid!")
        tedad = input("lotfan tedad kala ro vared konid: ")
        if tedad == "":
            print("shoma tedad kala ro vared nakardid!")
            continue
        try:
            count = int(tedad)
        except ValueError:
            print(f"lotfan tedad kala ro be addad vared konid!")
            continue
        natije = product_tool.is_in_stock(count)
        print(natije)
        

