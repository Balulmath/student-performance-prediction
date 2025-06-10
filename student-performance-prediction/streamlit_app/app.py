
import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Student Risk Predictor", layout="centered")

st.title("🎓 Student Risk Prediction App")
st.markdown("Enter student information to check if they're at academic risk.")

# Inputs
gender = st.selectbox("Gender", ["female", "male"])
race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parent_edu = st.selectbox("Parental Level of Education", [
    "some college", "some high school", "high school",
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])

math_score = st.slider("Math Score", 0, 100, 50)
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

if st.button("Predict"):
    try:
        # Encode categorical (must match training)
        ordinal_map = {
            "parental level of education": {
                "some college": 0,
                "some high school": 1,
                "high school": 2,
                "associate's degree": 3,
                "bachelor's degree": 4,
                "master's degree": 5
            },
            "lunch": {"free/reduced": 0, "standard": 1},
            "test preparation course": {"none": 0, "completed": 1},
        }

        gender_encoding = [1, 0] if gender == "female" else [0, 1]
        race_encoding = [int(race == grp) for grp in ["group A", "group B", "group C", "group D", "group E"]]

        input_features = [
            ordinal_map["parental level of education"][parent_edu],
            ordinal_map["lunch"][lunch],
            ordinal_map["test preparation course"][test_prep],
            math_score,
            reading_score,
            writing_score,
            *gender_encoding,
            *race_encoding
        ]

        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"features": input_features}
        )

        if response.status_code == 200:
            pred = response.json()["prediction"]
            if pred == 1:
                st.error("⚠️ The student is AT RISK of underperforming.")
            else:
                st.success("✅ The student is NOT at risk.")
        else:
            st.warning("⚠️ Error: API call failed. Check if Flask server is running.")

    except Exception as e:
        st.exception(e)
