from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(50), unique= False, nullable=False)
    author = db.Column(db.String(50), unique= False, nullable=False)
    name = db.Column(db.String(50), unique= False, nullable=False)
    
    def __init__(self, category, author, name):
        self.category = category
        self.author = author
        self.name = name

    
