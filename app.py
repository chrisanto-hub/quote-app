from flask import Flask, render_template
from pymongo import MongoClient
import random
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["quote_db"]
collection = db["quotes"]

@app.route("/")
def home():
    quotes = list(collection.find({}, {"_id": 0, "text": 1}))
    quote = random.choice(quotes)["text"] if quotes else "No quotes available."
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
