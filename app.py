from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape as ms


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route('/')
def index():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars_data=mars_data)


@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = ms.scrape()
    mars.update(
        {},
        mars_data,
        upsert=True
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
