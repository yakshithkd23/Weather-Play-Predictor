import streamlit as st
import joblib

# Load model
model = joblib.load("weather/decision_tree_model.pkl")

st.title("🌦️ Weather Play Predictor")
st.write("Enter the weather conditions to predict if you should play.")

# User Inputs
outlook = st.selectbox("Outlook", ["sunny", "overcast", "rainy"])
temp = st.selectbox("Temperature", ["hot", "mild", "cool"])
humidity = st.selectbox("Humidity", ["high", "normal"])
windy = st.selectbox("Windy", ["true", "false"])

# Manual label encoding (must match your training encoding)
outlook_map = {"sunny": 0, "overcast": 1, "rainy": 2}
temp_map = {"hot": 0, "mild": 1, "cool": 2}
humidity_map = {"high": 0, "normal": 1}
windy_map = {"false": 0, "true": 1}

# Encode input
input_data = [[
    outlook_map[outlook],
    temp_map[temp],
    humidity_map[humidity],
    windy_map[windy]
]]

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = "✅ Play" if prediction[0] == "yes" else "❌ Don't Play"
    st.success(f"Prediction: {result}")
