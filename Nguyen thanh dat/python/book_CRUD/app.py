import os
from dotenv import load_dotenv
from book_CRUD import create_app

load_dotenv()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
