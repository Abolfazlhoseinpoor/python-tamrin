import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3


class Maghaze:

    def __init__(self):
        self.connection = sqlite3.connect("maghaze.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS moshtary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            phone INTEGER)"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS kharid(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moshtary_id INTEGER,
            kala TEXT,
            price INTEGER )"""
        )
        self.connection.commit()

    def add_moshtary(self, name, phone):
        try:
            self.cursor.execute("INSERT INTO moshtary (name,phone) VALUES (?,?)", (name, phone))
            self.connection.commit()
            print(f"moshtary: {name} be list moshtary ha ezafe shod!")
        except sqlite3.IntegrityError:
            print(f"moshtary: {name} ghablan sabt shode!")
            return

    def sabt_jens(self, name):
        self.cursor.execute("SELECT id FROM moshtary WHERE name = (?)", (name,))
        vojod = self.cursor.fetchone()
        if not vojod:
            print("hamchin moshtary sabt nashode!")
            return
        else:
            moshtary_id = vojod[0]
        tedad = input(f"moshtary : {name} chnd ta kala bardashte?")
        if tedad == "":
            print("shoma moshakhas nakardid ke mishtary chnt ta kala bardashte !")
            return
        try:
            tedad_kala = int(tedad)
        except ValueError:
            print("lotfan tedad kala ke moshtary bardashte ro be addad vared konid!")
            return
        for i in range(tedad_kala):
            kala = input("lotfan esm kala ro vared konid: ")
            if kala == "":
                print("shoma kala ke moshtary bardashte ro vared nakardid!")
                continue
            if not kala.isalpha():
                print("lotfan esm kala ro be horof vared konid!")
                continue
            price = input(f"lotfan mablagh : {kala} ro vared konid: ")
            if price == "":
                print("shoma mablagh kala ro vared nakardid!")
                continue
            try:
                price_kala = int(price)
            except ValueError:
                print("lotfan mablagh kala ro be addad vared konid!")
                continue
            self.cursor.execute(
                "INSERT INTO kharid (moshtary_id,kala,price) VALUES (?,?,?)",
                (moshtary_id, kala, price_kala),
            )
            self.connection.commit()
        print(f"kala haye moshtary : {name} sabt shod!")

    def show_moshtary(self):
        self.cursor.execute("SELECT name,phone FROM moshtary")
        row = self.cursor.fetchall()
        for i in row:
            name, phone = i
            print(f"esm moshtary: {name} shomare telephone: {phone}")

    def show_kala_moshtary(self):
        self.cursor.execute(
            "SELECT moshtary.name,kharid.kala, kharid.price FROM moshtary JOIN kharid ON moshtary.id = kharid.moshtary_id"
        )
        row = self.cursor.fetchall()
        for i in row:
            name, kala, price = i
            print(f"esm moshtary: {name} va esm kala: {kala} va gheymat: {price}")

    def show_number_moshtary(self, name):
        self.cursor.execute("SELECT phone FROM moshtary WHERE name = (?)", (name,))
        row = self.cursor.fetchone()
        if not row:
            print(f"moshtary : {name} dar list moshtary ha vojod nadarad!")
            return
        print(f"esm moshtary: {name} shomare: {row}")

    def show_kala(self, name):
        self.cursor.execute("SELECT name FROM moshtary WHERE name = (?)", (name,))
        row = self.cursor.fetchone()
        if not row:
            print(f"moshtary be esm: {name} vojod nadarad!")
            return
        self.cursor.execute(
            "SELECT moshtary.name , kharid.kala, kharid.price FROM moshtary JOIN kharid ON moshtary.id = kharid.moshtary_id WHERE moshtary.name = (?) ",
            (name,),
        )
        row = self.cursor.fetchall()
        jam = []
        for i in row:
            esm, kala, price = i
            jam.append(price)
            total = sum(jam)
        print(f"esm moshtary: {esm} kala : {kala} va gheymat: {price} va jam kol ghyemat: {total}")

    def show_number(self):
        self.cursor.execute("SELECT name , phone FROM moshtary")
        row = self.cursor.fetchall()
        for i in row:
            name, phone = i
            print(f"esm moshtary: {name} va shomare: {phone}")

    def hazf_moshtary(self, name):
        self.cursor.execute("SELECT id FROM moshtary WHERE name = (?)", (name,))
        row = self.cursor.fetchone()
        if row:
            moshtary_id = row[0]
            self.cursor.execute("DELETE FROM kharid WHERE moshtary_id = (?)", (moshtary_id,))
            self.cursor.execute("DELETE FROM moshtary WHERE id = (?)", (moshtary_id,))
            self.connection.commit()
            print(f"moshtary : {name} az list moshtary ha hazf shod!")

    def count_moshtary(self):
        self.cursor.execute("SELECT COUNT(*) FROM moshtary")
        return self.cursor.fetchone()[0]

    def count_kharid(self):
        self.cursor.execute("SELECT COUNT(*) FROM kharid")
        return self.cursor.fetchone()[0]


maghaze = Maghaze()

while True:
    print("=" * 30)
    print("gozine 1 == ezafe kardan moshtari va shomare telephone" \
    "\ngozine 2 == sabt jens moshtary " \
    "\ngozine 3 == namayesh moshtary be telephone" \
    "\ngozine 4 == namayesh jens moshtary " \
    "\ngozine 5 == namayesh shomare moshtary mored nazar " \
    "\ngozine 6 == namayesh kala moshtary mored nazar" \
    "\ngozine 7 == namayesh shomare tamam moshtary" \
    "\ngozine 8 == hazf moshtary" \
    "\ngozine 9 == exit")
    print("=" * 30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue

    if choice == "1":
        print("shoam gozine 1 ro entekhab kardid!")
        moshtary = input("lotfan esm moshtary ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshtary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        phone = input(f"lotfan shomare moshtary: {moshtary} ro vared konid:")
        if phone == "":
            print(f"shoma shomare telephone moshtary: {moshtary} ro vared nakardid! ")
            continue
        if not phone.isalnum():
            print("lotfan shomare telephone moshtary ro be addad vared konid!")
            continue
        if not len(phone) == 11:
            print("lotfan tedad addad shomare bayad 11 ragham bashad!")
            continue
        maghaze.add_moshtary(moshtary, phone)

    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary ha khali ast!")
            continue
        moshtary = input("lotfan esm moshtary ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshtary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        maghaze.sabt_jens(moshtary)

    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary ha khali ast!")
            continue
        maghaze.show_moshtary()

    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary khali ast!")
            continue
        if not maghaze.count_kharid():
            print("list kala ha khali ast!")
            continue
        maghaze.show_kala_moshtary()

    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary ha khali ast!")
            continue
        moshtary = input("lotfan esm moshtary ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshtary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        maghaze.show_number_moshtary(moshtary)

    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary ha khali ast!")
            continue
        if not maghaze.count_kharid():
            print("list kala ha khali ast!")
            continue
        moshtary = input("lotfan esm moshtary mored nazar khod ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        maghaze.show_kala(moshtary)

    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary khali ast!")
            continue
        maghaze.show_number()

    elif choice == "8":
        print("shoma goizine 8 ro entekhab kardid!")
        if not maghaze.count_moshtary():
            print("list moshtary khali ast!")
            continue
        moshtary = input("lotfan esm moshtary ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshtary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        maghaze.cursor.execute("SELECT name FROM moshtary WHERE name = (?) ", (moshtary,))
        vojod = maghaze.cursor.fetchone()
        if not vojod:
            print(f"moshtary be esm : {moshtary} vojod nadarad!")
            continue
        maghaze.hazf_moshtary(moshtary)

    elif choice == "9":
        print("shoma gozine 9 ro netkehab kardid!" \
        "\naz barname kharej shodid bye bye!!!")
        break

    else:
        print("lotfan az gozine 1 ta 9 entekhab konid!")
        continue