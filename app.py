import os
import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from utils.model_utils import load_model, predict_damage
from utils.image_processing import preprocess_image, overlay_predictions

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load model when app starts
model = None

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Load model if not loaded
        global model
        if model is None:
            model = load_model()
            # Set confidence threshold (can be made configurable through frontend)
            model.conf = 0.25
        
        # Process image and make prediction
        processed_img = preprocess_image(filepath)
        result = predict_damage(model, processed_img)
        
        # Create annotated image
        annotated_img_path = overlay_predictions(filepath, result['detections'])
        # Get relative path for frontend
        annotated_img_rel_path = annotated_img_path.replace('\\', '/').replace('static/', '')
        
        return jsonify({
            'result': result,
            'image_path': filepath.replace('\\', '/').replace('static/', ''),
            'annotated_image_path': annotated_img_rel_path
        })
    
    return jsonify({'error': 'Invalid file type'})

@app.route('/api/detect', methods=['POST'])
def api_detect():
    """API endpoint for programmatic access"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Load model if not loaded
        global model
        if model is None:
            model = load_model()
            model.conf = 0.25
        
        # Get confidence threshold from request if provided
        threshold = request.form.get('threshold', 0.25)
        try:
            model.conf = float(threshold)
        except ValueError:
            model.conf = 0.25
        
        # Process image and make prediction
        result = predict_damage(model, filepath)
        
        return jsonify({
            'success': True,
            'message': f"Detected {result['count']} instances of damage",
            'data': result
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True) 