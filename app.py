from flask import Flask, request
import sqlite3
app = Flask(__name__)


@app.route("/hello/")
def hello():
    if 'name' in request.args:
        name = request.args['name']
        db = sqlite3.connect('mydb')
        cursor = db.cursor()
        cursor.execute('INSERT INTO users(name) VALUES(?)', (name,))
        db.commit()
        db.close()
        return "Hello " + name + "!"
    else:
        return "Hello Stranger!"


def create_db():
    db = sqlite3.connect('mydb')
    cursor = db.cursor()
    try:
        cursor.execute('CREATE TABLE users(name TEXT)')
        db.commit()
    except:
        print "table exists. skipping."
    db.close()


if __name__ == '__main__':
    create_db()
    app.run(debug=True)
