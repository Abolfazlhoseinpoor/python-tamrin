#tamrin 1 zog ya fard
'''def zog_fard ():
    num = input("lotfan adadi k mikhahid bedonid zog ast ya fard ro vared konid: ").strip()
    if num == "":
        print("shoma addadi ro vared nakardid!")
        return
    try:
        zog_ya_fard = int(num)
    except ValueError:
        print("lotfan addad mored nazar khod ro be addad vared konid!")
        return
    if zog_ya_fard % 2 == 0:
        print(f"addad {zog_ya_fard} zog ast!")
    else:
        print(f"addad {zog_ya_fard} fard ast")
while True:
    print("="*30)
    print("gozine 1 == zog ya fard \ngozine 2 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        zog_fard()
    elif choice == "2":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan gozine 1 ya 2 ro vared konid!")
        continue'''
# tamrin 2 bozorgtarin addad
'''list_addad = []
def add_list(list_addad):
    tedad = input("chnd addad mikhahid be list addad ezafe konid: ").strip()
    if tedad == "":
        print("shoma nagoftid ke chnd addad mikhahid be list addad ezafe konid!")
        return
    try:
        tedad_list = int(tedad)
    except ValueError:
        print("lotfan be addad vared konid!")
        return
    for i in range(tedad_list):
        num = input("lotfan adad khod ro vared konid: ").strip()
        if num == "":
            print("shoma addadi ro vared nakardid!")
            return
        try: 
            num_int = int(num)
        except ValueError:
            print(f"lotfan addad mored nazar khod : {num} ro be addad vared konid na horof!")
            return
        list_addad.append(num_int)
    print("addad be list addad ezafe shodan!")
def find_max(list_addad):
    if not list_addad:
        print("list addad khali ast")
        return
    max_num = list_addad[0]
    for i in list_addad:
        if i > max_num:
            max_num = i
    print(f"bozorgtarin addad dar list addad --> {max_num}")
def clear_list (list_addad):
    if not list_addad:
        print("list addad khali ast")
        return
    list_addad.clear()
    print("list addad kamle pak shod!")
def show_list(list_addad):
    if not list_addad:
        print("list addad khali ast")
        return
    print(f"list addad shoma \n {list_addad}")
while True:
    print("="*30)
    print("gozine 1 == ezafe kardan addad be list addad \ngozine 2 == peyda kardan bozorgtarin addad \ngozine 3 == pak kardan list addad\ngoznie 4 == namayesh list \ngozine 5 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        add_list(list_addad)
    elif choice == "2":
        print("shoma gozine 2 ro enetkhab kardid!")
        find_max(list_addad)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        clear_list(list_addad)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        show_list(list_addad)
    elif choice == "5":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 5 entekhab konid!")
        continue'''
list_school = {}
def add_class (list_school):
    klass = input("chnd ta klass mikhahid ezafe konid?: ").strip()
    if klass == "":
        print("shoma nagoftid chn ta class mikhahid ezafe konid!")
        return
    try:
        tedad_klass = int(klass)
    except ValueError:
        print("lotfan tedad klass ro be addad vared konid!")
        return
    for i in range(tedad_klass):
        name_klass = input("lotfan esm klass ro vared konid: ").strip()
        if name_klass == "":
            print("shoma esm klassi ro vared nakardid!")
            return
        if name_klass in list_school:
            print(f"{name_klass} dar list class haye madrese vojod darad!")
            continue
        list_school[name_klass] = {}
    print("class ha be list class haye madrese ezafe shod!")
def add_student (list_school):
    wich_klass = input("danesh amozan ro mikhahid be kodom klass ezafe konid: ").strip()
    if wich_klass == "":
        print("shoma nagoftid ke kodom klass mikhaid danesh amooz ro ezafe konid!")
        return
    if wich_klass not in list_school:
        print(f"{wich_klass} dar list klass haye madrese peyda nashod!")
        return
    student = input(f"chnd ta danesh amooz mikhahid be kelass {wich_klass} ezafe konid?: ").strip()
    if student == "":
        print(f"shoma moshakhas nakardid ke chnd ta danesh amooz ro baraye ezafe kardan be {wich_klass} vared nakardid!")
        return
    try:
        tedad_student = int(student)
    except ValueError:
        print(f"lotfan tedad danesh amoozani ke mikhahid be {wich_klass} ro be addad vared konid! ")
        return
    for m in range(tedad_student):
        name_student = input(f"lotfan esm danesh amooz ro baraye ezafe kardan be {wich_klass} vared konid: ").strip()
        if name_student == "":
            print("shoma esm danesh amooz ro vared nakardid!")
            return
        if name_student in list_school[wich_klass]:
            print(f"danesh amooz {name_student} dar list danesh amozan klass {wich_klass} vojod darad!")
            continue
        list_school[wich_klass][name_student] = []
    print(f"danesh amozan ha be list danesh amozan {wich_klass} madrese ezafe shod!")
def add_lesson_grade (list_school):
    name_klass = input("lotfan esm klass ro vared konid: ").strip()
    if name_klass == "":
        print("shoma esm klass ro vared nakardid!")
        return
    if name_klass not in list_school:
        print(f"klassi be name {name_klass} dar list klass haye madrese vojod nadarad!")
        return
    name_student = input("lotfan esm danesh amooz ro vared konid: ").strip()
    if name_student == "":
        print("shoma esm danesh amooz ro vared nakardid!")
        return
    if name_student not in list_school[name_klass]:
        print(f"esm danesh amooz dar list danesh amozan klass {name_klass} vojod nadarad!")
        return
    nomarat_dars = []
    while True:
        dars = input("lotfan esm dars ro vared konid: ").strip()
        if dars == "":
            print("shoma esm dars ro vared nakardid!")
            break
        nomre = input(f"lotfan nomre dars {dars} ro vared konid: ").strip()
        if nomre == "":
            print(f"shoma nomre dars {dars} ro vared nakardid!")
            break
        try:
            nomre_addad = float(nomre)
        except ValueError:
            print(f"lotfan nomre dars {dars} ro be addad vared konid!")
            continue
        nomarat_dars.append((dars,nomre_addad))
    list_school[name_klass][name_student] = nomarat_dars
    print(f"esm dars ba nomre be list nomarat danesh amooz {name_student} ezafe shod!")
def show_klass (list_school):
    if not list_school:
        print("list klass haye madrese khali ast!")
        return
    print(f"list kelas haye madrese: \n {i} === {name}")
    for  i ,name in enumerate(list_school.keys(),start=1):
        print(f"{i} === {name}")
def show_student (list_school):
    if not list_school:
        print("list klass ha va list danesh amozan madrese khali ast!")
        return
    name_kelass = input("lotfan esm kelassi ke mikhahid danesh amozan ro bebinid ro vared konid: ").strip()
    if name_kelass == "":
        print("shoma esm kelas baraye namayesh danesh amozan vared nakardid!")
        return
    if name_kelass not in list_school:
        print(f"esm {name_kelass} dar list kelas haye madrese vojod nadarad!")
        return
    print(f"danesh amozan kelass {name_kelass}:")
    for i,name in enumerate(list_school[name_kelass].keys(),start=1):
        print(f"{i} === {name}")
def show_nomre (list_school):
    if not list_school:
        print("list klass ha va danesh amozan va nomarat madrese khali ast!")
        return
    name_kelass = input("lotfan esm kelass ro vared konid: ").strip()
    if name_kelass == "":
        print("shoma esm kelass ro vared nakardid!")
        return
    if name_kelass not in list_school:
        print(f"esm {name_kelass} dar list kelass haye madrese vojod nadarad!")
        return
    name_student = input("lotfan esm danesh amoozi ke mikhahid nomaratash ro bebinind vared konid: ").strip()
    if name_student == "":
        print("shoma esm danesh amooz ro vared nakardid!")
        return
    if name_student not in list_school[name_kelass]:
        print(f"danesh amooz {name_student} dar list danesh amozan kelass {name_kelass} vojod nadarad!")
        return
    nomrarat =list_school[name_kelass][name_student]
    if not nomrarat:
        print("hanoz nomre ie sabt nashode!")
        return
    print(f"list nomarat danesh amooz {name_student}: ")
    for i,(dars,nomre) in enumerate(nomrarat,start=1):
        print(f"{i} ==== {dars} === {nomre}")
def gozaresh(list_school):
    if not list_school:
        print("list klass ha va danesh amozan va nomarat madrese khali ast!")
        return
    name_klass = input("lotfan esm klass ro vared konid: ").strip()
    if name_klass == "":
        print("shoma esm kelass ro vared nakardid!")
        return
    if name_klass not in list_school:
        print(F"{name_klass} dar list kelass ha vojod nadarad!")
        return
    name_student = input("lotfan esm danesh amooz ro vared konid: ").strip()
    if name_student == "":
        print("shoma esm danesh amooz ro vared nakardid!")
        return
    if name_student not in list_school[name_klass]:
        print(f"esm danesh amooz {name_student} dar list danesh amozan vojod nadarad!")
        return
    score = list_school[name_klass][name_student]
    if not score:
        print("nomre ie vojod nadarad!")
        return
    nomere = [nomerat for (dars,nomerat) in score]
    miangin = sum(nomere) / len(nomere)
    max_nomre = nomere[0]
    min_nomre = nomere[0]    
    for m in nomere[1:]:
        if m > max_nomre:
            max_nomre = m
        if m < min_nomre:
            min_nomre = m
    print("="*30)
    print(f"gozaresh vaziyat danesh amooz {name_student} dar {name_klass}")
    print(f"miangin nomarat === {miangin}")
    print(f"bala tarin nomre === {max_nomre}")
    print(f"paien tarin nomre === {min_nomre}")
while True:
    print("="*30)
    print("goizne 1 == ezafe kardan kelas \ngozine 2 == ezafe kardan danesh amooz \ngozine 3 == ezafe kardan nomarat dars haye danesh amozan \ngozine 4 == namayesh list kelasha \
          \ngozine 5 == namayesh danesh amozan kelas \ngozine 6 == namayesh nomarat danesh amoz \ngozine 7 == vaziyat danesh amooz \ngozine 8 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ").strip()
    if choice == "":
        print("shoma gozine ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        add_class(list_school)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        add_student(list_school)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        add_lesson_grade(list_school)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        show_klass(list_school)
    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid!")
        show_student(list_school)
    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        show_nomre(list_school)
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid!")
        gozaresh(list_school)
    elif choice == "8":
        print("shoma az barname kharej shodid!")
        break
    else:
        print("lotfan az gozine 1 ta 8 entekhab konid!")
        continue
