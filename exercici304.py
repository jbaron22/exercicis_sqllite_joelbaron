import sqlite3

conexio=sqlite3.connect("bd1.db")
conexio.execute("insert into articles(descripcio,preu) values (?,?)", ("taronjes", 23.50))
conexio.execute("insert into articles(descripcio,preu) values (?,?)", ("peres", 34))
conexio.execute("insert into articles(descripcio,preu) values (?,?)", ("platans", 25))
conexio.commit()
conexio.close()