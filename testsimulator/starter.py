from __future__ import with_statement
from contextlib import closing
import sqlite3
from testsimulator import app


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    db = connect_db()
    cur = db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


def main():
    cur = query_db('select * from candidates')
    for rec in cur:
        for k, v in rec:
            print k, v


if __name__ == '__main__': main()
