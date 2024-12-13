from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def db_connection():
    connection = sqlite3.connect("mydatabase.db")
    return connection

@app.route("/persons")
def persons():
    conn = db_connection()
    people = conn.execute("SELECT * FROM People;").fetchall()
    conn.close()
    return render_template("persons.html", people=people)

@app.route("/createPerson", methods=["GET", "POST"])
def create_person():
    if request.method == "GET":
        return render_template("create_person.html")
    else:
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        age = request.form["age"]
        conn = db_connection()
        conn.execute(f"""
           INSERT INTO People (FirstName, LastName, Age)
           VALUES ("{first_name}", "{last_name}", {age});
        """)
        conn.commit()
        conn.close()
        return redirect("/persons")
    
app.run(debug = True)