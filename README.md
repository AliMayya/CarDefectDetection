# CarDefectDetection
**Prepared by:**
**Dr. Ali Mayya** (model preparation, dataset creation and annotation, training, evaluation, and writing)

**Eng Ali Altrkbi** (App design and implementation)

## Table of Contents
- [Part 1 Backend](#part 1 Backend)
- [Model creation, training, and evaluation code](#model creation, training, and evaluation code)
- [Evaluation results](#evaluation results)
- [Test samples](#test samples)
- [Test samples from Internet](#test samples from Internet)
- [validation curves](#validation curves)
- [Part2 frontend APP](#part2 frontend (APP))
- [Limitation and Future work](#limitation and Future work)

## Part 1 Backend
Mission: Design and implement a basic image-based model that detects common types of vehicle damage such as scratches, dents, or broken parts. 
Main Architecture: YOLOV8 (without pretrained weights)
1.	Collect Dataset:
o	Self-collected images of vehicle damages: 70 images
o	Classes: broken_glass, Damaged_light_tire_parts, dent, scratch
Examples:

![image](https://github.com/user-attachments/assets/022920a0-80be-4c72-a108-79ddb7ed9143)


2. Annotate dataset:
   We utilize LabelImg to annotate images using bounding boxes.
        labelImg . classes.txt
   Annotation in LabelImg example:
   
   ![image](https://github.com/user-attachments/assets/619c857d-ad3a-43c5-90b8-c398b436af32)
   

   Dataset images and labels are located in Dataset.rar file
   
3. Save images and Labels into two separate folders ("Images", "Labels")
   
4. Create YOLOV8 core model
   
5. Train model using the training set and apply the augmentation operations during training
   
6. Evaluate the trained model using both validation and test sets
   
## Model creation, training, and evaluation code
Code file: CarDefectsDetectionYOLOV8.ipynb
Output trained model file: carDamageDetectYOLOV8.pt

## Evaluation results
**Validation set:**

![image](https://github.com/user-attachments/assets/bade578c-2d0f-4512-865a-b00008a2739a)


**Test Set:**

![image](https://github.com/user-attachments/assets/c5742c6c-52fd-450b-9cca-b240f2e8fe1f)

## Test samples
Test sample1:

![image](https://github.com/user-attachments/assets/9062be5a-d4fc-48ba-a179-00a3bc95214e)

Test sample2:

![image](https://github.com/user-attachments/assets/2356850e-9394-4c67-b84d-630ebb79626a)

Test sample3:

![image](https://github.com/user-attachments/assets/792da005-8892-4e96-ad9f-6d232e857d2e)

Test Sample4:

![image](https://github.com/user-attachments/assets/7e6abdd5-90f0-43e9-b459-9aa19f564c64)


## Test samples from Internet

![image](https://github.com/user-attachments/assets/25a7aa1e-7470-402a-abe2-07f26b467f71)


## validation curves


![image](https://github.com/user-attachments/assets/1f53c4e9-1887-4424-a7da-2b349a33a465)

![image](https://github.com/user-attachments/assets/7adda13b-41fb-4eb7-81c3-4ff6322c62ce)

![image](https://github.com/user-attachments/assets/a63a676b-b3e1-4959-9582-c3fdf490d9bf)

![image](https://github.com/user-attachments/assets/bd204d1e-51b5-41a4-9821-af4b4c3ef479)


**Confusion Matrix**

![image](https://github.com/user-attachments/assets/de5518dc-8ebc-4bb7-aad0-3fe68086331a)


** Precision, Recall, mAP50 Curves**

![image](https://github.com/user-attachments/assets/e61e46b8-c85b-4172-a7ae-8e6ea1cc18f0)




**Conclusion:** Dataset needs more samples to make more roubust training (At least 1000 images with more than 3000 instances (bounding boxes)).

Feel free to contact me: a.mayya1988@gmail.com


## Part2 frontend APP
# Vehicle Damage Detection System App

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
### Test example using the APP

![61f500f0-8b64-42be-abc9-1d1655553e9e](https://github.com/user-attachments/assets/f2c4da2a-331d-460b-aa64-6da526cbc011)

![4916e4fb-6658-4e89-a335-cb7c526c2a63](https://github.com/user-attachments/assets/82676f2a-076a-404a-8b54-45bdb771423b)


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

## Limitation and Future work
The main issue is the small dataset size
Future work will increase the dataset size for a better and more robust training
