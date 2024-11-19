import sqlite3 as sql

# def createDB():

# conn = sql.connect("streamers.db")

# conn.commit()

# conn.close()

def createTable():
    conn =sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE usuarios (
        apellido text,
        nombre text,
        correo text,
        contrasena texto)"""
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #print("hola grupo de ingeniería del software")
    createTable()