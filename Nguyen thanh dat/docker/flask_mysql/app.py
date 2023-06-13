import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from book.book import book_bp,db
from list.python_list import python_list_bp

load_dotenv()
app = Flask(__name__)
app.secret_key = "hidrodat"
# app.config['SQLALCHEMY_DATABASE_URI'] = c
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.register_blueprint(book_bp)
app.register_blueprint(python_list_bp)
db.init_app(app) 
migrate = Migrate(app, db)

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True,host='0.0.0.0', port=5000)
