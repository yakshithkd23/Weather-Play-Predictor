from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.DataFrame({
    "Outlook": ["Rainy", "Rainy", "Overcast", "Sunny", "Sunny", "Sunny", "Overcast", "Rainy", "Rainy", "Sunny", "Rainy", "Overcast", "Overcast", "Sunny"],
    "Temp": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Windy": ["False", "True", "False", "False", "False", "True", "True", "False", "False", "False", "True", "True", "False", "True"],
    "Play": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
})

# Encode categorical variables
label_encoders = {}
for col in ["Outlook", "Temp", "Humidity", "Windy", "Play"]:
    label_encoders[col] = LabelEncoder()
    data[col] = label_encoders[col].fit_transform(data[col])

# Split data
X = data.drop("Play", axis=1)
y = data["Play"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train decision tree model
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy on test data
y_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {test_accuracy:.2f}")

# Save model
with open("decision_tree_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

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
