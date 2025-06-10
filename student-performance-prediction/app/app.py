
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return "Student Risk Prediction API is up!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    print("Received data:", data)  
    input_features = np.array(data["features"]).reshape(1, -1)
    input_scaled = scaler.transform(input_features)
    prediction = model.predict(input_scaled)[0]
    print("Prediction:", prediction)  
    return jsonify({"prediction": int(prediction)})


if __name__ == "__main__":
    app.run(debug=True)
