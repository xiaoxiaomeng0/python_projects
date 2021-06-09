from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/guess/<name>')
def home(name):
    parameter = {
        "name": "Luca",
    }
    gender_response = requests.get(url="https://api.genderize.io", params=parameter)
    gender = gender_response.json()["gender"]
    age_response = requests.get(url="https://api.agify.io", params=parameter)
    age = age_response.json()["age"]
    return render_template("index.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = ""
    # create a api request here.

if __name__ == "__main__":
    app.run(debug=True)



