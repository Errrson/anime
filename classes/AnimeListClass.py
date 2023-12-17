import requests


class AnimeListClass:

    def __init__(self):
        self.url_base = "https://api.jikan.moe/v4/anime"
        self.h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    def get_anime_list(self, anime_name=None) -> list:
        if anime_name == None:
            self.url_full = self.url_base
        else:
            self.url_full = f"{self.url_base}?q={anime_name}"

        self.response = requests.get(self.url_full, headers=self.h)
        self.results = self.response.json()
        list_animes = []
        for element in self.results["data"]:
            dict_tmp = {
                'name': element["title"],
                'url_img': element["images"]["jpg"]["large_image_url"],
                'url_anime': f"/anime/{element['mal_id']}"
            }
            list_animes.append(dict_tmp)
        return list_animes
