import json

def new_books(books):
    published_2023 = []

    for book in books:
        book_id = book['id']
        book_json = open(f'data/books/{book_id}.json', encoding='utf-8')
        book_detail = json.load(book_json)

        if book_detail['pubDate'][:4] == '2023':
            published_2023.append(book_detail['title'])

    return published_2023



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
