from flask import Flask, render_template, request, redirect, url_for
from classes.AnimeListClass import AnimeListClass
from classes.AnimeClass import AnimeClass

app = Flask(__name__)


@app.route("/")
def index():
    Animes = AnimeListClass()
    anime_list = Animes.get_anime_list()
    return render_template("index.html", anime_list=anime_list)


@app.route("/anime/<string:id_anime>")
def page_anime(id_anime):
    Anime = AnimeClass(id_anime)
    anime_data = Anime.get_anime_data()
    return render_template("anime.html", anime_data=anime_data)


@app.route("/anime/search", methods=['POST'])
def search():
    current_search = "nada"
    if request.method == 'POST':
        current_search = request.form.get("search")

    return redirect(url_for("index", current_search=current_search))


if __name__ == "__main__":
    app.run(debug=True)
