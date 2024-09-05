
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd
import cv2
import numpy as np
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
from image_processing import calculate_image_metrics, classify_complexity

app = Flask(__name__)

# Path to save uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage where the image is uploaded
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if an image is uploaded
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Process the image and extract metrics
            length, width, area, shape, complexity = calculate_image_metrics(file_path)
            complexity_label = classify_complexity(complexity)

            return render_template('index.html', image_url=file_path, length=length, width=width, area=area, 
                                   shape=shape, complexity=complexity_label)
    
    return render_template('index.html')

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
