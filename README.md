\# ⚖️ AI Legal Empowerment System



> \*\*AI-Powered Legal Awareness \& Assistance Platform\*\*



An intelligent legal awareness platform that leverages Artificial Intelligence and Natural Language Processing (NLP) to help users understand potential legal issues from their complaints. The system analyzes user-provided situations, predicts relevant legal categories, and provides applicable laws, legal sections, and basic guidance information.



\*\*Goal:\*\* Make legal awareness more accessible through technology.



\---



\## 🌟 Features



\### 🤖 AI Legal Classification

\- Accepts user complaints in natural language

\- Uses NLP techniques for text analysis

\- Predicts appropriate legal categories using Machine Learning



\### 📚 Legal Guidance System

Provides comprehensive information including:

\- Applicable law information

\- Relevant legal sections

\- Basic legal awareness guidance



\### 🔍 Supported Legal Categories

The system currently supports seven legal categories:

\- \*\*Domestic Violence\*\*

\- \*\*Cyber Crime\*\*

\- \*\*Workplace Harassment\*\*

\- \*\*Dowry Harassment\*\*

\- \*\*Child Abuse\*\*

\- \*\*Stalking / Threat\*\*

\- \*\*Sexual Assault\*\*



\### 🖥️ Responsive User Dashboard

\- Clean and user-friendly interface

\- Dedicated legal issue input section

\- AI prediction result display

\- Emergency helpline information

\- Mobile-responsive design



\---



\## 🔄 Application Workflow



1\. User enters their legal situation or complaint

2\. Frontend dashboard sends input to Flask backend API

3\. Backend processes text using NLP techniques

4\. Machine Learning model analyzes the complaint

5\. System predicts relevant legal category

6\. Application provides related laws, sections, and guidance



\---



\## 🏗️ System Architecture



\### High-Level Architecture

```

&#x20;        User

&#x20;          ↓

&#x20; Frontend Dashboard

&#x20;          ↓

&#x20;     Flask API

&#x20;          ↓

&#x20; NLP Text Processing

&#x20;          ↓

&#x20; Machine Learning Model

&#x20;          ↓

&#x20; Legal Category Prediction

&#x20;          ↓

&#x20; Legal Information Response

```



\### 🧠 Machine Learning Workflow

```

User Legal Complaint

&#x20;       ↓

&#x20; Text Preprocessing

&#x20;       ↓

&#x20; TF-IDF Vectorization

&#x20;       ↓

&#x20; ML Classifier

&#x20;       ↓

&#x20; Category Prediction

&#x20;       ↓

&#x20; Legal Guidance Mapping

```



\---



\## 🛠️ Technology Stack



\### 🎨 Frontend

| Technology | Purpose |

|------------|---------|

| HTML5 | Structure |

| CSS3 | Styling |

| JavaScript | Interactivity |



\### ⚙️ Backend

| Technology | Purpose |

|------------|---------|

| Python | Core language |

| Flask | Web framework |

| Flask-CORS | Cross-origin resource sharing |



\### 🧠 Machine Learning

| Technology | Purpose |

|------------|---------|

| Scikit-learn | ML library |

| NLP | Text analysis |

| TF-IDF Vectorization | Feature extraction |

| ML Classification | Prediction model |



\### 📊 Data Processing

| Technology | Purpose |

|------------|---------|

| Pandas | Data manipulation |

| NumPy | Numerical computing |

| Pickle | Model serialization |



\---



\## 📂 Project Structure



```

AI\_Legal\_Empowerment\_System/

│

├── backend/

│   ├── app.py                    # Flask application

│   ├── legal\_model.pkl           # Trained ML model

│   ├── vectorizer.pkl            # TF-IDF vectorizer

│   └── label\_encoder.pkl         # Label encoder

│

├── frontend/

│   ├── dashboard.html            # Main dashboard

│   ├── login.html                # Login page

│   ├── script.js                 # Frontend logic

│   └── style.css                 # Styling

│

├── ml/

│   ├── train\_classifier.py       # Model training script

│   ├── evaluate\_model.py         # Model evaluation

│   ├── legal\_dataset.csv         # Training dataset

│   └── legal\_dataset.csv.xlsx    # Dataset (Excel format)

│

├── docs/

│   ├── problem\_statement.docx    # Problem documentation

│   ├── technology\_stack.docx     # Tech stack details

│   ├── legal\_categories.docx     # Category definitions

│   └── screenshots/              # Project screenshots

│

├── requirements.txt              # Python dependencies

├── README.md                     # This file

└── .gitignore                    # Git ignore rules

```



\---



\## ⚙️ Installation \& Setup



\### Prerequisites

\- Python 3.8 or higher

\- pip (Python package manager)

\- Modern web browser (Chrome, Firefox, Edge)



\### Step 1: Clone Repository



```bash

git clone https://github.com/ShenbagaDeviB/AI-Legal-Empowerment-System.git



cd AI-Legal-Empowerment-System



\### Step 2: Install Dependencies



```bash

pip install -r requirements.txt

```



\### Step 3: Run Backend Server



```bash

python backend/app.py

```



The backend will start at:



\*\*http://127.0.0.1:5000\*\*



\### Step 4: Run Frontend



Open the following file in your browser:



```

frontend/login.html

```



Your AI Legal Empowerment System is now ready to use!



\---



\## 🔌 API Documentation



\### Predict Legal Category



\*\*Endpoint:\*\* `POST /predict`



\#### Request Format



```json

{

&#x20;   "text": "Someone hacked my social media account and is misusing my private information"

}

{

&#x20;   "category": "Cyber Crime",

&#x20;   "law": "Information Technology Act, 2000",

&#x20;   "section": "Section 66C, 66E",

&#x20;   "advice": "Report this to cyber crime cell and preserve digital evidence."

}

```



\### API Workflow



```

Frontend

&#x20;  ↓

User Complaint Text

&#x20;  ↓

Flask /predict API

&#x20;  ↓

ML Model Prediction

&#x20;  ↓

Legal Guidance Response

```



\---



\## 📸 Project Screenshots



\### 🔐 Login Page



!\[Login Page](docs/screenshots/login-page.png)



\### 🖥️ AI Legal Dashboard



!\[Dashboard](docs/screenshots/dashboard.png)



\### 🔍 AI Prediction Result



!\[Prediction Result](docs/screenshots/prediction-result.png)

\## 📌 Project Status



✅ \*\*Frontend Completed\*\*  

✅ \*\*Responsive Dashboard Implemented\*\*  

✅ \*\*Flask Backend Completed\*\*  

✅ \*\*Machine Learning Model Integrated\*\*  

✅ \*\*Legal Prediction API Working\*\*  

✅ \*\*Legal Guidance Mapping Implemented\*\*  



\---



\---



\## 🎯 Project Objective



The main objective of this project is to develop an AI-based legal awareness system that helps users identify possible legal categories from their complaints.



The system uses Machine Learning and Natural Language Processing (NLP) techniques to analyze user inputs and provide basic legal information, applicable laws, and awareness-based guidance.



This project aims to improve access to legal awareness through technology.



\## 🚀 Future Enhancements



\- \*\*Real user authentication system\*\* - Secure login and user management

\- \*\*Voice-based legal assistant\*\* - Speech-to-text complaint input

\- \*\*Multilingual support\*\* - Tamil, English, and other regional languages

\- \*\*AI chatbot conversation mode\*\* - Interactive dialogue-based assistance

\- \*\*Mobile application development\*\* - Native iOS and Android apps

\- \*\*Advocate connection platform\*\* - Direct lawyer consultation feature

\- \*\*Real-time legal updates\*\* - Latest law amendments and notifications

\- \*\*Improved ML accuracy\*\* - Training with larger, diverse datasets



\---



\## ⚠️ Disclaimer



> \*\*Important Notice:\*\* This project provides AI-based legal awareness and information support only. It is designed to help users understand possible legal categories and available information. \*\*It does not replace professional legal consultation from qualified legal professionals.\*\* For serious legal matters, always consult a licensed attorney.



\---



\## 📄 License



This project is open-source and available for educational and non-commercial purposes.



\---



\## 👩‍💻 Developer



\*\*Shenbaga Devi\*\*  

\*AI \& Machine Learning Enthusiast\*



\- \*\*GitHub:\*\* \[@ShenbagaDeviB](https://github.com/ShenbagaDeviB)

\- \*\*Project Repository:\*\* \[AI-Legal-Empowerment-System](https://github.com/ShenbagaDeviB/AI-Legal-Empowerment-System)



\---



\## 🤝 Contributing



Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.



\---



\## 📧 Contact



For questions, suggestions, or collaborations, please reach out through the GitHub repository or create an issue.



\---



\*\*Last Updated:\*\* July 2026

```



\*\*\*

