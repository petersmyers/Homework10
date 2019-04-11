from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    scrapings = mongo.db.scrapings.find_one()
    return render_template("index.html", scrapings=scrapings)

@app.route("/scrape")
def scraper():
    scrapings = mongo.db.scrapings
    scrapings_data = scrape_mars.scrape()
    scrapings.update({}, scrapings_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
