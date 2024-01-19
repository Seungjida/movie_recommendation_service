import json
from pprint import pprint


def books_info(books, categories):
    stocks = []
    for book in books:
        categoryId = book.get('categoryId')
        categoryName = []

        for standard_id in categoryId:
            for category in categories:
                if standard_id == category['id']:
                    categoryName.append(category['name'])

        stocks.append({'author': book.get('author'),
                       'categoryName': categoryName,
                       'cover': book.get('cover'),
                       'description': book.get('description'),
                       'id': book.get('id'),
                       'priceSales': book.get('priceSales'),
                       'title': book.get('title')})
    return stocks


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
