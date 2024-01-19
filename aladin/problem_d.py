import json


def best_book(books):
    review_title = []

    for book in books:
        book_id = book['id']
        book_json = open(f'data/books/{book_id}.json', encoding='utf-8')
        book_detail = json.load(book_json)

        review_title.append({'customerReviewRank': book_detail['customerReviewRank'], 'title': book_detail['title']})
    
    sorted_review_title = sorted(review_title, key = lambda x: x['customerReviewRank'], reverse=True)
    return sorted_review_title[0]['title']


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
