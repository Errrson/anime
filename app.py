from flask import Flask, render_template, request, redirect, url_for
from classes.AnimeListClass import AnimeListClass
from classes.AnimeClass import AnimeClass

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    current_search = None
    if request.method == 'POST':
        current_search = request.form.get("search")

    Animes = AnimeListClass()
    anime_list = Animes.get_anime_list(current_search)
    return render_template("index.html", anime_list=anime_list)


@app.route("/anime/<string:id_anime>")
def page_anime(id_anime):
    Anime = AnimeClass(id_anime)
    anime_data = Anime.get_anime_data()
    if anime_data:
        return render_template("anime.html", anime_data=anime_data)
    else:
        return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)
