import sqlite3

conexio=sqlite3.connect("bd1.db")
cursor=conexio.execute("select codi,descripcio,preu from articles")
for fila in cursor:
    print(fila)
conexio.close()