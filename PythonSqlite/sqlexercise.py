import sqlite3

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Address = request.form['Address']
            City = request.form['City']
            Pin = request.form['Pin']

            if not FirstName or LastName or Address:
                with sqlite3.connect("students.db") as con:
                    cur = con.cursor();
                    cur.execute("INSERT INTO students(FirstName, LastName, Address, City, Pin) values(?,?,?,?)",(FirstName,LastName,Address,City,Pin))
                    con.commit()
                    msg="Record added to db"
                    print(msg)
            else:
                msg ="Error: Insert all fields"
        except:
            con.rollback()
            msg = "error in reading data"
        finally:
            return render_template("results.html", msg=msg)
            con.close()

@app.route('/list')
def list():
    con = sqlite3.connect("students.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    row = cur.fetchall()
    return render_template("list.html", rows=row)


if __name__=='__main__':
    app.run(debug=True)


