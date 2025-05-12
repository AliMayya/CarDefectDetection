# Vehicle Damage Detection System

A computer vision application that detects and classifies vehicle damage such as scratches, dents, and broken parts using a YOLOv8 object detection model.

## Features

- Detects different types of vehicle damage (scratches, dents, broken lights, etc.)
- Web interface for easy image upload and analysis
- REST API for integration with other applications
- Visual results with annotated images highlighting damage locations

## Requirements

- Python 3.8+
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv car_detection_env
   ```
3. Activate the virtual environment:
   - Windows: `car_detection_env\Scripts\activate`
   - Linux/Mac: `source car_detection_env/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

1. Activate your virtual environment
2. Run the Flask application:
   ```
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000`
4. Upload an image of a vehicle and click "Analyze Image"

### Using the API

You can also use the REST API to integrate with other applications:

**Endpoint**: `/api/detect`
**Method**: POST
**Parameters**:
- `file`: Image file (multipart/form-data)
- `threshold` (optional): Detection confidence threshold (default: 0.25)

**Example using curl**:
```
curl -X POST -F "file=@path/to/your/image.jpg" -F "threshold=0.3" http://127.0.0.1:5000/api/detect
```

**Example Response**:
```json
{
  "success": true,
  "message": "Detected 2 instances of damage",
  "data": {
    "count": 2,
    "detections": [
      {
        "class": "scratch",
        "confidence": 0.92,
        "bbox": [120, 145, 380, 225]
      },
      {
        "class": "dent",
        "confidence": 0.78,
        "bbox": [420, 190, 520, 310]
      }
    ]
  }
}
```

### Running Inference Script

For direct image analysis without the web interface, use the `inference.py` script:

```
python inference.py --image path/to/your/image.jpg --threshold 0.25
```

The script will display the analysis results and save an annotated image.

## Project Structure

- `app.py`: Flask web application
- `inference.py`: Command-line inference script
- `models/`: Contains the trained YOLOv8 model
- `utils/`: Utility functions for model operations and image processing
- `static/`: Static assets for the web application
- `templates/`: HTML templates for the web application

## Model Details

The car damage detection model is based on YOLOv8, trained to detect the following types of damage:
- Scratches
- Dents
- Broken lights
- Broken bumpers
- Other damage types

The model was trained on a diverse dataset of vehicle images with various damage types, captured from different angles and lighting conditions.

## License

[Your License] 