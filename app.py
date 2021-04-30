from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from werkzeug.utils import secure_filename
import os
from object_dection import detect
from conn import connection
import mysql.connector
import io
import re

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    keyword = ""
    category = "contents"
    cursor = connection.cursor()
    sql = "SELECT * FROM images"

    cursor.execute(sql, ())
    results = cursor.fetchall()

    if request.method == 'POST':
        req = request.form
        keyword = req.get("keyword", default="")
        category = req.get("category", default="contents")
        #print(category, keyword)
        sql = "SELECT * FROM images WHERE objects LIKE '%' %s '%' OR tags LIKE '%' %s '%' OR descr LIKE '%' %s '%' OR category LIKE '%' %s '%' OR title LIKE '%' %s '%'"
        cursor.execute(sql, (keyword, keyword, keyword, keyword, keyword))
        results = cursor.fetchall()
        return render_template('index.html', results=results, category=category, keyword=keyword)
        
    return render_template('index.html', results=results, keyword=keyword)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    msg = ""
    if request.method == 'POST':
        req = request.form
        msg = "File uploaded"
        title = req.get("title")
        descr = req.get("descr")
        tags = req.get("tags")
        category = req.get("category")

        if 'img' not in request.files:
            flash('No image selected', 'info')

        img_file = request.files['img']
        if img_file.filename == '':
            flash('No image selected', 'info')

        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
            #print(filename)
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print(title, descr, tags, category)
            
            objects = detect(filename)
            objects_str = ','.join(objects)

            #print(objects)

            try:
                cursor = connection.cursor()
                sql = """ INSERT INTO images (id, title, descr, tags, category, objects, img) VALUES (null, %s, %s, %s, %s, %s, %s)"""
                data = (title, descr, tags, category, objects_str, filename)
                cursor.execute(sql, data)
                connection.commit()
                flash('Image uploaded', 'success')
            except mysql.connector.Error as error:
                flash('Ooopsie Daisy...There was an error', 'danger')
                print("Failed inserting BLOB data into MySQL table {}".format(error))
        else:
            flash('Please upload an image file', 'warning')

    return render_template('upload.html')
    


if __name__ == "__main__":
    app.run(debug=True)