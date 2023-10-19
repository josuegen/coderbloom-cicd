from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    return "<h1> Hello World! </h1>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)