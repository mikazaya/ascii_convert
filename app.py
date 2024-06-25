import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

from ascii import convert

UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = {'webp', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__,template_folder="j2")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key="lol"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html.j2")


@app.route("/upload", methods=("POST",))
def upload_hyperscript():
        
    if 'file' not in request.files:
        flash('No file sent')
    else:
        file=request.files['file']
        if file.filename=='':
            flash("You didn't enter a file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            saved_path=os.path.join("images",filename)
            file.save(saved_path)
            ascii=convert(saved_path)

            return (f'''<textarea id="ascii_result">{ascii}</textarea>''', 200) 

    
        

    


app.run("localhost","5000")