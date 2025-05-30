# 🎯 Student Risk Prediction

This project predicts whether high school students are at risk of underperforming using demographic and academic data. The solution uses machine learning classification models and is prepared for deployment via Flask.

---

## 📁 Dataset

- **Source**: [Kaggle - Student Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Attributes**:
  - `Gender`, `Race/Ethnicity`
  - `Parental Level of Education`
  - `Lunch` program type
  - `Test Preparation Course`
  - `Math`, `Reading`, `Writing` scores

---

## 🧠 Objective

To predict whether a student is **at risk of underperforming** (i.e., average score < 60) and to enable early interventions by school systems.

---

## 🧪 Models Used

- Logistic Regression
- Random Forest
- Decision Tree
- K-Nearest Neighbors
- XGBoost

---

## 🎯 Evaluation Metrics

- **Accuracy**
- **F1 Score**
- **Confusion Matrix**
- **Classification Report**

---

## 📊 Visualizations

- 🔍 Feature Importance from XGBoost
- 📉 Model comparison by Accuracy and F1 Score
- 📚 Confusion matrix and precision/recall metrics

---

## 🔐 Data Privacy

- Data is synthetic and anonymized.
- Sensitive fields were removed in the preprocessing pipeline.

---

## 💻 Tech Stack

- Python 3.12+
- Jupyter Notebook
- Scikit-learn
- XGBoost
- Pandas, Seaborn, Matplotlib
- Flask (for deployment)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/student-risk-prediction.git
cd student-risk-prediction
