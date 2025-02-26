# Weather-Play-Predictor
Flask-based web application that predicts whether it's a good idea to play outside based on weather conditions.
Description:
This project is a Flask-based web application that predicts whether it's a good idea to play outside based on weather conditions. It utilizes a Decision Tree Model trained on weather data and takes user inputs such as outlook, temperature, humidity, and wind status to make predictions.

Features:
✅ User-friendly Web Interface 🎨
✅ Machine Learning Model (Decision Tree) 🤖
✅ Real-time Weather Prediction 🌦️
✅ Flask Backend & HTML/CSS Frontend 🌐

Technologies Used:
Python 🐍 (Flask, NumPy, Pickle)
HTML, CSS 🎨 (for UI)
Machine Learning (Decision Tree Classifier)

steps: 
C:\Users\HP\Downloads\weatherplay\
│── app.py  
│── decision_tree_model.pkl  
│── templates\  
│   ├── index.html  
│── static\  
│   ├── css\  
│       ├── styles.css  


What is Decision tree ?

Decison tree is the type of machine learning . it can used for the classification and regression .it will split the data into the different branches based on the feature condition and final calss represent the predicted class or value.

how it works?

The tree is built using a recursive partitioning approach, selecting the best attribute at each step based on Entropy and Information Gain.

📝 note: Recursive partioning approach-is popular predictive modeling techniques.it creates a tree like structure based on data splits. it is simple to interpret using “if-then” rules.Handles classification and regression tasks.Efficient in pattern recognition for medical and data science applications.

formulas:
Entropy (E): Measures data impurity.
E(s)= -(p1*log2(p1)+p2*log2(p2))

p1 and p2 are positive and negative samples

information gain:

IG= E(s)-E(after)

   whereae , E(s)- total value entropy
             E(after)-weigted avaerage entropy
        
  E(after)= ∑ (|Sv|/|s| *E(Sv))
    𝑆
|S|= Total number of instance
|Sv|=number of instance in Sv (example under total, 5 number of rainy is there so it is |Sv| is 5)
sv = subset data value of s(example : weather it may be sunny or rainy entropy value )







References:
https://www.sciencedirect.com/topics/psychology/recursive-partitioning


