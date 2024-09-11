import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Temporary in-memory "database" of flats
flats = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', flats=flats)

@app.route('/add_flat', methods=['GET', 'POST'])
def add_flat():
    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        description = request.form.get('description')

        # Handle file upload
        file = request.files['photo']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        else:
            photo_url = None

        # Add flat to the list
        flats.append({
            'title': title,
            'price': price,
            'description': description,
            'photo': photo_url
        })

        return redirect(url_for('index'))
    return render_template('add_flat.html')

if __name__ == '__main__':
    app.run(debug=True)
