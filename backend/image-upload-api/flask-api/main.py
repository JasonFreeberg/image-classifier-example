import json
import numpy as np
from app import app
from flask import request, jsonify, send_from_directory
from PIL import Image, ImageOps
from tensorflow.keras.models import model_from_json

# Allowed file types for the image
ALLOWED_EXTENSIONS = set(['jpeg', 'png', 'jpg'])

# File extension must be from ALLOWED_EXTENSIONS
def allowed_file(filename):
    '''
    This function checks if the uploaded file has the correct extensions.
    '''
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Deserialize the json file and create the model
with open("./notebooks/models/2021-09-06-keras.json", "r") as json_file:
    json_model = json.load(json_file)

model_test = model_from_json(json_model)

# Some functions for resp
def result(array):
    '''
    Given the prediciton array from the model, this method returns the predicted label.
    '''
    if array[0][0] > array[0][1]:
        return 'genuine'
    if array[0][0] < array[0][1]:
        return 'forged'
    return 'unable to determine'

def result_percentage(array):
    '''
    Given the prediction array from the model, this method returns the prediction confidence.
    '''
    if array[0][0] > array[0][1]:
        return "{:.2f}".format(array[0][0] * 100)
    if array[0][0] < array[0][1]:
        return "{:.2f}".format(array[0][1] * 100)
    return 'unable to determine'

# serving index.html on flask
@app.route('/')
def home():
    '''
    This function creates a URL route for index.html.
    '''
    return send_from_directory('frontend', 'index.html')

# API to validate the Image file
@app.route('/image-upload', methods=["POST"])
def image_upload():
    '''
    This function creates an API to handele image uploading.
    '''
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    file = request.files['file']
    # Handler for no file selected
    if file.filename == '':
        resp = jsonify({'message': "No Image selected for upload"})
        resp.status_code = 400
        return resp

    # Correct request
    if file and allowed_file(file.filename):
        

        img = Image.open(file)
        if 'L' in img.getbands():
            img = ImageOps.colorize(img, black='blue', white='white')
        img_after_resize = img.resize((200,200))
        img_array = np.asarray(img_after_resize)
        img_array_optimized = np.array(img_array, dtype = 'float32')/255.0
        data = img_array_optimized.reshape((1,-1))
        prediction = model_test.predict(data)
        print(prediction)
        resp = jsonify({
            'predicted-label':  str(result(prediction)),
            "prediction-confidence-percentage": str(result_percentage(prediction))
            })
        resp.status_code = 201
        return resp

    resp = jsonify({'message': 'Allowed file types are jpeg, png, jpg'})
    resp.status_code = 400
    return resp

# Start Flask App
if __name__ == "__main__":
    app.run(debug = True, host ='0.0.0.0', port = 5000)
