import streamlit as st
import joblib

# Load the trained decision tree model
model = joblib.load("decision_tree_model.pkl")

# App title
st.title("Weather Play Predictor")
st.write("Enter the weather conditions to predict if you should play:")

# User inputs
outlook = st.selectbox("Outlook", ["sunny", "overcast", "rainy"])
temp = st.selectbox("Temperature", ["hot", "mild", "cool"])
humidity = st.selectbox("Humidity", ["high", "normal"])
windy = st.selectbox("Windy", ["true", "false"])

# Convert categorical inputs to same format as training data
# You may need to one-hot encode or label-encode these depending on how model was trained
input_data = [[outlook, temp, humidity, windy]]

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Play' if prediction[0] == 'yes' else 'Don\'t Play'}")
