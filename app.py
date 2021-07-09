
from flask import Flask,render_template,request

import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method =='POST':
        try:
          roll_no = request.form['roll_no']
          name = request.form['name']
          fname = request.form['fname']
          phone = request.form['phone']
          cinic = request.form['cinic']
          program = request.form ['program']
          session = request.form['session']
          fees = request.form['fees']

          with sql.connect("database.db") as con:

              cur = con.cursor()

              cur.execute("INSERT INTO students (roll_no,name,fname,phone,cinic,program,session,fees) VALUES (?,?,?,?,?,?,?,?)",(roll_no,name,fname,phone,cinic,program,session,fees))

              con.commit()

              msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template('result.html',msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect('database.db')
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("select * from students")

    rows = cur.fetchall()

    return render_template('list.html',rows=rows)


if __name__ == "__main__":
    app.run(debug=True)