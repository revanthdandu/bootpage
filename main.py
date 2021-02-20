from flask import *
import json
import pymysql as Mysql

app = Flask(__name__, static_url_path='',
            static_folder='templates')

mydb = Mysql.connect(host="localhost", user="root", password="root123", database="tester")
mycursor = mydb.cursor()



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/pagetest", methods=['GET', 'POST', 'PUT'])
def pagetest():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email,phone,message)

        mycursor.execute("SELECT * FROM pagetest")
        data = mycursor.fetchall()
        length = len(data)
        cmd = "INSERT INTO `pagetest`(`name`, `email`,`phone`,`message`) VALUES(%s,%s,%s,%s)"
        val = (name, email,phone,message)
        res = mycursor.execute(cmd, val)
        mydb.commit()
        print(res)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)