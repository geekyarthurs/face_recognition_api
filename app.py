import os
from flask import Flask, request, redirect, url_for, render_template, send_file, send_from_directory, make_response
from werkzeug.utils import secure_filename
from face_detection import face_detector
UPLOAD_FOLDER = '/uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
        

            
            return 'Image Not Found'
        
        
        file = request.files['file']
        if not allowed_image(file):
            return "Invalid Image :D Not hacking"
        secure_file = file.filename
        file.save("./uploads/" + secure_file)
        face_detector("./uploads/" + secure_file)
        print(secure_file)


        response = make_response(send_file("./uploads/" + secure_file))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = 0
        
        return response


        

        
    if request.method == 'GET':
        
        return render_template("index.html")

def allowed_image(filename):
    
    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
