# CarDefectDetection
Mission: Design and implement a basic image-based model that detects common types of vehicle damage such as scratches, dents, or broken parts. 
Main Architecture: YOLOV8 (without pretrained weights)
1.	Collect Dataset:
o	Self-collected images of vehicle damages: 70 images
o	Classes: broken_glass, Damaged_light_tire_parts, dent, scratch

2. Annotate dataset:
   We utilize LabelImg to annotate images using bounding boxes.
        labelImg . classes.txt
3. Save images and Labels into two separate folders ("Images", "Labels")
4. Create YOLOV8 core model
5. Train model using the training set and apply the augmentation operations during training
6. Evaluate the trained model using both validation and test sets

**Evaluation results:**
Validation set:

![image](https://github.com/user-attachments/assets/bade578c-2d0f-4512-865a-b00008a2739a)


Test Set:

![image](https://github.com/user-attachments/assets/c5742c6c-52fd-450b-9cca-b240f2e8fe1f)

**Test samples:**
Test sample1:

![image](https://github.com/user-attachments/assets/9062be5a-d4fc-48ba-a179-00a3bc95214e)

Test sample2:

![image](https://github.com/user-attachments/assets/2356850e-9394-4c67-b84d-630ebb79626a)

Test sample3:

![image](https://github.com/user-attachments/assets/792da005-8892-4e96-ad9f-6d232e857d2e)

Test Sample4:

![image](https://github.com/user-attachments/assets/7e6abdd5-90f0-43e9-b459-9aa19f564c64)


**Test samples from Internet**

![image](https://github.com/user-attachments/assets/25a7aa1e-7470-402a-abe2-07f26b467f71)


**validation curves**


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





