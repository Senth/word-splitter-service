import splitter
from flask import Flask

app = Flask(__name__)


@app.route("/<word>")
def split(word: str):
    return " ".join(splitter.split(word))
