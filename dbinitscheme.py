import sqlite3
import os

def main() -> None:
    if os.path.isfile("./movies.db"):
        os.remove("./movies.db")

    con: sqlite3.Connection = sqlite3.connect('movies.db')
    cur: sqlite3.Cursor = con.cursor()

    cur.execute("CREATE TABLE movies(id, name, pattern)")
    cur.execute("INSERT INTO movies(id,name, pattern) VALUES (1, 'Interstellar', 'Inter')")

    con.commit()
    con.close()


if __name__ == '__main__':
    main()