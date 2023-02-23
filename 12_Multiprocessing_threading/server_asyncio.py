import time

from flask import Flask, render_template, redirect, url_for, request
import asyncio

app = Flask(__name__)


mes1 = ''
mes2 = ''
mes3 = ''


async def plus(a, b):
    await asyncio.sleep(5)
    global mes1
    try:
        mes1 = str(int(a) + int(b))
    except:
        mes1='error'
    print("plus")
    # return None


async def minus(a, b):
    await asyncio.sleep(0)
    global mes2
    try:
        mes2 = str(int(a) - int(b))
    except:
        mes2='error'
    print("minus")
    # return None


async def multiply(a, b):
    await asyncio.sleep(7)
    global mes3
    try:
        mes3 = str(int(a) * int(b))
    except:
        mes3='error'
    print("multiply")
    # return None


@app.route("/")
@app.route('/home')
def home():
    return render_template("index.html", message2="hello world")


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


@app.route('/submit_plus', methods=['POST'])
async def submit_plus():
    val1 = request.form['num1']
    val2 = request.form['num2']
    # await plus(val1, val2)
    if "plus-button" in request.form:
        print("yoyo")
        await plus(val1, val2)
    if "minus-button" in request.form:
        await minus(val1, val2)
    if "multiply-button" in request.form:
        await multiply(val1, val2)
        print("11 multy 11")
    await asyncio.sleep(3)
    return render_template('index.html', message1=mes1,message2=mes2, message3=mes3, val1=val1, val2=val2)

if __name__ == "__main__":
    app.run(debug=True)