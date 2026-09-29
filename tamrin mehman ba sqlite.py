import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3

new_connection = sqlite3.connect("daftarche.db")
new_cursor = new_connection.cursor()
new_cursor.execute(
    """CREATE TABLE IF NOT EXISTS daftarche(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    vaziyat_mehman TEXT DEFAULT 'nayomade')
"""
)

new_cursor.execute(
    """CREATE TABLE IF NOT EXISTS hadiye(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mehman_id INTEGER,
    kado TEXT)"""
)
new_connection.commit()


def add_mehman (mehman):
    try:
        new_cursor.execute("INSERT INTO daftarche (name) VALUES (?)",(mehman,))
        new_connection.commit()
        print(F"mehman: {mehman} be list mehman ha ezafe shod!")
    except sqlite3.IntegrityError:
        print(f"mehman: {mehman} ghablan dar list mehman ha sabt shode!")
        return

    
def vaziyat_mehman(mehman,vaziyat):
    new_cursor.execute("UPDATE daftarche SET vaziyat_mehman = (?) WHERE name = (?)", (vaziyat,mehman))
    new_connection.commit()
    if new_cursor.rowcount > 0:
        print(f"esm mehman: {mehman} va vaziyat: {vaziyat} dar list mehmna ha sabt shod!")
    else:
        print("mehmani vojod nadarad!")
        return

    
def show_vaziyat (mehman):
    new_cursor.execute("SELECT * FROM daftarche WHERE name = (?)",(mehman,))   
    vaziyat = new_cursor.fetchone()
    shomre,name,hozor = vaziyat
    print(f"{shomre} esm mehman: {name} vaziyat: {hozor}")


def show_mehman():
    new_cursor.execute("SELECT * FROM daftarche")
    row = new_cursor.fetchall()
    for i in row:
        shomare,name,vaziyat = i
        print(f"{shomare} esm mehman: {name} vaziyat: {vaziyat}")


def show_hazerin ():
    new_cursor.execute("SELECT * FROM daftarche WHERE vaziyat_mehman = 'omade' ")
    row = new_cursor.fetchall()
    for i in row:
        shomare,name,hozor = i
        print(f"esm mehman: {name} vaziayt: {hozor}")


def show_ghayebin():
    new_cursor.execute("SELECT * FROM daftarche WHERE vaziyat_mehman = 'nayomade'")
    row = new_cursor.fetchall()
    for i in row:
        shomare,name,hozor = i
        print(f"esm mehman: {name} vaziyat: {hozor}")


def hazf_mehman (mehman):
    new_cursor.execute("DELETE FROM daftarche WHERE name = (?) ",(mehman,))
    new_connection.commit()
    print(f"mehman: {mehman} az list mehman ha hazf shod!")

def show_mehman_alephba_hazer ():
    new_cursor.execute("SELECT name FROM daftarche WHERE vaziyat_mehman = 'omade' ORDER BY name ASC ")
    row = new_cursor.fetchall()
    for i in row:
        print(f"esm mehman: {i}")


def show_mehaman_alephba_nayomde():
    new_cursor.execute("SELECT name FROM daftarche WHERE vaziyat_mehman = 'nayomade' ORDER BY name DESC ")
    row = new_cursor.fetchall()
    for i in row:
        print(f"esm mehman: {i}")


while True:
    print("="*30)
    print("gozine 1 == ezafe kardan mehman " \
    "\ngozine 2 == vaziyat mehman " \
    "\ngozine 3 == mehman omade ya na " \
    "\ngozine 4 == namyesh mehman ha  " \
    "\ngozine 5 == namyesh mehman hayi ke omadan " \
    "\ngozine 6 == namayesh mehman hayi ke nayomadan " \
    "\ngozine 7 == hazf mehman " \
    "\ngozine 8 == namayesh mehman ha ke amade be tartib alefba " \
    "\ngozine 9 == namayesh mehman ha ke nayame be tartib alefba" \
    "\ngozine 10 == sabt hadayae mehman ha" \
    "\ngozine 11 == namayesh hadayae ke mehman ha avordan" \
    "\ngozine 12 == namayesh hadiye yek mehman mored nazar" \
    "\ngozine 13 == exit")
    print("="*30)


    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        mehman = input("lotfan esm mohman khod ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof benevisid!")
            continue
        add_mehman(mehman)


    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani vojod nadarad!")
            continue
        mehman = input("lotfan esm mehman ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof benevisid!")
            continue
        new_cursor.execute("SELECT name FROM daftarche WHERE name = (?)",(mehman,))
        vojod = new_cursor.fetchone()
        if not vojod:
            print(f"mehmani be esm: {mehman} dar list mehman ha vojod nadarad! ")
            continue
        vaziyat = input(f"aya mehman {mehman} omade ya na ba (omade ya nayomade) javab dahid:")
        if vaziyat == "":
            print("shoma aslan elam nakrdid ke mehman omade ya na!")
            continue
        if not vaziyat.isalpha():
            print("lotfan vaziyat mehman ro ba bale ya khayr javab dahid!")
            continue
        if vaziyat == "omade":
            hast = "omade"
        elif vaziyat == "nayomade":
            hast = "nayomade"
        else:
            print("lotfan hozor mehman ro ba (omade ya nayomade) elam konid!")
            continue
        vaziyat_mehman(mehman,hast)


    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani vojod nadarad!")
            continue
        mehman = input("lotfan esm mehman ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof vared konid!")
            continue
        new_cursor.execute("SELECT name FROM daftarche WHERE name = (?)",(mehman,))
        vojod = new_cursor.fetchone()
        if not vojod:
            print(f"mehmani be esm: {mehman} dar list mehman ha vojod nadarad! ")
            continue
        show_vaziyat(mehman)


    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani vojod nadarad!")
            continue
        show_mehman()


    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani dar list mehman ha nis!")
            continue
        show_hazerin()


    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani dar list mehman ha nis!")
            continue
        show_ghayebin()


    elif choice == "7":
        print("shoma gozine 8 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani dar list mehman ha nis!")
            continue
        mehman = input("lotfan esm mehmani ke mikhahid hazf konid ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof vared konid!")
            continue
        new_cursor.execute("SELECT name FROM daftarche WHERE name = (?)",(mehman,))
        vojod = new_cursor.fetchone()
        if not vojod:
            print(f"mehmani be esm: {mehman} dar list mehman ha vojod nadarad! ")
            continue
        hazf_mehman(mehman)


    elif choice == "8":
        print("shoma gozine 8 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani vojod nadard dar list mehman ha!")
            continue
        show_mehman_alephba_hazer()

    elif choice == "9":
        print("shoma gozine 9 ro entekhab kardid!")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani vojod nadard dar list mehman ha!")
            continue
        show_mehaman_alephba_nayomde ()


    elif choice == "10":
        print("shoma gozine 10 ro entekhab kardid! ")
        new_cursor.execute("SELECT COUNT(*) FROM daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmani dar list mehman ha sabt nashode!")
            continue
        mehman = input("lotfan esm mehman ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof vared konid!")
            continue
        new_cursor.execute("SELECT id FROM daftarche WHERE name = (?) AND vaziyat_mehman = 'omade' ",(mehman,))
        natije = new_cursor.fetchone()
        if not natije:
            print("hamchin mehmani vojod nadarad ya hanoz nayomade!!")
            continue
        else:
            mehman_id = natije[0]
            hadiye = input(f"lotfan esm hadiye ke mehman: {mehman} avorde ro vared konid!")
            if hadiye == "":
                print("shoma hadiye ke mehman avorde ro vared nakardid!")
                continue
            if not hadiye.isalpha():
                print("lotfan esm hadiye ro be horof vared konid!")
                continue
            new_cursor.execute("INSERT INTO hadiye (mehman_id,kado) VALUES (?,?)",(mehman_id,hadiye))
            new_connection.commit()
            print("hadiye sabt shod!")


    elif choice == "11":
        print("shoma gozine 11 ro entekhab kardid")
        new_cursor.execute("SELECT daftarche.name , hadiye.kado FROM daftarche JOIN hadiye ON daftarche.id = hadiye.mehman_id")       
        row = new_cursor.fetchall()
        for i in row:
            name,kado = i
            print(f"esm mehman: {name} va kado: {kado} ")

    elif choice == "12":
        print("shoma goIne 12 ro entekhab kardid! ")
        new_cursor.execute("SELECT COUNT(*) from daftarche")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich mehmnai dar list mehman ha vojod nadarad!")
            continue
        new_cursor.execute("SELECT COUNT(*) FROM hadiye")
        vojod = new_cursor.fetchone()[0]
        if not vojod:
            print("hich hadiye ie sabt nashode!")
            continue
        mehman = input("lotfan esm mehman ro vared konid: ")
        if mehman == "":
            print("shoma esm mehman ro vared nakardid!")
            continue
        if not mehman.isalpha():
            print("lotfan esm mehman ro be horof vared konid!")
            continue
        new_cursor.execute("SELECT name FROM daftarche WHERE name = (?)",(mehman,))
        vojod = new_cursor.fetchone()
        if not vojod:
            print(f"mehmani be esm : {mehman} sabt nashode!")
            continue
        new_cursor.execute("SELECT name  FROM daftarche WHERE name = (?) AND vaziyat_mehman = 'omade'  ",(mehman,))
        natije = new_cursor.fetchone()
        if not natije:
            print("mehman mored nazar hanoz nayomade!")
            continue
        new_cursor.execute("SELECT daftarche.name , hadiye.kado FROM daftarche JOIN hadiye ON daftarche.id = hadiye.mehman_id WHERE daftarche.name = (?)",(mehman,))
        rows = new_cursor.fetchall()
        if not rows:
            print(f"mehman : {mehman} kado nayavorde!")
            continue
        for i in rows:
            name,kado = i
            print(f"esm mehman: {name} va kadi ke avorde : {kado}")

    elif choice == "13":
        print("shoma gozine 13 ro entekhab kardid!" \
        "\naz barname kharej shodid bye bye!!")
        break

    else:
        print("lotfan az gozine 1 ta 13 entekhab konid!")
        continue

        