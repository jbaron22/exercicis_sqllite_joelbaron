import sqlite3

conexio=sqlite3.connect("bd1.db")
preu=float(input("Ingresa un preu: "))
cursor=conexio.execute("select descripcio from articles where preu<?", (preu, ))
files=cursor.fetchall()
if len(files)>0:
    for fila in files:
        print(fila)
else:
    print("No existeixen articles amb un preu menor al ingressat5.")
conexio.close()