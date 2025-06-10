#!/bin/bash
sudo apt update && sudo apt install -y python3-pip git
pip3 install flask pandas scikit-learn xgboost joblib
git clone https://github.com/your-username/student-risk-predictor.git
cd student-risk-predictor/app
python3 app.py
