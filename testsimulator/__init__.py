from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, g
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads, DOCUMENTS

app = Flask(__name__)
app.config.from_object('setting.devconfig')

uploaded_photos = UploadSet('photos', IMAGES)
uploaded_resumes = UploadSet('attachments', DOCUMENTS)

configure_uploads(app, uploaded_photos)
configure_uploads(app, uploaded_resumes)

import testsimulator.view


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()


if __name__ == '__main__':
    app.run()
