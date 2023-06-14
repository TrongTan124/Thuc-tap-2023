from ..model.book import Book, db


class BookController:
    # def __init__(self,session):
    #     self.session = session
    
    def get_list_book():
        books = Book.query.all()
        book_list = [{'id': book.id, 'category': book.category, 'author': book.author, 'name': book.name} for book in books]
        return book_list
    
    def update_book(id, category = None, author = None, name = None):
        book = Book.query.get(id)
        if book:
            if category:
                book.category = category
            if author:
                book.author = author
            if name: 
                book.name = name
            db.session.commit()
            return True
        return False
   
    def get_book_by_id(id):
        book = Book.query.get(id)
        return book
    
    def add_book(name, author, category):
        book_name = name
        book_author = author
        book_category = category
        book = Book(book_category, book_author, book_name)
        db.session.add(book)
        db.session.commit()
        books = Book.query.all()
        
        return books[-1] 
         
    
    def delete_book_by_id(id):
        book = Book.query.get(id)
        if book:   
            db.session.delete(book)
            db.session.commit()
            return True
        
        return False
    