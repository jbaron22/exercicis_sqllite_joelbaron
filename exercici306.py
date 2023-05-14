import sqlite3

conexio=sqlite3.connect("bd1.db")
codi=int(input("Ingresa el codi d'un' article: "))
cursor=conexio.execute("select descripcio,preu from articles where codi=?", (codi, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existeix un article amb aquest codi.")
conexio.close()