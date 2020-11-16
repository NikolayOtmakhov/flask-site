from flask import Flask, render_template, request
from assets import sql_login
import magic

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

    DATA = birthday_data(sql_login)

    return render_template("birthdays.html",people=DATA)

@app.route('/stocks', methods=['GET','POST'])
def stocks():
    return render_template('stocks.html')

@app.route('/stockshow', methods=['GET','POST'])
def stocksshow():
  return render_template('stockinfo.html', stock_ticker=request.args.get("stock_ticker", "world"))


@app.route('/testsite' , methods=['GET','POST'])
def testsite():
    return render_template('testsite.html')

