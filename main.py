import numpy as np
import cv2
from tensorflow.keras.models import load_model
import tensorflow as tf


facetracker = load_model('face-bottel-model')

width = 650
height = 450

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _ , frame = cap.read()
#    frame = frame[50:500, 50:500,:]
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(width,height))
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(rgb, (120,120))
    
    yhat = facetracker.predict(np.expand_dims(resized/255,0))
    sample_coords = yhat[1][0]
    
    # Controls the main rectangle
    cv2.rectangle(frame, 
                    tuple(np.multiply(sample_coords[:2], [width,height]).astype(int)),
                    tuple(np.multiply(sample_coords[2:], [width,height]).astype(int)), 
                        (255,0,0), 2)
    # Controls the label rectangle
    cv2.rectangle(frame, 
                    tuple(np.add(np.multiply(sample_coords[:2], [width,height]).astype(int), 
                                [0,-30])),
                    tuple(np.add(np.multiply(sample_coords[:2], [width,height]).astype(int),
                                [80,0])), 
                        (255,0,0), -1)
    
    # Controls the text rendered
    cv2.putText(frame, 'face', tuple(np.add(np.multiply(sample_coords[:2], [width,height]).astype(int),
                                            [0,-5])),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    
    cv2.imshow('FaceTrack', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()