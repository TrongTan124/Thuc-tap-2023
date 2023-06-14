import pytest
from sqlalchemy import create_engine
from flask import Flask
from sqlalchemy.orm import sessionmaker
from book_CRUD.model.book import db
from book_CRUD.controller.book_controller import BookController 


# engine = create_engine('')
# Session = sessionmaker(bind=engine)

@pytest.fixture(scope='function')
def confbook():
    
    app = Flask(__name__)
    app_context = app.app_context()
    app_context.push()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:4449/book_store'

    db.init_app(app) 
    
    controller = BookController
    
    yield controller

def test_add_book(confbook):
    
    book = BookController.add_book('Fiction', 'John Doe', 'Test Book')

    assert book.id is not None


def test_get_book(confbook):

    book = BookController.add_book('Fiction', 'John Doe', 'Test Book')
    retrieved_book = BookController.get_book_by_id(book.id)

    assert retrieved_book is not None
    assert retrieved_book.id == book.id


def test_update_book(confbook):

    book = BookController.add_book('Fiction', 'John Doe', 'Test Book')
    updated = BookController.update_book(book.id, author='Jane Smith')

    assert updated is True

    retrieved_book = BookController.get_book_by_id(book.id)
    assert retrieved_book.author == 'Jane Smith'
    
def test_update_book_fail(confbook):
    updated = BookController.update_book(10000, author='Jane Smith')
    
    assert updated is False


def test_delete_book(confbook):

    book = BookController.add_book('Fiction', 'John Doe', 'Test Book')
    deleted = BookController.delete_book_by_id(book.id)

    assert deleted is True

    retrieved_book = BookController.get_book_by_id(book.id)
    assert retrieved_book is None

def test_delete_book_fail(confbook):
    
    deleted = BookController.delete_book_by_id(10000000)

    assert deleted is False
    