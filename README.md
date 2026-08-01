**⚖️ AI Legal Empowerment System
**
AI-Powered Legal Awareness & Assistance Platform

An intelligent legal awareness platform that uses Artificial Intelligence (AI) and Natural Language Processing (NLP) to help users understand potential legal issues from their complaints.

The system analyzes user-provided situations, predicts relevant legal categories, and provides applicable laws, legal sections, and basic legal awareness guidance.

Goal: Make legal awareness more accessible through technology.

**🌟 Features**

🤖 AI Legal Classification

Accepts user complaints in natural language

Uses NLP techniques for text analysis

Predicts appropriate legal categories using Machine Learning

📚 Legal Guidance System

Applicable law information

Relevant legal sections

Basic legal awareness guidance

🔍 Supported Legal Categories

Domestic Violence

Cyber Crime

Workplace Harassment

Dowry Harassment

Child Abuse

Stalking / Threat

Sexual Assault

🖥️ Responsive User Dashboard

Clean and user-friendly interface

Legal issue input section

AI prediction result display

Emergency helpline information

Mobile responsive design

🔄 Application Workflow

User enters their legal complaint.

Frontend sends the complaint to the Flask API.

NLP preprocessing is performed.

The Machine Learning model predicts the legal category.

The system returns legal guidance.

🏗️ System Architecture

User
  |
  v
Frontend
  |
  v
Flask API
  |
  v
NLP Processing
  |
  v
ML Model
  |
  v
Prediction
  |
  v
Legal Guidance

🛠️ Technology Stack

Layer

Technologies

Frontend

HTML5, CSS3, JavaScript

Backend

Python, Flask, Flask-CORS

ML

Scikit-learn, NLP, TF-IDF

Data

Pandas, NumPy, Pickle

📂 Project Structure

AI_Legal_Empowerment_System/
├── backend/
├── frontend/
├── ml/
├── docs/
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation

git clone https://github.com/ShenbagaDeviB/AI-Legal-Empowerment-System.git
cd AI-Legal-Empowerment-System
pip install -r requirements.txt
python backend/app.py

Open frontend/login.html in your browser.

🔌 API

POST /predict

Request:

{
  "text": "Someone hacked my account"
}

Response:

{
  "category":"Cyber Crime",
  "law":"Information Technology Act, 2000",
  "section":"66C, 66E",
  "advice":"Report to cyber crime cell."
}

📌 Project Status

Frontend Completed

Backend Completed

ML Model Integrated

API Working

🚀 Future Enhancements

Authentication

Voice Assistant

Multilingual Support

AI Chatbot

Mobile App

Advocate Platform

⚠️ Disclaimer

This project is intended for legal awareness only and does not replace professional legal advice.

👩‍💻 Developer

Shenbaga Devi
