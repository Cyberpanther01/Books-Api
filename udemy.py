from fastapi import Body, FastAPI

app = FastAPI()


BOOKS = [
    {'title': 'Title one', 'author': 'Author One', 'category': 'Science'},
    {'title': 'Title two', 'author': 'Author two', 'category': 'Math'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'Physics'},
    {'title': 'Title four', 'author': 'Author four', 'category': 'Chemistry'},
    {'title': 'Title five', 'author': 'Author two', 'category': 'Arts'},
    {'title': 'Title six', 'author': 'Author six', 'category': 'History'},
    {'title': 'Title three', 'author': 'Author three', 'category': 'English'},
    {'title': 'Title seven', 'author': 'Author seven', 'category': 'Agric'}

]



@app.get("/books/title%20four")
def getBooks(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get('/books')
def read_all_books():
    return BOOKS
        
@app.get('/books/{dynamic_param}')
def readAllBooks(dynamic_param: str):
    return {'dynamic_param': dynamic_param} 


@app.get('/books/{book_title}')
def readAllBooks(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return


@app.get('/books/')
def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return



@app.get("/books/{book_author}/")
def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold()  == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return



@app.post('/books/create_book')
def create_book(new_book = Body()):
    BOOKS.append(new_book)
 
@app.put("/books/update_book")
def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
 