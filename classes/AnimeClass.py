import requests


class AnimeClass:
    def __init__(self, id):
        self.endpoint = f"https://api.jikan.moe/v4/anime/{id}"
        self.endpoint_pictures = f"https://api.jikan.moe/v4/anime/{id}/pictures"
        self.anime_id = id
        self.anime_data = ""
        self.anime_pictures = ""
        self.h = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

    def get_anime_data(self):
        self.response = requests.get(self.endpoint, headers=self.h)
        if self.response.ok:
            anime_json = self.response.json()
            self.anime_data = anime_json['data']
            anime_data = {
                'name': self.anime_data['title'],
                'id': self.anime_data['mal_id'],
                'url_img': self.anime_data['images']['jpg']['large_image_url'],
                'score': self.anime_data['score'],
                'scored_by': self.anime_data['scored_by'],
                'rank': self.anime_data['rank'],
                'popularity': self.anime_data['popularity'],
                'members': self.anime_data['members'],
                'trailer': self.anime_data['trailer']['embed_url'],
                'synopsis': self.anime_data['synopsis'],
                'pictures': self.get_anime_pictures(),
                'more_info': self.anime_data['url'],
                'type': self.anime_data['type'],
                'status': self.anime_data['status'],
                'episodes': self.anime_data['episodes'],
                'duration': self.anime_data['duration']
            }
            return anime_data
        else:
            return False

    def get_anime_pictures(self):
        self.response_pictures = requests.get(
            self.endpoint_pictures, headers=self.h)
        if self.response_pictures.ok:
            pictures_json = self.response_pictures.json()
            self.anime_pictures = pictures_json['data']
            pictures_list = [element['jpg']['large_image_url']
                             for element in self.anime_pictures]
            return pictures_list
        else:
            return False
