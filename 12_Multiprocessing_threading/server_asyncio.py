import time

from flask import Flask, render_template, redirect, url_for, request
import asyncio

app = Flask(__name__)


mes1 = ''
mes2 = ''
mes3 = ''


async def plus(a, b):
    global mes1
    try:
        mes1 = str(int(a) + int(b))
        await asyncio.sleep(0)
        print("plus")
    except:
        mes1='error'
    # return None


async def minus(a, b):
    global mes2
    try:
        mes2 = str(int(a) - int(b))
        await asyncio.sleep(4)
        print("minus")
    except:
        mes2='error'
    # return None


async def multiply(a, b):
    global mes3
    try:
        mes3 = str(int(a) * int(b))
        await asyncio.sleep(10)
        print("multiply")
    except:
        mes3='error'
    # return None


@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/go_to_about', methods=['POST'])
def go_to_about():
    return redirect(url_for('about'))


@app.route('/go_to_home', methods=['POST'])
def go_to_home():
    # Делаем перенаправление на другую страницу
    return redirect(url_for('home'))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/submit', methods=['POST'])
async def submit():
    val1 = request.form['num1']
    val2 = request.form['num2']
    # await plus(val1, val2)
    if "plus-button" in request.form:
        print("we are in submit: plus")
        await plus(val1, val2)
    if "minus-button" in request.form:
        print("we are in submit: minus")
        await minus(val1, val2)
    if "multiply-button" in request.form:
        print("we are in submit: multiply")
        await multiply(val1, val2)
    # await asyncio.sleep(1)
    return render_template('index.html', message1=mes1, message2=mes2, message3=mes3, val1=val1, val2=val2)

if __name__ == "__main__":
    app.run(debug=True)