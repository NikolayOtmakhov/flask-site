from flask import Flask, render_template, request
from assets import sql_login
from logic import sql_functions
import requests

Running_local = False

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
    DATA = sql_functions.birthday_data(sql_login,Running_local)
    return render_template("birthdays.html",people=DATA)

@app.route('/stocks', methods=['GET','POST'])
def stocks():
    return render_template('stocks.html')

@app.route('/stockshow', methods=['GET','POST'])
def stocksshow():
    return render_template('stockinfo.html', stock_ticker = request.args.get("stock_ticker", "world"))

def tester():
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token 33fa689353e4b7f1deec77ae17eeda1dbb432df6'
    }
    url = "https://api.tiingo.com/tiingo/daily/aapl"
    try:
        response = requests.get(url, headers=headers)
        return "passed"
    except:
        return "failed"


@app.route('/testsite' , methods=['GET','POST'])
def testsite():
    stock_ticker = tester()
    return render_template('stockinfo.html',stock_ticker=stock_ticker)

if __name__ == '__main__':
    Running_local = True
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)