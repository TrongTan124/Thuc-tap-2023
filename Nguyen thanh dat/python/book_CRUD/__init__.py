from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from .model.book import db
from .api.book_route import book_bp
from .api.list_route import python_list_bp

load_dotenv()
def create_app(DB_URL = "mysql://root:123@127.0.0.1:4449/book_store"):
    app = Flask(__name__)
    app.secret_key = "hidrodat"
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.register_blueprint(book_bp)
    app.register_blueprint(python_list_bp)
    db.init_app(app) 
    migrate = Migrate(app, db)
    return app


