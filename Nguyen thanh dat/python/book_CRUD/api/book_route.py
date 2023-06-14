from flask import Blueprint, redirect, render_template, session, request
from ..controller.book_controller import BookController as BCL 


book_bp = Blueprint("book_route", __name__, template_folder="templates")


@book_bp.route('/books')
def index():
    book_list = BCL.get_list_book()
    announce = session.get('announce')  
    session.pop('announce', None) 
    return render_template("index.html", books=book_list, announce=announce)  
    
@book_bp.route('/update_book/<int:id>', methods=['POST'])
def update_book(id):
    category = request.form['category']
    author = request.form['author']
    name = request.form['name']
    BCL.update_book(id, category, author, name)
    return redirect('/books')

@book_bp.route('/update_book/<int:id>', methods=[ 'GET'])
def get_book(id):
    book = BCL.get_book_by_id(id)
    return render_template('book/update_book.html', book=book)

@book_bp.route('/add_book', methods=['POST'])
def add_book():
    name = request.form.get('name')
    author = request.form.get('author')
    category = request.form.get('category')
    BCL.add_book(name, author, category)
    return redirect('/books')

@book_bp.route('/delete_book/<int:id>', methods=['POST'])
def delete_book(id):
    BCL.delete_book_by_id(id)
    return redirect('/books')

