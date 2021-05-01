# app.py
# Mohammed Perves
# April 30, 2021

from flask import Flask, render_template, url_for, request, flash
from werkzeug.utils import secure_filename
import os
from object_dection import detect
import mysql.connector


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


host='localhost'
db = 'shopify'
user = 'root'
password = ''


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'




#************************************************Index & Search************************************************
@app.route('/', methods=['GET', 'POST'])
def index():
    connection = mysql.connector.connect(host=host, database=db, user=user, password=password)
    results = []
    keyword = ""
    category = "contents"
    cursor = connection.cursor()
    sql = "SELECT * FROM images"
    cursor.execute(sql, ())
    results = cursor.fetchall()
    cursor.close()

    if request.method == 'POST':
        req = request.form
        keyword = req.get("keyword", default="")
        category = req.get("category", default="contents")
        #print(category, keyword)
        sql = "SELECT * FROM images WHERE objects LIKE '%' %s '%' OR tags LIKE '%' %s '%' OR descr LIKE '%' %s '%' OR category LIKE '%' %s '%' OR title LIKE '%' %s '%'"
        cursor = connection.cursor()
        cursor.execute(sql, (keyword, keyword, keyword, keyword, keyword))
        results = cursor.fetchall()
        cursor.close()
        return render_template('index.html', results=results, category=category, keyword=keyword)

    return render_template('index.html', results=results, keyword=keyword)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




#************************************************Upload Route************************************************
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    connection = mysql.connector.connect(host=host, database=db, user=user, password=password)
    if request.method == 'POST':
        req = request.form
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
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            img_file.save(img_path)
            #print(title, descr, tags, category)
            
            objects = detect(img_path)
            objects_str = ','.join(objects)

            #print(objects)

            try:
                cursor = connection.cursor()
                sql = """ INSERT INTO images (id, title, descr, tags, category, objects, img) VALUES (null, %s, %s, %s, %s, %s, %s)"""
                data = (title, descr, tags, category, objects_str, filename)
                cursor.execute(sql, data)
                connection.commit()
                cursor.close()
                flash('Image uploaded', 'success')
            except mysql.connector.Error as error:
                flash('Ooopsie Daisy...There was an error', 'danger')
                print("Failed inserting BLOB data into MySQL table {}".format(error))
        else:
            flash('Please upload an image file', 'warning')

    return render_template('upload.html')
    


if __name__ == "__main__":
    app.run(debug=True)