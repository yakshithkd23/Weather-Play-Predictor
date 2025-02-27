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


What is Decision tree ?

Decison tree is the type of machine learning . it can used for the classification and regression .it will split the data into the different branches based on the feature condition and final calss represent the predicted class or value.

how it works?

The tree is built using a recursive partitioning approach, selecting the best attribute at each step based on Entropy and Information Gain.

📝 note: Recursive partioning approach-is popular predictive modeling techniques.it creates a tree like structure based on data splits. it is simple to interpret using “if-then” rules.Handles classification and regression tasks.Efficient in pattern recognition for medical and data science applications.

formulas:
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

Example: Play Tennis Decision Tree

 
ID	Weather	Windy	Play Tennis
1	Sunny 	Yes	No
2	Sunny   	No	   No
3	Overcast	 Yes	Yes
4	Rainy	    Yes	Yes
5	Rainy     No	  Yes
6	Overcast 	No 	Yes

step 1: Compute Entropy of the Whole Dataset  by using equation  1 
                    p+=4/6
                    p-=2/6
 so ,E(S)=0.91

 step 2: compute entropy for weather attribute.
 Weather	Yes (Play)	No (Play)	Total
Sunny	     0	         2	        2
Overcast	   2	         0	        2
Rainy    	2	         0	        2
      
by applying equation 1 you will get entropy of sunny, overcast,rainy as 0,0,0
  after these apply equation 3 
    so, E(After) is also 0

step 3:  Compute Information Gain for Weather
        apply equation 2 
        so IG(weather)=0.91
        
Since IG(Weather) is high, it is a good splitting attribute.

Step 4: Compute Information Gain for Wind
Windy	Yes (Play)	No (Play)	Total
Yes      	2     	2	       4
No	         2	      0	       2

Entropy for windy =Yes:
    E(yes)=1
Entropy for windy =No:
   E(no)=0
 information gain is   0.24

 step 5: Choose the best attribute
 IG(weather)=0.91
 IG(windy)=0.24 
 Since Weather has the highest IG (0.91), it is chosen as the root node for the decision tree.
      Weather
     /   |   \
 Sunny  Overcast  Rainy
  |       |       |
  No     Yes      Yes

    
References:
https://www.sciencedirect.com/topics/psychology/recursive-partitioning


