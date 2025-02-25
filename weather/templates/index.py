<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Play Predictor</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <div class="container">
        <h1 style="color: darkblue;">Weather Play Predictor</h1>
        <p>Enter weather conditions to predict if playing outside is a good idea.</p>
        
        <form action="/predict" method="post">
            <label for="outlook">Outlook:</label>
            <select name="outlook" id="outlook">
                <option value="Sunny">Sunny</option>
                <option value="Overcast">Overcast</option>
                <option value="Rainy">Rainy</option>
            </select>

            <label for="temp">Temperature:</label>
            <select name="temp" id="temp">
                <option value="Hot">Hot</option>
                <option value="Mild">Mild</option>
                <option value="Cool">Cool</option>
            </select>

            <label for="humidity">Humidity:</label>
            <select name="humidity" id="humidity">
                <option value="High">High</option>
                <option value="Normal">Normal</option>
            </select>

            <label for="windy">Windy:</label>
            <select name="windy" id="windy">
                <option value="False">No</option>
                <option value="True">Yes</option>
            </select>

            <button type="submit">Predict</button>
        </form>

        {% if prediction %}
            <div class="result">
                <h2>Prediction: {{ prediction }}</h2>
            </div>
        {% endif %}
    </div>
</body>
</html>
