from flask import Flask, redirect, url_for, request, render_template
import sqlite3
from markupsafe import escape
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()  
    conn.close()
    return render_template('index.html', posts=posts)

app.config['UPLOAD_FOLDER'] = '/home/chunporo/Documents/GitHub/Image_Augenmation/img'

@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    files = request.files.getlist('file')
    for file in files:
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('image_gen.html')


if __name__ == '__main__':  
    app.run(debug=True)