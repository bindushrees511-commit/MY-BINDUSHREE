import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_note_authentication(age, Sex_male, cigsPerDay, totChol, sysBP, glucose):
    """
    Predicts the likelihood of heart disease using a trained classifier.
    """
    prediction = classifier.predict([[age, Sex_male, cigsPerDay, totChol, sysBP, glucose]])
    return prediction[0]

# Main App
st.title("Heart Disease Prediction")

# Custom CSS 
st.markdown(
    f"""
    <style>
    .stApp {{
            body::before 
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background-color: rgba(255, 255, 255, 0.5); /* White overlay with 50% transparency */
                z-index: -1;
            
            .content 
                position: relative; /* Ensures the content is above the overlay */
                z-index: 2;
                text-align: center;
                color: red;
                text-shadow: 1px 1px 2px black;
                background: rgba(255, 255, 255, 0.8); /* Optional: Semi-transparent background for text */
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            
    }}
    </style>
    """, unsafe_allow_html=True
)

# Input fields with validation
age = st.number_input("Age", min_value=1, max_value=120, step=1, value=30)
Sex_male = st.selectbox("Sex", options=[("Female", 0), ("Male", 1)], format_func=lambda x: x[0])[1]
cigsPerDay = st.number_input("Cigarettes Per Day", min_value=0, step=1, value=0)
totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=0, value=200)
sysBP = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, value=120)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, value=100)

if st.button("Predict"):
    # Perform prediction
    prediction = predict_note_authentication(age, Sex_male, cigsPerDay, totChol, sysBP, glucose)
    
    # Pass result and inputs to the results page as query parameters
    query_params = {
        "age": age,
        "Sex_male": Sex_male,
        "cigsPerDay": cigsPerDay,
        "totChol": totChol,
        "sysBP": sysBP,
        "glucose": glucose,
        "result": prediction
    }

    # Generate a link to the results page with query parameters
    query_string = "&".join([f"{key}={value}" for key, value in query_params.items()])
    results_page_url = f"/Result_Page?{query_string}"
    
    # Display the link to the user
    st.write(f"### Click below to view the results:")
    st.write(f"[Go to Results]({results_page_url})")

if st.button("About"):
    st.text("This project predicts heart disease likelihood using machine learning.")
