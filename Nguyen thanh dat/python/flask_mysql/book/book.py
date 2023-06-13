from flask import Blueprint, redirect, render_template, session, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
book_bp = Blueprint("book", __name__, template_folder="templates")


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), unique= False, nullable=False)
    author = db.Column(db.String(50), unique= False, nullable=False)
    name = db.Column(db.String(50), unique= False, nullable=False)
    buyer = db.Column(db.String(50), unique= False, nullable=False)

    def __init__(self, category, author, name):
        self.category = category
        self.author = author
        self.name = name

    def init_app(app):
        db.init_app(app)
        with app.app_context():
            db.create_all()
        return db
    
@book_bp.route('/books')
def check_database_connection():
    books = Book.query.all()
    book_list = [{'id': book.id, 'category': book.category, 'author': book.author, 'name': book.name} for book in books]
    announce = session.get('announce')  # Retrieve the 'announce' message from the session
    session.pop('announce', None)  # Clear the 'announce' message from the session
    return render_template("index.html", books=book_list, announce=announce)  # Pass the 'announce' variable to the template  
    # return render_template('../templates/index.html', books=book_list, announce=announce)  # Pass the 'announce' variable to the template  

@book_bp.route('/update_book/<int:id>', methods=[ 'POST'])
def update_book(id):
    book = Book.query.get(id)  # Get the book object by its ID
    # Update the book details
    book.category = request.form['category']
    book.author = request.form['author']
    book.name = request.form['name']
    db.session.commit()
    return redirect('/books')

@book_bp.route('/update_book/<int:id>', methods=[ 'GET'])
def getbook(id):
    book = Book.query.get(id)  # Get the book object by its ID
    return render_template('book/update_book.html', book=book)

@book_bp.route('/receive_book', methods=['POST'])
def receive_book():
    # Process the book data received from the request
    # For example, you can access the book data using request.form
    book_name = request.form.get('name')
    book_author = request.form.get('author')
    book_category = request.form.get('category')
    book = Book(book_category, book_author,book_name)

    # Add the book to the database
    db.session.add(book)
    db.session.commit()    
    # Redirect to the "/book" route
    return redirect('/books')

@book_bp.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get(id)  # Get the book object by its ID

    db.session.delete(book)
    db.session.commit()

    return redirect('/books')

