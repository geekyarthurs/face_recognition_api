import os
from flask import Flask, request, redirect, url_for, render_template, send_file, send_from_directory, make_response
from werkzeug.utils import secure_filename
from face_detection import face_detector
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            
            return 'Image Not Found'
        file = request.files['file']
        secure_file = file.filename
        file.save(secure_file)
        face_detector(secure_file)
        print(secure_file)


        response = make_response(secure_file))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = 0
        
        return response


        

        
    if request.method == 'GET':
        
        return render_template("index.html")

if __name__ == '__main__':
    app.run()
