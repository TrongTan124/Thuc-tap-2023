from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from book.book import book_bp,db
from list.python_list import python_list_bp


app = Flask(__name__)
app.secret_key = "hidrodat"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:4449/book_store'
app.register_blueprint(book_bp)
app.register_blueprint(python_list_bp)
db.init_app(app) 
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

