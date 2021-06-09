from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/URL/<int:number>")
def guess_number(number):
    guessed = random.randint(0, 9)
    if guessed > number:
        return "<h1 style='color: red'>Too low, try again!</h1><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if guessed < number:
        return "<h1 style='color: blue'>Too high, try again!</h1><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if guessed == number:
        return "<h1>You are right!</h1><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
