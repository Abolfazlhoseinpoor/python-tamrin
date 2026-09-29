import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sqlite3
conect = sqlite3.connect("show.db")
cusor = conect.cursor()
cusor.execute(
    """CREATE TABLE IF NOT EXISTS PRODUCTS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    quantity INTEGER)"""
)
conect.commit()
cusor.execute("INSERT INTO PRODUCTS (name,price,quantity) VALUES (?,?,?)",("shalvar",150000,5))
cusor.execute("INSERT INTO PRODUCTS (name,price,quantity) VALUES (?,?,?)",("pirahan",200000,10))
cusor.execute("INSERT INTO PRODUCTS (name,price,quantity) VALUES (?,?,?)",("katan",850000,0))
cusor.execute("INSERT INTO PRODUCTS (name,price,quantity) VALUES (?,?,?)",("t_shirt",490000,18))
conect.commit()
print("jadval sakhte shod va mahsol ezafe shod!")

conect.execute("UPDATE PRODUCTS SET quantity = 0 WHERE name = 'shalvar' ")
conect.commit()

conect.execute("DELETE FROM PRODUCTS WHERE name = 'katan' ")
conect.commit()


cusor.execute("SELECT * FROM PRODUCTS WHERE name = 'satan' ")
radif = cusor.fetchone()
if radif is None:
    print("kala peyda nashod!")
else:
    product_id,name,price,quantity = radif
    print(f"shomare: {product_id} esm jens: {name} gheymat: {price} tedad: {quantity}")