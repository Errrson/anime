from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/anime/<string:name_anime>")
def page_anime(name_anime):
    return render_template("anime.html", name_anime=name_anime)


if __name__ == "__main__":
    app.run(debug=True)
