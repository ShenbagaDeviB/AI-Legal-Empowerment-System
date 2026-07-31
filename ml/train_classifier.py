import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("legal_dataset.csv")

print("Dataset Loaded Successfully")
print(data.head())

# -----------------------------
# Clean Text
# -----------------------------
data['text'] = data['text'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

# -----------------------------
# Encode Categories
# -----------------------------
le = LabelEncoder()
data['label'] = le.fit_transform(data['category'])

print("\nCategory Mapping:")
for i, category in enumerate(le.classes_):
    print(i, "->", category)

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    data['text'],
    data['label'],
    test_size=0.2,
    random_state=42
)

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# -----------------------------
# Evaluate Model
# -----------------------------
y_pred = model.predict(X_test_vec)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# -----------------------------
# Save Model Files
# -----------------------------
pickle.dump(model, open("legal_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("\nModel saved successfully!")