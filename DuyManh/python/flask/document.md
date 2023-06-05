#### Configure Flask-SQLAlchemy with Flask application
- pip install Flask-SQLAlchemy: Install Flask-SQLAlchemy
- import app.py: 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(\_\_name\_\_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_file.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False (vô hiệu hóa theo dõi sửa đổi, cải thiện hiệu suất.)
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def \_\_repr\_\_(self):
        return '<User %r>' % self.username
with app.app_context():
    db.create_all()
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

