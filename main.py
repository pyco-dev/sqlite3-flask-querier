from flask import Flask, g, request, render_template
import sqlite3


class DatabaseManager:
    def __init__(self, db: str):
        self.db = db

    def get_db(self) -> sqlite3.Connection:
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(self.db)

        return db


def flaskApp(db: str) -> None:
    app: Flask = Flask(__name__)
    dbManager: DatabaseManager = DatabaseManager(db)

    @app.route('/')
    def index() -> str:
        return render_template("index.html")

    @app.route('/query')
    def query() -> str:
        movieName: str = request.args.get('moviename')
        con: sqlite3.Connection = dbManager.get_db()
        cursor: sqlite3.Cursor = con.cursor()

        movies = cursor.execute("SELECT * FROM movies").fetchall()
        movieList: list[str] = []

        for movie in movies:
            qString = f"SELECT name FROM movies WHERE '{movieName.lower()}' LIKE '%{movie[2].lower()}%'; "
            try:
                query: str = cursor.execute(qString).fetchone()[0]
                movieList.append(query)
            except:
                pass

        con.commit()
        con.close()
        g._database = None

        if len(movieList) > 0:
            return str(movieList)
        else:
            return ""

    app.run()


def main() -> None:
    DATABASE = "./movies.db"
    flaskApp(db=DATABASE)


if __name__ == "__main__":
    main()
