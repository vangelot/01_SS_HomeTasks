from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Обрабатываем данные из формы
    username = request.form['username']
    password = request.form['password']

    # Делаем что-то с данными (например, сохраняем их в базу данных)

    # Делаем перенаправление на другую страницу
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Данные успешно отправлены'
