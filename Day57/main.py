from flask import Flask, render_template
import requests

app = Flask(__name__)

post_url = "https://api.npoint.io/4af156202f984d3464c3"
response = requests.get(url=post_url)
post_list = response.json()

@app.route('/')
def home():
    return render_template("index2.html", post_list=post_list)

@app.route("/url/post/<int:blog_id>")
def view_blog(blog_id):
    print(type(blog_id))
    print(type(post_list[0]["id"]))
    return render_template("post.html", post_id=blog_id, post_list=post_list)

if __name__ == "__main__":
    app.run(debug=True)
