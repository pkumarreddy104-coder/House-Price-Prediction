import joblib
import numpy as np

print("Loading model...")
model = joblib.load("house_price_model.pkl")
print("Model loaded successfully")

sample_house = np.array([[8.3, 41, 6.9, 1.02, 322, 2.5, 37.8, -122.2]])
print("Input:", sample_house)

prediction = model.predict(sample_house)
print("Prediction raw output:", prediction)

print("Predicted Median House Value:", prediction[0])

