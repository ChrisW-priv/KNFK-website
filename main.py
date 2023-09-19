from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    with open("index.html") as file:
        site_str = file.read()
    return site_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
