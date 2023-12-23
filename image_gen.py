import os
import time 
import uuid
import cv2

IMAGES_PATH = os.path.join("new_data", "images")
number_images = 60

# Create the directory if it doesn't exist
os.makedirs(IMAGES_PATH, exist_ok=True)

cap = cv2.VideoCapture(0)

for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    
    # Capture a frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    # Check if the frame is not empty
    if not ret:
        print("Error: Couldn't capture frame.")
        break
    
    # Generate a unique image name using UUID
    imgname = os.path.join(IMAGES_PATH, f'{str(uuid.uuid1())}.jpg')
    
    # Save the image
    cv2.imwrite(imgname, frame)
    
    # Display the frame
    cv2.imshow('frame', frame)
    
    # Pause for a short duration
    time.sleep(0.5)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera resources
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
