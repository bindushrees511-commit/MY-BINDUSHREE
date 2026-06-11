import streamlit as st

# Get query parameters
params = st.query_params

if params:
    age = int(params.get("age", [0])[0])
    Sex_male = int(params.get("Sex_male", [0])[0])
    cigsPerDay = int(params.get("cigsPerDay", [0])[0])
    totChol = int(params.get("totChol", [0])[0])
    sysBP = int(params.get("sysBP", [0])[0])
    glucose = int(params.get("glucose", [0])[0])
    result = int(params.get("result", [0])[0])

    st.title("Prediction Results")
    st.write(f"### Input Details:")
    st.write(f"- Age: {age}")
    st.write(f"- Sex (Male): {'Yes' if Sex_male == 1 else 'No'}")
    st.write(f"- Cigarettes Per Day: {cigsPerDay}")
    st.write(f"- Total Cholesterol: {totChol}")
    st.write(f"- Systolic Blood Pressure: {sysBP}")
    st.write(f"- Glucose Level: {glucose}")

    st.write(f"### Prediction:")
    if result == 1:
        st.error("Heart disease likely detected.")
    else:
        st.success("No heart disease detected.")
else:
    st.warning("No data received. Please use the main page to make predictions.")
