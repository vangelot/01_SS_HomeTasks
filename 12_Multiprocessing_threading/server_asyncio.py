from flask import Flask, render_template, redirect, url_for, request
import asyncio

app = Flask(__name__)


mes1 = 'a'
mes2 = 'b'
mes3 = 'c'


async def plus(a, b):
    await asyncio.sleep(1)
    global mes1
    mes1 = str(a + b)
    # return None


async def minus(a, b):
    await asyncio.sleep(1)
    global mes2
    mes2 = str(a - b)
    # return None


async def multy(a, b):
    await asyncio.sleep(2)
    global mes3
    mes3 = str(a * b)
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


@app.route('/submit_request', methods=['POST'])
def submit_request():

    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(plus(request.form['num1'], request.form['num2'])),
             ioloop.create_task(minus(request.form['num1'], request.form['num2'])),
             ioloop.create_task(multy(request.form['num1'], request.form['num2']))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
    return render_template('index.html', message2=mes1 + mes2 + mes3)


if __name__ == "__main__":
    # ioloop = asyncio.get_event_loop()
    # tasks = [ioloop.create_task(plus(1, 2)),
    #          ioloop.create_task(minus(1, 2)),
    #          ioloop.create_task(multy(1, 2))]
    # wait_tasks = asyncio.wait(tasks)
    # ioloop.run_until_complete(wait_tasks)
    # print(mes1, mes2, mes3)
    # ioloop.close()

    app.run(debug=True)