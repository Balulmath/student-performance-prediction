
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, StandardScaler
import xgboost as xgb
import joblib

# Load data
df = pd.read_csv("../data/exams.csv")

# Generate label
df['avg_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
df['at_risk'] = (df['avg_score'] < 60).astype(int)
df.drop(columns=['avg_score'], inplace=True)

# Encode categorical
ordinal_cols = ['parental level of education', 'lunch', 'test preparation course']
categories = [[
    "some college", "some high school", "high school",
    "associate's degree", "bachelor's degree", "master's degree"
], ["free/reduced", "standard"], ["none", "completed"]]

enc_ord = OrdinalEncoder(categories=categories)
df[ordinal_cols] = enc_ord.fit_transform(df[ordinal_cols])

enc_oh = OneHotEncoder(sparse_output=False)
encoded = enc_oh.fit_transform(df[['gender', 'race/ethnicity']])
encoded_df = pd.DataFrame(encoded, columns=enc_oh.get_feature_names_out())
df = pd.concat([df.drop(columns=['gender', 'race/ethnicity']), encoded_df], axis=1)

# Split
X = df.drop("at_risk", axis=1)
y = df["at_risk"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.25, random_state=42)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")
