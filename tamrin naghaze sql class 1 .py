import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3

class maghaze:
    def __init__(self):
        self.new_connection = sqlite3.connect("daftar.db")
        self.new_cursor = self.new_connection.cursor()
        self.new_cursor.execute(
            """CREATE TABLE IF NIT EXISTS moshtary(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                phone INTEGER          
            )"""
        )
        self.new_cursor.execute(
            """CREATE TABLE IF NOT EXISTS kharid(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                moshtary_id INTEGER,
                kala TEXT,
                price INTEGER
            )"""
        )
        self.new_connection.commit()
    def add_moshtary (self,name,phone):
        self.new_cursor.execute("SELECT id FROM moshtary WHERE name = (?) AND phone = (?)",(name,phone))
        row = self.new_cursor.fetchone()
        if  not row:
           self.new_cursor.execute("INSERT INTO moshtary (name,phone) VALUES(?,?) ",(name,phone))
           self.new_connection.commit()
           if self.new_cursor.rowcount > 0:
               print("moshtary sabt shod!")
        else:
            print(f"moshtary : {name} dar list moshtary ha vojod darad!")
            return
        
        




daftar = maghaze()
while True:
    print("="*30)
    print("gozine 1 == ezafe kardan moshtary be list moshtary" \
    "\ngozine 2 == namayesh moshtary ha ba shomare " \
    "\ngozine 3 == namayehs shomare moshtary mored nazar" \
    "\ngozine 4 == ezafe kardan kala " \
    "\ngozine 5 == namayesh kharid moshtary mored nazar" \
    "\ngozine 6 == taghir kala moshtary " \
    "\ngozine 7 == hazf moshtary mored nazar" \
    "\ngozine 8 == exit")
    print("="*30)
    choice = input("lotfan gozine mored nazar khod ro vared konid: ")
    if choice == "":
        print("shoma gozine ie ro entekhab nakardid")
        continue
    if choice == "1":
        print("shoma gozine 1 ro entekhab kardid!")
        moshtary = input("lotfan esm moshtary ro vared konid: ")
        if moshtary == "":
            print("shoma esm moshtary ro vared nakardid!")
            continue
        if not moshtary.isalpha():
            print("lotfan esm moshtary ro be horof vared konid!")
            continue
        phone = input(f"lotfan shomare moshtary : {moshtary} ro vared konid: ")
        if phone == "":
            print("shoma shomare moshtary ro vared nakardid!")
            continue
        if len(phone) != 11:
            print("tedad addad bayad 11 ta bashad!")
            continue
        try:
            shomare = int(phone)
        except ValueError:
            print("lotfan shomare ro be addad vared konid!")
            continue
        daftar.add_moshtary(moshtary,shomare)

        