import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import json
school = {}
def add_class (class_name):
    if class_name in school:
        print(f"in class vojod darad! : {class_name}")
        return
    school[class_name] = {}
    print(f"esm class : {class_name} be list class madrese ezafe shod!")
def add_daneshamooz (class_name,danesh_amooz):
    if not school:
        print("classi vojod nadarad!")
        return
    if not class_name in school:
        print(f"class : {class_name} dar list class ha vojod nadarad!")
        return
    if danesh_amooz in school[class_name]:
        print(f"danesh amooz : {danesh_amooz} dar list danesh amozan class: {class_name} vojod darad!" )
        return
    school[class_name][danesh_amooz] = {}
    print(f"danesh amooz : {danesh_amooz} be danesh amozan class : {class_name} ezafe shod!")
def add_nomre (class_name,danesh_amooz):
    if not school:
        print("classi vojod nadarad!")
        return
    if not class_name in school:
        print(f"class : {class_name} dar list class ha vojod nadarad!")
        return
    if not danesh_amooz in school[class_name]:
        print(f"danesh amooz : {danesh_amooz} dar list danesh amoozan class : {class_name} vojod nadarad!")
        return
    tedad_dars = input(f"nomrat chnd ta dars mikhahid ezafe konid be nomarat danesh amooz: {danesh_amooz}: ")
    if tedad_dars =="":
        print("shoma tedad nomrat dars ro moshkhas nakardid!")
        return
    try:
        doros =int(tedad_dars)
    except ValueError:
        print(f"lotfan tedad dars ro be addad vared konid: shoma ino vared kardid ==> {tedad_dars}")
        return
    for i in range(doros):
        print(f"dars: {i+1}")
        esm_dars = input("lotfan esm dars ro vared konid: ")
        if esm_dars == "":
            print("shoma esm dars ro vared nakardid!")
            return
        nomre = input(f"lotfan nomre dars {esm_dars} ro vared konid: ")
        if nomre == "":
            print("shoma nomre dars ro vared nakardid!")
            return
        try:
            grade = float(nomre)
        except ValueError:
            print(f"lotfan nomre dars {esm_dars} ro be adda dvared konid: shoma ino vared kardid ==> {nomre}")
            return
        school[class_name][danesh_amooz][esm_dars] = grade
    print(f"nomarat danesh amooz {danesh_amooz} ezafe shod!")
def show_class ():
    if school:
        print(f"tedad class haye madrse: {len(school.keys())}")
        for i,esm_class in enumerate(school.keys(),start=1):
            print(f"{i} === {esm_class}")
    else:
        print("classi vojod nadard!")
        return
def show_student(class_name):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class: {class_name} dar list kelass ha vojod nadard!")
        return
    if not school[class_name]:
        print("danesh amoozi vojod nadarad!")
        return
    print(f"tedad danehs amoozan class : {class_name} : {len(school[class_name].keys())}")
    for i,esm_student in enumerate(school[class_name].keys(),start=1):
        print(f"{i} === {esm_student}")
def show_grade(class_name,student_name):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class: {class_name} dar list kelass ha vojod nadard!")
        return
    if not school[class_name]:
        print("danesh amoozi vojod nadarad!")
        return
    if not student_name in school[class_name]:
        print(f"danesh amooz  {student_name} dar list danesh amozan vojod nadarad!")
        return
    if not school[class_name][student_name]:
        print(f"nomre danesh amooz: {student_name} vojod nadarad!")
        return
    print(f"tedad dars ha === {len(school[class_name][student_name].keys())}")
    grade = school[class_name][student_name]
    for i,(dars,nomre) in enumerate(grade.items(),start=1):
        print(f"{i} ===> {dars} ===> {nomre}")
def delete_class (class_name):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class : {class_name} dar list class ha vojod nadarad!")
        return
    school.pop(class_name)
    print(f"class : {class_name} az list class haye madrese hazf shod!")
def delelte_student (class_name,student_name):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class: {class_name} dar list kelass ha vojod nadard!")
        return
    if not school[class_name]:
        print("danesh amoozi vojod nadarad!")
        return
    if not student_name in school[class_name]:
        print(f"danesh amooz  {student_name} dar list danesh amozan vojod nadarad!")
        return
    school[class_name].pop(student_name)
    print(f"danesh amooz {student_name} az danesh amoozan class : {class_name} hazf shod!")
def delete_dars (class_name,student_name,dars):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class: {class_name} dar list kelass ha vojod nadard!")
        return
    if not school[class_name]:
        print("danesh amoozi vojod nadarad!")
        return
    if not student_name in school[class_name]:
        print(f"danesh amooz  {student_name} dar list danesh amozan vojod nadarad!")
        return
    if not school[class_name][student_name]:
        print(f"nomre ie baraye danesh amoz: {student_name} vojod nadarad")
        return
    if not dars in school[class_name][student_name]:
        print(f"dars : {dars} dar nomarat danesh amooz : {student_name} vojod nadarad!")
        return
    school[class_name][student_name].pop(dars)
    print(f"dars : {dars} az nomarat danesh amooz: {student_name} hazf shod!")
def clear_school():
    school.clear()
    print("madrese khali shod!")
def miangin_nomarat(class_name,student_name):
    if not school:
        print("madrese khali ast!")
        return
    if not class_name in school:
        print(f"class: {class_name} dar list kelass ha vojod nadard!")
        return
    if not school[class_name]:
        print("danesh amoozi vojod nadarad!")
        return
    if not student_name in school[class_name]:
        print(f"danesh amooz  {student_name} dar list danesh amozan vojod nadarad!")
        return
    if not school[class_name][student_name]:
        print(f"nomre ie baraye danesh amoz: {student_name} vojod nadarad")
        return
    nomarat = school[class_name][student_name].values()
    tedad_dars = len(nomarat)
    jam_nomarat = sum(nomarat)
    print(f"jam noamarat = {jam_nomarat}")
    print(f"miangin nomarat danesh amooz: {student_name} = {jam_nomarat / tedad_dars}")
def write_file (name_file):
    if not school:
        print("madrese khali ast!")
        return
    try:
        with open (name_file , "w" ) as f:
            json.dump(school , f ,ensure_ascii=False,indent=4)
    except PermissionError:
        print("shoma dastarasi be neveshtan file nadarid!")
        return
    print(f"dar file : {name_file} zakhire shod!")
def show_file(name_file):
    try:
        with open (name_file , "r") as f:
            data = json.load(f)
        if not data:
            print(f"file : {name_file} khali ast!")
            return
    except FileNotFoundError:
        print(f"file : {name_file} peyda nashod!")
        return
    for i, (name_class,daneshamooz)  in enumerate(data.items(),start=1) :
        print(f"{i} == esm class : {name_class}")
        for j , (stu_name,nomre) in enumerate(daneshamooz.items(),start=1):
            print(f"{j} . {stu_name} : {nomre}")
while True:
    print("="*30)
    print("goizine 1  == afzodan class \ngozine 2 == afzodan danesh amooz \ngozine 3 == afzodan nommre danesh amooz \ngozine 4 == namayesh class ha \ngozine 5 == namayesh danesh amozan class \ngozine 6 == namayesh list nomarat danesh amooz\ngozine 7 == hazf kelas \ngozine 8 == hazf danesh amooz \ngozine 9 == hazf dars ba nomre \ngozine 10 == pak kardan kamel madrese \ngozine 11 == miangin nomarat danesh amooz \ngozine 1 == navaeshtan list class ha va danesh amozan va nomarat dar file \ngozine 13 == namayesh file \ngozine 14 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ro enetkhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro enetkhab kardid!")
        name_class = input("lotfan esm class ro vared konid: ")
        if name_class == "":
            print("shoma esm class ro vared nakardid!")
            continue
        add_class(name_class)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        class_name = input("lotfan esm class ro vared konid ke mikhahhid danesh amooz ro dar dar on classs sabt konid: ")
        if class_name == "":
            print("shoma esm class ro vared nakardid!")
            continue
        name_danesh_amooz = input("lotfan esm danesh amooz ro vared konid: ")
        if name_danesh_amooz == "":
            print("shoma esm danesh amooz ro vared nakardid!")
            continue
        add_daneshamooz(class_name,name_danesh_amooz)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        esm_class = input("lotfan esm class ro vared konid: ")
        if esm_class == "":
            print("shoma esm class ro vared nakardid!")
            continue
        esm_danesh_amooz = input("lotfan esm danesh amooz ro vared konid: ")
        if esm_danesh_amooz == "":
            print("shoma esm danesh amooz ro vared nakardid!")
            continue
        add_nomre(esm_class,esm_danesh_amooz)
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        show_class()
    elif choice == "5":
        print("shoma gozine 5 ro enetkhab kardid!")
        class_show = input("lotfan esm class i ke mikhahid danesh amozanash namayesh dade shavad ro vared konid: ")
        if class_show == "":
            print("shoma esm classi ro vared nakardid!")
            continue
        show_student(class_show)
    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        kelass = input("lotfan esm class ro vared konid: ")
        if kelass == "":
            print("shoma esm class ro vared nakardid!")
            continue
        student_name = input("lotfan esm danesh amooz ro vared konid: ")
        if student_name == "":
            print("Shoma esm danesh amooz ro vared nakardid!")
            continue
        show_grade(kelass,student_name)
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid!")
        hazf_kelas = input("lotfan esm classi ke mikhahid hazf konid ro vared konid:  ")
        if hazf_kelas == "":
            print("shoma esm class ro vared nakardid!")
            continue
        delete_class(hazf_kelas)
    elif choice == "8":
        print("shoma gozine 8 ro enetkhab kardid!")
        delete_kelass = input("lotfan esm class ro vared konid: ")
        if delete_kelass == "":
            print("shoma esm class ro vared nakardid!")
            continue
        hazf_student = input("lotfan esm danesh amooz ro vared konid: ")
        if hazf_student == "":
            print("shoma esm danesh amooz ro vared nakardid!")
            continue
        delelte_student(delete_kelass,hazf_student)
    elif choice == "9":
        print("shoma gozine 9 ro entekhab kardid!")
        del_class = input("lotfan esm class ro vared konid: ")
        if del_class == "":
            print("shoma esm class ro vared nakardid!")
            continue
        del_student = input("lotfan esm danesh amooz ro vared konid:")
        if del_student == "":
            print("shoam esm danesh amooz ro vared nakardid!")
            continue
        dars = input("lotfan esm dars ro vared konid: ")
        if dars == "":
            print("shoma esm dars ro vared nakardid!")
            continue
        delete_dars(del_class,del_student,dars)
    elif choice == "10":
        print("shoma gozine 10 ro enetkhab kardid!")
        clear_school()
    elif choice == "11":
        print("shoma gozine 11 ro enetkhab kardid!")
        miangin_class = input("lotfan esm danesh amooz ro vared konid: ")
        if miangin_class == "":
            print("shoma esm class ro vared nakardid! ")
            continue
        miangin_student = input("lotfan esm danesh amooz ro vared konid: ")
        if miangin_student == "":
            print("shoma esm danesh amooz ro vared nakardid!")
            continue
        miangin_nomarat(miangin_class,miangin_student)
    elif choice == "12":
        print("shoma gozine 12 ro entekhab kardid!")
        name_file = input("lotfan esm file ke mikhahid etelaat madre dar file neveshte shavad ro vared konid: ")
        if name_file == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not name_file.endswith(".json"): 
            file = name_file + ".json"
        else:
            file = name_file
        write_file(file)
    elif choice == "13":
        print("shoam gozine 13 ro entekhab kardid!")
        file_name = input("lotfan esm file ro vared konid: ")
        if file_name == "":
            print("shoma esm file ro vared nakardid!")
            continue
        if not file_name.endswith(".json"):
            file2 =file_name + ".json"
        else:
            file2 = file_name
        show_file(file2)
    elif choice == "14":
        print("shoma gozine 14 ro entekhab kardid!")
        print("az barname kharej shodid bye bye")
        break
    else:
        print("lotfan az gozine 1 ta 14 entekhab konid") 
        continue