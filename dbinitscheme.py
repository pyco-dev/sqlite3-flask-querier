import sqlite3
import os

def main() -> None:
    if os.path.isfile("./movies.db"):
        os.remove("./movies.db")

    con: sqlite3.Connection = sqlite3.connect('movies.db')
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("CREATE TABLE movies(id, name, pattern)")
    cur.execute("INSERT INTO movies(id,name,pattern) VALUES (1, 'Interstellar', 'Inter')")
    cur.execute("INSERT INTO movies(id,name,pattern) VALUES (2, 'Jurrassic Park', 'Jurr')")
    cur.execute("INSERT INTO movies(id,name,pattern) VALUES (3, 'Jurrassic Park 2', 'Jurr')")
    cur.execute("INSERT INTO movies(id,name,pattern) VALUES (4, 'Jurrassic Park 3', 'Jurr')")

    con.commit()
    con.close()


if __name__ == '__main__':
    main()
