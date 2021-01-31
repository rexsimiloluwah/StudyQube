from flask import Flask, render_template
from datetime import datetime 

app = Flask(__name__)

posts = [
    {
        "title" : "Building a URL Shortener with FastAPI and MongoDB",
        "category" : "FastAPI",
        "url" : "https://simiokunowo.hashnode.dev/build-a-url-shortener-with-fastapi-mongodb-and-python",
        "date" : str(datetime.now()).split(" ")[0]
    },

    {
        "title" : "Building a Plant disease classification Web-app with Tensorflow.js and Python",
        "category" : "Machine learning",
        "url" : "https://rexsimiloluwa.medium.com/building-a-plant-disease-classification-web-app-in-keras-and-tensorflow-js-d435829213fa",
        "date" : str(datetime.now()).split(" ")[0]
    },

    {
        "title" : "Extracting real-time data from NCDC Website",
        "category" : "Web scraping",
        "url" : "https://rexsimiloluwa.medium.com/extracting-real-time-covid-19-data-from-the-ncdc-website-using-python-beautifulsoup-and-flask-d7a6965bc18",
        "date" : str(datetime.now()).split(" ")[0]
    }
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blogs")
def blogs():
    return render_template("blogs.html", posts = posts)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)