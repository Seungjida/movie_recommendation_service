import json
from pprint import pprint


def artist_info(artists, genres):
    artists_information = []

    for artist in artists:
        genres_ids = artist.get('genres_ids')
        genres_names = []

        for id in genres_ids:
            for genre in genres:
                if id == genre['id']:
                    genres_names.append(genre['name'])

        artists_information.append({'genres_names': genres_names,
                        'id': artist.get('id'),
                        'images': artist.get('images'),
                        'name': artist.get('name'),
                        'type': artist.get('type')
                        })
    return artists_information


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))
