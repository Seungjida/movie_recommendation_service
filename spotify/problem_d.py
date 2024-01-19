import json


def max_polularity(artists):
    popularity_name = []

    for artist in artists:
        artist_id = artist['id']
        artist_json = open(f'data/artists/{artist_id}.json', encoding='utf-8')
        artist_detail = json.load(artist_json)

        popularity_name.append({'popularity': artist_detail['popularity'], 'name': artist_detail['name']})
    
    sorted_popularity_name = sorted(popularity_name, key = lambda x: x['popularity'], reverse=True)
    
    return sorted_popularity_name[0]['name']

# 아래의 코드는 수정하지 않습니다.
if __name__ == "__main__":
    artists_json = open("data/artists.json", encoding="utf-8")
    artists_list = json.load(artists_json)

    print(max_polularity(artists_list))
