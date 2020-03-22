from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/hemisphere_challenge_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   hemisphere_challenge = mongo.db.hemisphere_challenge.find_one()
   return render_template("index.html", hemisphere_challenge=hemisphere_challenge)

@app.route("/scrape")
def scrape():
   hemisphere_challenge = mongo.db.hemisphere_challenge
   hemisphere_challenge_data = scraping_challenge.scrape_all()
   hemisphere_challenge.update({}, hemisphere_challenge_data, upsert=True)
   return "If that worked I'll fall of my chair!"

if __name__ == "__main__":
   app.run()