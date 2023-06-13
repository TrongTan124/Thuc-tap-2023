from flask import Blueprint, redirect, render_template, session, request
from model.book import Book,db

book_bp = Blueprint("book_route", __name__, template_folder="templates")


@book_bp.route('/books')
def index():
    books = Book.query.all()
    book_list = [{'id': book.id, 'category': book.category, 'author': book.author, 'name': book.name} for book in books]
    announce = session.get('announce')  
    session.pop('announce', None) 
    return render_template("index.html", books=book_list, announce=announce)  
    
@book_bp.route('/update_book/<int:id>', methods=['POST'])
def update_book(id):
    book = Book.query.get(id) 
    book.category = request.form['category']
    book.author = request.form['author']
    book.name = request.form['name']
    db.session.commit()
    db.session.clear()
    return redirect('/books')

@book_bp.route('/update_book/<int:id>', methods=[ 'GET'])
def get_book(id):
    book = Book.query.get(id)  
    return render_template('book/update_book.html', book=book)

@book_bp.route('/add_book', methods=['POST'])
def add_book():
    book_name = request.form.get('name')
    book_author = request.form.get('author')
    book_category = request.form.get('category')
    book = Book(book_category, book_author,book_name)
    db.session.add(book)
    db.session.commit()    
    db.session.clear()
    return redirect('/books')

@book_bp.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get(id)  
    db.session.delete(book)
    db.session.commit()
    db.session.clear()
    return redirect('/books')

