import sqlite3

conexio=sqlite3.connect("bd1.db")
try:
    conexio.execute("""create table articles (
                              codi integer primary key autoincrement,
                              descripcio text,
                              preu real
                        )""")
    print("S'ha creat la taula d'articles")                        
except sqlite3.OperationalError:
    print("La taula d'articles ja existeix")                    
conexio.close()