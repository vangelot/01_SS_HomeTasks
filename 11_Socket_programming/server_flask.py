from flask import Flask, render_template, redirect, url_for, request
import string

app = Flask(__name__)

dict_of_answers = {'weather': "the weather is fine",
                   'exit': 'try to use Alt+F4 or Ctrl+w',
                   0: 'use: "weather", "exit" for bot\n  ' \
                   'and any other to count words'
                   }


def count_words(word):
    words_amount = 0
    counter = 0
    while counter < len(word):
        if word[counter] in string.ascii_letters:
            words_amount += 1
            counter += 1
            while (counter < len(word)) and (word[counter] in string.ascii_letters):
                counter += 1
            continue
        counter += 1
    return words_amount


@app.route("/")
@app.route('/home')
def home():

    return render_template("index.html", message2=dict_of_answers[0])


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/go_to_home', methods=['POST'])
def go_to_home():
    # Делаем перенаправление на другую страницу
    return redirect(url_for('home'))


@app.route('/submit_request', methods=['POST'])
def submit_request():
    if request.form['request'] in dict_of_answers.keys():
        message = dict_of_answers[request.form['request']]
    else:
        message = 'word amount = ' + str(count_words(request.form['request'])) + " :IN: " + request.form['request']
    return render_template('index.html', message=message, message2=dict_of_answers[0])


@app.route('/go_to_about', methods=['POST'])
def go_to_about():
    # Делаем перенаправление на другую страницу
    return redirect(url_for('about'))

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True)

