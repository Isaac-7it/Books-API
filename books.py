from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/my_book')
async def read_all_books():
    return {'book title': 'My favourite book!'}

@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
    return {'message': 'Not found!'}

@app.get('/books/')
async def read_books_by_query(category: str):
    books_to_return = []

    for books in BOOKS:
        if books['category'].casefold() == category.casefold():
            books_to_return.append(books)

    return books_to_return

'''
@app.get('/path')
async def get_by_query(query: str):
    return {
        'query': query
    }
'''

@app.get('/books')
async def read_by_query(category: str):
    books_to_return = []

    for book in BOOKS:
        if book['category'].casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get('/books/{author}/')
async def read_by_author_and_category(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book['author'].casefold() == author.casefold() and book['category'].casefold() == category.casefold():
            return book
    return {
        'message': 'Not Found!'
    }