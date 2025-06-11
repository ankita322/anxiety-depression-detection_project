
import streamlit as st
import joblib

# Load the saved model and vectorizer
model = joblib.load("best_anxiety_depression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Streamlit UI
st.set_page_config(page_title="Mental Health Classifier", layout="centered")

st.markdown("<h1 style='white-space: nowrap;'>🧠 Anxiety and Depression Detection</h1>", unsafe_allow_html=True)
st.markdown("#### _Your AI-powered mental health assistant_")
st.write("This app predicts whether a social media post shows signs of **anxiety/depression**.")

# Input text
user_input = st.text_area("✍️ Enter your post or message here:")

# When the button is clicked
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        features = vectorizer.transform([user_input])
        prediction = model.predict(features)[0]
        result = "Anxiety/Depression 😟" if prediction == 1 else "Normal 😊"
        st.success(f"**Prediction:** {result}")

