import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained model
model = load_model("backend/models/traffic_model.h5")

def detect_traffic(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    
    prediction = model.predict(image)
    return "High Congestion" if prediction > 0.5 else "Low Congestion"

