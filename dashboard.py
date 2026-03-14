from flask import Flask
from stats import stats

app = Flask(__name__)

@app.route("/")
def home():

    return {
        "signals":stats["signals"],
        "wins":stats["wins"],
        "loss":stats["loss"]
    }

app.run(port=8080)
