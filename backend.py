from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

# Load trained model files
model = pickle.load(open("legal_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connection


# Home Route (for testing)
@app.route("/", methods=["GET"])
def home():
    return "AI Legal Empowerment Backend is Running!"


# Legal Advice Dictionary
legal_info = {
    "Domestic Violence": {
        "law": "Protection of Women from Domestic Violence Act, 2005",
        "section": "Provides protection orders and legal remedies.",
        "advice": "You can approach police or seek protection orders."
    },
    "Cyber Crime": {
        "law": "Information Technology Act, 2000",
        "section": "Section 66C, 66E",
        "advice": "Report this to cyber crime cell and preserve digital evidence."
    },
    "Workplace Harassment": {
        "law": "Sexual Harassment of Women at Workplace Act, 2013",
        "section": "Internal Complaints Committee provision",
        "advice": "You can file complaint with ICC in your organization."
    },
    "Dowry Harassment": {
        "law": "Dowry Prohibition Act, 1961",
        "section": "IPC 498A",
        "advice": "Dowry demand is illegal. You can file a complaint."
    },
    "Child Abuse": {
        "law": "POCSO Act, 2012",
        "section": "Protection of Children from Sexual Offences",
        "advice": "Report immediately to child protection authorities."
    },
    "Stalking/Threat": {
        "law": "Indian Penal Code",
        "section": "Section 354D, Section 506",
        "advice": "You can file FIR under stalking and intimidation sections."
    },
    "Sexual Assault": {
        "law": "Indian Penal Code",
        "section": "Section 376",
        "advice": "Immediately report to police and seek medical help."
    }
    }
# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    user_text = data["text"].lower()

    # Transform text
    text_vector = vectorizer.transform([user_text])

    # Predict category
    prediction = model.predict(text_vector)
    category = label_encoder.inverse_transform(prediction)[0]
    print("Received text:", user_text)
    print("Predicted category:", category)
    info = legal_info.get(category, {})
    return jsonify({
    "category": category,
    "law": info.get("law"),
    "section": info.get("section"),
    "advice": info.get("advice")
    })


if __name__ == "__main__":
    app.run(debug=True)