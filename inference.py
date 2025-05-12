import os
import cv2
import argparse
import matplotlib.pyplot as plt
from utils.model_utils import load_model, predict_damage
from utils.image_processing import overlay_predictions

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Car Damage Detection Inference')
    parser.add_argument('--image', type=str, required=True, help='Path to the input image')
    parser.add_argument('--threshold', type=float, default=0.25, help='Confidence threshold (default: 0.25)')
    args = parser.parse_args()
    
    # Check if image exists
    if not os.path.exists(args.image):
        print(f"Error: Image not found at {args.image}")
        return
    
    # Load model
    print("Loading model...")
    model = load_model()
    
    # Set confidence threshold
    model.conf = args.threshold
    
    # Perform prediction
    print(f"Analyzing image: {args.image}")
    results = predict_damage(model, args.image)
    
    # Display results
    if results['count'] == 0:
        print("No damage detected in the image.")
    else:
        print(f"Detected {results['count']} instances of damage:")
        for i, detection in enumerate(results['detections']):
            print(f"  {i+1}. {detection['class']} (Confidence: {detection['confidence']:.2f})")
    
    # Visualize results
    annotated_image_path = overlay_predictions(args.image, results['detections'])
    print(f"Annotated image saved to: {annotated_image_path}")
    
    # Display the annotated image
    img = cv2.imread(annotated_image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.title('Car Damage Detection Results')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 