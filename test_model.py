import pickle

model = pickle.load(open("legal_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

while True:
    text = input("Enter text: ")
    text_vector = vectorizer.transform([text.lower()])
    prediction = model.predict(text_vector)
    category = label_encoder.inverse_transform(prediction)[0]
    print("Predicted:", category)