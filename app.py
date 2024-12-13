from flask import Flask, render_template, request, redirect
from contextlib import contextmanager
import sqlite3

app = Flask(__name__)

@contextmanager
def db_connection():
    connection = sqlite3.connect("mydatabase.db")
    try:
        yield connection
    finally:
        connection.close()

@app.route("/persons")
def persons():
    with db_connection() as conn:
        people = conn.execute("SELECT * FROM People;").fetchall()
    return render_template("persons.html", people=people)

@app.route("/createPerson", methods=["GET", "POST"])
def create_person():
    if request.method == "GET":
        return render_template("create_person.html")
    else:
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        age = request.form["age"]
        with db_connection() as conn:
            conn.execute("""
                INSERT INTO People (FirstName, LastName, Age)
                VALUES (?, ?, ?);
            """, (first_name, last_name, age))
            conn.commit()
        return redirect("/persons")