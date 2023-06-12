from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
app = Flask(__name__)

# config database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/MANH/Documents/GitHub/Thuc-tap-2023/DuyManh/python/flask/templates/test.db'

# config migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'date_created': self.date_created
        }
        
with app.app_context():
    db.create_all()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        tasks = Todo.query.order_by(Todo.date_created).all()
        if 'sort' in request.form:
            sort_list = request.form['lists']
            sort_list = list(map(int, sort_list.split(',')))
            sort_list = bubble_sort(sort_list)
            return render_template('index.html', lists=sort_list, tasks=tasks)  
        
        if request.headers.get('Content-Type') == 'application/json':
            task_content = request.json['content']
        else:
            task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            if request.headers.get('Content-Type') == 'application/json':
                return jsonify(new_task.to_dict())
            else:
                return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        if 'Postman' in request.headers.get('User-Agent'):
            tasks = [task.to_dict() for task in tasks]
            return jsonify(tasks)
        else:
            return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        if request.headers.get('Content-Type') == 'application/json':
            return jsonify(task_to_delete.to_dict())
        else:
            return redirect('/')
    except:
        return 'There was an issue deleting your task'

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)