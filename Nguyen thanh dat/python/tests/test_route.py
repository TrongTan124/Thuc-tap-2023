import pytest
from book_CRUD import create_app
from flask import session
from book_CRUD.controller.book_controller import BookController 

@pytest.fixture()
def client():
    app = create_app()
    app.config['TESTING'] = True
    app_context = app.app_context()
    app_context.push()
    
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200

def test_update_book_get(client):
    list_book = BookController.get_list_book()
    book = list_book[1]
    response = client.get(f'/update_book/{book["id"]}')
    assert response.status_code == 200

def test_update_book_post(client):
    list_book = BookController.get_list_book()
    book = list_book[1]
    data = {
        'category': 'Fiction',
        'author': 'John Doe',
        'name': 'The Great Novel'
    }
    response = client.post(f'/update_book/{book["id"]}', data = data, follow_redirects=True)
    assert response.status_code == 200
    

def test_add_book(client):
    data = {
        'category': 'demo',
        'author': 'virtual',
        'name': 'none name'
    }
    response = client.post('/add_book', data = data, follow_redirects = True)
    assert response.status_code == 200
    

def test_delete_book(client):
    list_book = BookController.get_list_book()
    book = list_book[1]
    response = client.post(f'/delete_book/{book["id"]}', follow_redirects = True)
    assert response.status_code == 200
    
def test_sort_list(client):
    data = {
        'list':"2,1,2,3"
        }
    response = client.post("/sort_list",data = data, follow_redirects =True)
    assert response.status_code == 200
    assert session['announce'] == "Sorted list: [1, 2, 2, 3]"
    
    
