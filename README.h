**# Weather-Play-Predictor**
Flask-based web application that predicts whether it's a good idea to play outside based on weather conditions.
**Description:**
This project is a Flask-based web application that predicts whether it's a good idea to play outside based on weather conditions. It utilizes a Decision Tree Model trained on weather data and takes user inputs such as outlook, temperature, humidity, and wind status to make predictions.

**Features:**
✅ User-friendly Web Interface 🎨
✅ Machine Learning Model (Decision Tree) 🤖
✅ Real-time Weather Prediction 🌦️
✅ Flask Backend & HTML/CSS Frontend 🌐

**Technologies Used:**
Python 🐍 (Flask, NumPy, Pickle)  
HTML, CSS 🎨 (for UI)
Machine Learning (Decision Tree Classifier)


***What is Decision tree ?***

Decison tree is the type of machine learning . it can used for the classification and regression .it will split the data into the different branches based on the feature condition and final calss represent the predicted class or value.

**how it works?**

The tree is built using a recursive partitioning approach, selecting the best attribute at each step based on Entropy and Information Gain.

📝 note: Recursive partioning approach-is popular predictive modeling techniques.it creates a tree like structure based on data splits. it is simple to interpret using “if-then” rules.Handles classification and regression tasks.Efficient in pattern recognition for medical and data science applications.

Mathematical Calculation for Decision Tree Construction (ID3 Algorithm

**formulas:**
Entropy (E): Measures data impurity.
E(s)= -(p1*log2(p1)+p2*log2(p2))  .....equ(1)

p1 and p2 are positive and negative samples

information gain:

IG= E(s)-E(after)   ......equ(2)

   whereae , E(s)- total value entropy
             E(after)-weigted avaerage entropy
        
  E(after)= ∑ (|Sv|/|s| *E(Sv))   ......equ(3)
    𝑆
|S|= Total number of instance
|Sv|=number of instance in Sv (example under total, 5 number of rainy is there so it is |Sv| is 5)
sv = subset data value of s(example : weather it may be sunny or rainy entropy value )



**Example: Play cricket  Decision Tree**



| Day  | Outlook  | Temperature | Humidity | Windy  | Play |
|------|---------|------------|----------|--------|------|
| D1   | Rainy   | Hot        | High     | False  | No   |
| D2   | Rainy   | Hot        | High     | True   | No   |
| D3   | Overcast| Hot        | High     | False  | Yes  |
| D4   | Sunny   | Mild       | High     | False  | Yes  |
| D5   | Sunny   | Cool       | Normal   | False  | Yes  |
| D6   | Sunny   | Cool       | Normal   | True   | No   |
| D7   | Overcast| Cool       | Normal   | True   | Yes  |
| D8   | Rainy   | Mild       | High     | False  | No   |
| D9   | Rainy   | Cool       | Normal   | False  | Yes  |
| D10  | Sunny   | Mild       | Normal   | False  | Yes  |
| D11  | Rainy   | Mild       | Normal   | True   | Yes  |
| D12  | Overcast| Mild       | High     | True   | Yes  |
| D13  | Overcast| Hot        | Normal   | False  | Yes  |
| D14  | Sunny   | Mild       | High     | True   | No   |


step 1: Compute Entropy of the Whole Dataset  by using equation  1 
                    p+=9/14
                    p-=5/14
 so ,E(S)=0.940

 step 2: compute entropy for each attribute.
1. Entropy of Outlook
Outlook has 3 possible values: Sunny, Overcast, Rainy
   
| Outlook  | Play Yes | Play No | Total |
|----------|---------|---------|-------|
| Sunny    | 2       | 3       | 5     | 
| Overcast | 4       | 0       | 4     | 
| Rainy    | 3       | 2       | 5     | 
      
by applying equation 1 you will get entropy of sunny, overcast,rainy as 0.971,0,0.971
  after these apply equation 3 
    so, E(After) is  0.692
apply equation 2 :
        IG(weather)=0.247
           
2. Entropy of Humidity

| Humidity | Play Yes | Play No | Total |
|----------|---------|---------|-------|
| High     | 3       | 4       | 7     | 
| Normal   | 6       | 1       | 7     |  

   Entropy is 0.985 and 0.592 
     E(After) =0.789
     IG(humidity)=0.151
3. Entropy of Windy
| windy    | Play Yes | Play No | Total |
|----------|---------|---------|-------|
| True     | 3       | 3       | 6     | 
| Normal   | 6       | 2       | 8     | 
   Entropy is 1.0 and 0.811
     E(After) =0.891
     IG(windy)=0.049
4. Entropy of Temperature
|Tempara   | Play Yes | Play No | Total |
|----------|---------|---------|-------|
| hot    | 2       | 2       | 4     | 
| mild   | 4       | 2       | 6     | 
| cool   | 3       | 1       | 4     | 

    Entropy is 1.0 and 0.918
     E(After) =0.91
     IG(temp)=0.029

Step 3: Choosing the Best Attribute

Outlook has the highest Information Gain (0.247), we split the dataset based on Outlook first.

   Step 4: Constructing the Decision Tree

        Outlook
       /   |    \
  Sunny Overcast  Rainy
   /    \     |      /    \
Humidity No  Yes  Windy  Yes
 /    \        /     \
High Normal  False  True
 No    Yes    Yes    No

1.If Outlook = Overcast → Play = Yes
2.If Outlook = Sunny:
    If Humidity = High → Play = No
    If Humidity = Normal → Play = Yes
3.If Outlook = Rainy:
     If Windy = False → Play = Yes
     If Windy = True → Play = No

*** performance evaluation:***
   
Decision tree used for classification tasks, but their performance need to be ensure properly that's why performance mease
   is came in picture i.e recall , precision, accuracy

   1.Recall(sensitivity)- measure how well we find all positive cases

      Recall =TP/TP+FN
      TP= True positive
      FN= False negative
NOTE:
     actual    prediction 
      1         0            FN
      0          1           FP
      0          0            TN
      1           1            TP
   2. Precision
Measures how many predicted positives are actually correct.

  precision= TP/TP+FP
️3. Accuracy
Measures overall correctness (both positives & negatives).
   Accuracy= TP+TN/TP+TN+FP+FN
******

| Day  | Actual (Play?) | Predicted (Play?) | Category |
|------|--------------|------------------|----------|
| D1   | No           | No               | TN ✅    |
| D2   | No           | No               | TN ✅    |
| D3   | Yes          | Yes              | TP ✅    |
| D4   | Yes          | Yes              | TP ✅    |
| D5   | Yes          | Yes              | TP ✅    |
| D6   | No           | Yes              | FP ❌    |
| D7   | Yes          | Yes              | TP ✅    |
| D8   | No           | No               | TN ✅    |
| D9   | Yes          | Yes              | TP ✅    |
| D10  | Yes          | Yes              | TP ✅    |
| D11  | Yes          | Yes              | TP ✅    |
| D12  | Yes          | Yes              | TP ✅    |
| D13  | Yes          | No               | FN ❌    |
| D14  | No           | No               | TN ✅    |

Final Results
Recall = 0.8889 (88.89%)
Precision = 0.8889 (88.89%)
Accuracy = 0.8571 (85.71%)





References:
https://www.sciencedirect.com/topics/psychology/recursive-partitioning
https://leetcode.com/explore/learn/card/decision-tree/501/evaluation/2638/


