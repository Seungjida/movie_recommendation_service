import json
from pprint import pprint


def book_info(book):
    stocks = {'author': book.get('author'),
              'categoryId': book.get('categoryId'),
              'cover': book.get('cover'),
              'description': book.get('description'),
              'id': book.get('id'),
              'priceSales': book.get('priceSales'),
              'title': book.get('title')}
    return stocks



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
