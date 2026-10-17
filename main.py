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

@app.get('/books/')
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