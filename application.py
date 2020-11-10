from flask import Flask, render_template
import mysql.connector as mysql
from assets import sql_login

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/birthdays")
def birthdays():
    db = mysql.connect(
    host = sql_login.host,
    user = sql_login.user,
    passwd = sql_login.passwd,
    database = sql_login.database)

    cursor = db.cursor()

    cursor.execute("SELECT \
        name,  \
        /*Days Till Bday*/ IF(DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE())>0, \
                            DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE()), \
                            DATEDIFF(DATE(CONCAT(YEAR(CURDATE())+1, RIGHT(birth, 6))), CURDATE())), \
        /*Years Old*/ TIMESTAMPDIFF(YEAR, birth, CURDATE()) \
        FROM friends \
        ORDER BY \
        /*Days Till Bday*/ IF(DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE())>0, \
                            DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE()), \
                            DATEDIFF(DATE(CONCAT(YEAR(CURDATE())+1, RIGHT(birth, 6))), CURDATE()))")

    DATA = cursor.fetchall()

    return render_template("birthdays.html",people=DATA)

@app.route('/testsite', methods=['GET'])
def testsite():
    return render_template('testsite.html')

