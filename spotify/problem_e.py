import json
from pprint import pprint as print

def dec_artists(artists):
    name_uri_id = []

    for artist in artists:
        artist_id = artist['id']
        artist_json = open(f'data/artists/{artist_id}.json', encoding='utf-8')
        artist_detail = json.load(artist_json)

        if artist_detail['followers']['total'] >= 10000000:
            name_uri_id.append({'name': artist_detail.get('name'), 'uri-id': artist_detail.get('uri').split(':')[2]})
    
    sorted_name_uri_id = sorted(name_uri_id, key = lambda x: x['name'])
    
    return sorted_name_uri_id


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    artists_json = open('data/artists.json', encoding='utf-8')
    artists_list = json.load(artists_json)

    print(dec_artists(artists_list))
