import json
from pprint import pprint


def artist_info(artist):
    artist_information = {'genres_ids': artist.get('genres_ids'),
              'id': artist.get('id'),
              'images': artist.get('images'),
              'name': artist.get('name'),
              'type': artist.get('type')
            }       
    return artist_information


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artist_json = open('data/artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    pprint(artist_info(artist_dict))
