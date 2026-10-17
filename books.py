from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get('/books/my_book')
async def read_all_books():
    return BOOKS

@app.get('/books/category/')
async def read_books_by_query(category: str):
    books_to_return = []

    for books in BOOKS:
        if books['category'].casefold() == category.casefold():
            books_to_return.append(books)

    return books_to_return

@app.get('/books/author/')
async def fetch_book_by_author(author: str):
    filtered_books = []

    for book in BOOKS:
        if book['author'].casefold() == author.casefold():
            filtered_books.append(book)

    if not filtered_books:
        return {
            'message': '404'
        }

    return filtered_books

@app.get('/books/{book_title}/')
async def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
    return {'message': 'Not found!'}

@app.get('/books/{author}/')
async def read_by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == author.casefold() and book['category'].casefold() == category.casefold():
            return book
    return {
        'message': 'Not Found!'
    }

@app.post('/books/create_books/')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book/')
async def update_book(modified_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == modified_book['title'].casefold():
            BOOKS[i] = modified_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

