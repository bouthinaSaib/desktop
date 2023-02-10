import sqlite3
def AddToDb(name1, price1, unit1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists items(name TEXT PRIMARY KEY , price INT, unit TEXT)")
    cursor.execute("insert into items(name,price,unit) values(?, ?, ?)",(name1, price1, unit1))
    conn.commit()
    print("data inserted")
def getby(unit1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists items(name TEXT PRIMARY KEY , price INT, unit TEXT)")
    name= cursor.execute("Select name from items where unit=?",(unit1,))
    print(*name)
def deleteby(name1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists items(name TEXT PRIMARY KEY , price INT, unit TEXT)")
    cursor.execute("DELETE FROM items WHERE name=?",(name1,))
    conn.commit()
def updateitem(name1,price1,unit1 ):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists items(name TEXT PRIMARY KEY , price INT, unit TEXT)")
    cursor.execute("UPDATE items  SET price=?, unit=? WHERE name=? ",(price1, unit1,name1) )
    conn.commit()
def table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("create table if not exists items(name TEXT PRIMARY KEY , price INT, unit TEXT)")
    cursor.execute("select * From items")
    rows = cursor.fetchall()
    return rows
def getbyunit(unit1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("select name from items where unit=?",(unit1,))
    out=[]
    for item in cursor.fetchall():
        out.append(item[0])
    return out
def getbyname(name1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    price=cursor.execute("select price from items where name=?", (name1,))
    return str(cursor.fetchone()[0])


