from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/anime/<string:name_anime>")
def page_anime(name_anime):
    return render_template("anime.html", name_anime=name_anime)


@app.route("/anime/search", methods=['POST'])
def search():
    current_search = "nada"
    if request.method == 'POST':
        current_search = request.form.get("search")

    return redirect(url_for("index", current_search=current_search))


if __name__ == "__main__":
    app.run(debug=True)
