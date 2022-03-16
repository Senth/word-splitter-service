import splitter
from flask import Flask

app = Flask(__name__)


@app.route("/split")
def split():
    return " ".join(splitter.split("entityculling"))
