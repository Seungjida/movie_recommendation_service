import json
from pprint import pprint


def book_info(book, categories):
    categoryId = book.get('categoryId')
    categoryName = []

    for standard_id in categoryId:
        for category in categories:
            if standard_id == category['id']:
                categoryName.append(category['name'])

    stocks = {'author': book.get('author'),
              'categoryName': categoryName,
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

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
