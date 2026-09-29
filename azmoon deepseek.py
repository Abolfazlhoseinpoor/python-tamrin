import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3
import datetime


class ketabkhane:
    def __init__(self):
        self.new_coonection = sqlite3.connect("ketab.db")
        self.new_cursor = self.new_coonection.cursor()
        self.new_cursor.execute(
            """CREATE TABLE IF NOT EXISTS ketabkhane(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            esm_ketab TEXT,
            nevisande TEXT,
            enteshar TEXT
            )"""
        )
        self.new_cursor.execute(
            """CREATE TABLE IF NOT EXISTS ozv(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            esm_ozv TEXT,
            email TEXT)"""
        )
        self.new_cursor.execute(
        """CREATE TABLE IF NOT EXISTS vaziyat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ketab_id INTEGER,
        ozv_id TEXT,
        vaziyat_ketab TEXT,
        tarikh TEXT)""")
        self.new_coonection.commit()


    def afzodan_ketab (self,name,nevisande,sal_enteshar):
        self.new_cursor.execute("INSERT INTO ketabkhane (esm_ketab,nevisande,enteshar) VALUES (?,?,?)",(name,nevisande,sal_enteshar))
        self.new_coonection.commit()
        print("ketab ba nevisande va sal enteshar sabt shod!")



    def afzodan_ozv(self,name,email):
        self.new_cursor.execute("INSERT INTO ozv (esm_ozv,email) VALUES (?,?)",(name,email))
        self.new_coonection.commit()
        print(f"ozv : {name} sabt shod!")


    def amanat_gereftan (self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        self.new_cursor.execute("SELECT COUNT(*) FROM ozv")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ozvi sabt nashode")
            return
        ozv = input("lotfan esm ozv ro vared konid: ")
        if ozv == "":
            print("shoma esm ozv vared nakardid!")
            return
        if not ozv.isalpha():
            print("lotfan esm ozv ro be horof vared konid!")
            return
        self.new_cursor.execute("SELECT id FROM ozv WHERE esm_ozv = (?)",(ozv,))
        vojod = self.new_cursor.fetchone()
        if not vojod:
            print("hamvhin ozvi vojod nadarad!")
            return
        vojod = vojod[0]
        tedad = input(f"{ozv} chnd ta ketba mikhahad amant begirad: ")
        if tedad == "":
            print("shoma tedad ro moshakhas nakardid!")
            return
        try: 
            tedad_amanat = int(tedad)
        except ValueError:
            print("lotfan tedad ketba baraye amanat ro be addad vared konid!")
            return
        for i in range(tedad_amanat):
            esm_ketab = input(f"lotfan esm ketabi ke {ozv} mikhahad amant begirad ro vared konid: ")
            if esm_ketab == "":
                print("shoma esm ketab ro vared nakardid!")
                return
            if not esm_ketab.isalpha():
                print("lotfan esm ketab ro be horof vared konid!")
                return
            self.new_cursor.execute("SELECT id FROM ketabkhane WHERE esm_ketab = (?)",(esm_ketab,))
            row = self.new_cursor.fetchone()
            if not row:
                print("hamchin ketabi dar ketab khane sabt nashode va vojod nadarad!")
                return
            row = row[0]
            hala = datetime.datetime.now()
            zaman = hala.strftime("%Y - %m - %d %H:%M:%S")
            self.new_cursor.execute("INSERT INTO vaziyat (ketab_id,ozv_id,tarikh) VALUES(?,?,?) ",(row,vojod,zaman))
            self.new_cursor.execute("UPDATE vaziyat SET vaziyat_ketab = (?) WHERE ketab_id = (?) AND ozv_id = (?)",("AMANAT GEREFTE SHOD",row,vojod))
            self.new_coonection.commit()
        print("ketab amanat dade shode")


    def pass_gereftan(self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        self.new_cursor.execute("SELECT COUNT(*) FROM ozv")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ozvi sabt nashode")
            return
        ozv = input("lotfan esm ozv ro vared konid: ")
        if ozv == "":
            print("shoma esm ozv vared nakardid!")
            return
        if not ozv.isalpha():
            print("lotfan esm ozv ro be horof vared konid!")
            return
        self.new_cursor.execute("SELECT id FROM ozv WHERE esm_ozv = (?)",(ozv,))
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hamvhin ozvi vojod nadarad!")
            return
        tedad = input(f"{ozv} chnd ta ketba mikhahad bargardanad?: ")
        if tedad == "":
            print("shoma tedad ro moshakhas nakardid!")
            return
        try: 
            tedad_amanat = int(tedad)
        except ValueError:
            print("lotfan tedad ketab ke mikhahad bargardanad  ro be addad vared konid!")
            return
        for i in range(tedad_amanat):
            esm_ketab = input(f"lotfan esm ketabi ke {ozv} mikhahad  ro vared konid: ")
            if esm_ketab == "":
                print("shoma esm ketab ro vared nakardid!")
                return
            if not esm_ketab.isalpha():
                print("lotfan esm ketab ro be horof vared konid!")
                return
            self.new_cursor.execute("SELECT id FROM ketabkhane WHERE esm_ketab = (?)",(esm_ketab,))
            row = self.new_cursor.fetchone()[0]
            if not row:
                print("hamchin ketabi dar ketab khane sabt nashode va vojod nadarad!")
                return
            hala = datetime.datetime.now()
            zaman = hala.strftime("%Y - %m - %d %H:%M%S")
            self.new_cursor.execute("UPDATE vaziyat SET vaziyat_ketab = (?) WHERE ketab_id = (?) AND ozv_id = (?)",("pass gerefte shod",row,vojod))
            self.new_coonection.commit()
        print("ketab pass gerefte shod ")


    def namayesh_ketabha(self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        self.new_cursor.execute("SELECT * from ketabkhane")
        vojod = self.new_cursor.fetchall()
        for i,book in enumerate (vojod,start=1):
            ketab_id , esm_ketab , nevisande , sal_enteshar = book
            print(f"{i} ===> id ketab: {ketab_id} ===> esm ketab : {esm_ketab} ===> nevisande ketab : {nevisande} ===> sal enteshar ===> {sal_enteshar}")


    def namayesh_ketab_amanat (self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        self.new_cursor.execute("SELECT COUNT(*) FROM ozv")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ozvi sabt nashode")
            return
        self.new_cursor.execute(
            """SELECT ketabkhane.esm_ketab,ozv.esm_ozv,vaziyat.vaziyat_ketab FROM vaziyat
            JOIN ketabkhane ON vaziyat.ketab_id = ketabkhane.id
            JOIN ozv ON vaziyat.ozv_id = ozv.id
            WHERE vaziyat.vaziyat_ketab = "AMANAT GEREFTE SHOD" """
        )
        row = self.new_cursor.fetchall()
        if not row:
            print("hich kala pass dade nashode!")
            return
        for esm_ketab , esm_ozv , vaziyat in row:
            print(f"{esm_ketab} {esm_ozv} {vaziyat}")

    def namayesh_ketab_pass_gerefte(self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        self.new_cursor.execute("SELECT COUNT(*) FROM ozv")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ozvi sabt nashode")
            return
        self.new_cursor.execute(
            """SELECT ketabkhane.esm_ketab,ozv.esm_ozv,vaziyat.vaziyat_ketab FROM vaziyat
            JOIN ketabkhane ON vaziyat.ketab_id = ketabkhane.id
            JOIN ozv ON vaziyat.ozv_id = ozv.id
            WHERE vaziyat.vaziyat_ketab = "pass gerefte shod" """
        )
        row = self.new_cursor.fetchall()
        if not row:
            print("hich kala pass dade nashode!")
            return
        for esm_ketab , esm_ozv , vaziyat in row:
            print(f"{esm_ketab} {esm_ozv} {vaziyat}")


    def hazf_ketab(self):
        self.new_cursor.execute("SELECT COUNT(*) FROM ketabkhane")
        vojod = self.new_cursor.fetchone()[0]
        if not vojod:
            print("hich ketabi sabt nashode!")
            return
        esm_ketab = input("lotfan esm ketab ro vared konid: ")
        if esm_ketab == "":
            print("shoma esm ketab ro vared nakardid!")
            return
        self.new_cursor.execute("SELECT esm_ketab FROM ketabkhane WHERE esm_ketab = (?)" , (esm_ketab,))
        vojod = self.new_cursor.fetchone()[0]
        if not vojod :
            print("hamchin esmi vojod nadarad!")
            return
        self.new_cursor.execute("DELETE  FROM ketabkhane WHERE esm_ketab = (?)",(esm_ketab,))
        self.new_coonection.commit()
        print("ketab mored nazar hazf shod!")







ketab = ketabkhane()
while True:
    print("="*30)
    print("gozine 1 == afzodan ketab " \
    "\ngozine 2 == afzodan ozv" \
    "\ngozine 3 == amanat gereftan ketab" \
    "\ngozine 4 == pass dadan ketab" \
    "\ngozine 5 == namayesh list ketab ha" \
    "\ngozine 6 == namayesh ketab haye amanat dade shode" \
    "\ngozine 7 == namayesh ketab haye amant gerefte shode" \
    "\ngozine 8 == hazf ketab" \
    "\ngozine 9 == exit")
    print("="*30)

    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid!")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        name = input("lotfan esm ketab ro vared konid: ")
        if name == "":
            print("shoma esm ketab ro vared nakardid")
            continue
        if not name.isalpha():
            print("lotfan esm ketab ro be horof vared konid!")
            continue
        nevisande = input("lotfan esm nevisande ketab ro vared konid: ")
        if nevisande == "":
            print("shoma ems nevisande ketab ro vared nakardid!")
            continue
        if not nevisande.isalpha():
            print("lotfan esm nevisande ro be horof vared konid!")
            continue
        enteshar = input(f"lotfan sal enteshar ketab: {name} ro vared konid: ")
        if enteshar == "":
            print("shoma sal enteshar ketab ro vared nakardid!")
            continue
        if not enteshar.isalnum():
            print("lotfan sal enteshar ro be addad vared konid!")
            continue
        if not len(enteshar) == 4:
            print("tool enteshar bayad 4 ta bashad masalan: 1399")
            continue
        ketab.afzodan_ketab(name,nevisande,enteshar)
    elif choice == "2":
        print("shoma gozine 2 ro entekhab kardid!")
        ozv = input("lotfan esm ozv jadid ro vared konid: ")
        if ozv == "":
            print("shoma esm ozv jadid ro vared nakardid!")
            continue
        if not ozv.isalpha():
            print("lotfan esm esm jadid ro be horof vared konid!")
            continue
        email = input(f"lotafn email : {ozv} ro vared konid: ").lower().strip()
        if email == "":
            print("shoma email ro vared nakardid!")
            continue
        if not email.endswith("@gmail.com"):
            print("shoma @gmail.com ro vare nakardid!")
            continue
        ketab.afzodan_ozv(ozv,email)
    elif choice == "3":
        print("shoma gozine 3 ro entekhab kardid!")
        ketab.amanat_gereftan()
    elif choice == "4":
        print("shoma gozine 4 ro entekhab kardid!")
        ketab.pass_gereftan()
    elif choice == "5":
        print("shoma gozine 5 ro entekhab kardid!")
        ketab.namayesh_ketabha()
    elif choice == "6":
        print("shoma gozine 6 ro entekhab kardid!")
        ketab.namayesh_ketab_amanat()
    elif choice == "7":
        print("shoma gozine 7 ro entekhab kardid!")
        ketab.namayesh_ketab_pass_gerefte()
    elif choice == "8":
        print("shoma gozine 8 ro entekhab kardid!")
        ketab.hazf_ketab()
    elif choice == "9":
        print("shoma gozine 9 ro entekhab kardid " \
        "\naz barname kharej shodid bye bye")
        break
    else:
        print("lotfan az gozine 1 ta 9 entekhab konid!")
        continue
    