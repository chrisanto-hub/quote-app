from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "Success is not final, failure is not fatal.",
    "Dream big and dare to fail.",
    "Do one thing every day that scares you.",
    "Opportunities don't happen, you create them."
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
