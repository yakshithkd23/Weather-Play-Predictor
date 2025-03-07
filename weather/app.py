from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model and label encoders
with open("decision_tree_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("label_encoders.pkl", "rb") as le_file:
    label_encoders = pickle.load(le_file)

# Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get user inputs from the form
        outlook = request.form.get("outlook")
        temp = request.form.get("temp")
        humidity = request.form.get("humidity")
        windy = request.form.get("windy")

        # Check for missing input
        if not outlook or not temp or not humidity or not windy:
            return render_template("index.html", prediction="Error: Missing Input")

        # Convert user input to numerical form
        input_data = np.array([
            label_encoders["Outlook"].transform([outlook])[0],
            label_encoders["Temp"].transform([temp])[0],
            label_encoders["Humidity"].transform([humidity])[0],
            label_encoders["Windy"].transform([windy])[0]
        ]).reshape(1, -1)

        # Predict
        prediction = model.predict(input_data)[0]
        result = "Yes" if prediction == 1 else "No"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
