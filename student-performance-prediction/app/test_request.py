import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "features": [
        # Ordinal Encoded
        2,  # parental level of education (e.g., high school)
        1,  # lunch (1 = standard)
        0,  # test prep course (0 = none)
        
        # Raw scores
        65, 70, 75,
        
        # One-hot Encoded Gender
        1,  # female
        0,  # male
        
        # One-hot Encoded Race/Ethnicity (only one should be 1, rest 0)
        0, 1, 0, 0, 0
    ]
}

response = requests.post(url, json=data)
print("STATUS:", response.status_code)
print("RESPONSE:", response.json())