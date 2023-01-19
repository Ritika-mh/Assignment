import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

titanic_data=pd.read_csv('Screen Time Data.csv')

print("First 5 entries from loaded dataset")
print(titanic_data.head())
print("Number of passengers are"+str(len(titanic_data)))
    #step2:Analyze data
print("Visualisation:screen and yoga")
figure()
target="Yoga"
countplot(data=titanic_data,x=target,hue ="Total Screen Time ").set_title("Marvellous Infosystem:Screen n yoga")
show()
#WeekDayx = titanic_data['Week Day']

titanic_data.drop(["Other","Reading and Reference","Date","Entertainment"],axis=1,inplace=True)
print(titanic_data.head(5))
#le = preprocessing.LabelEncoder()
#WeekDayx_encoded = le.fit_transform(WeekDayx)
#print(Alcoholx_encoded)

#a=titanic_data.drop("Yoga",axis=1)
x=titanic_data.drop("Yoga",axis=1)
print("dddd",x)
y=titanic_data["Yoga"]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

logmodel=LogisticRegression()

logmodel.fit(xtrain,ytrain)

    #step4:data test
prediction=logmodel.predict(xtest)

    #step5:cal Accuracy
print("Classification report of Logistic Regression is:")
print(classification_report(ytest,prediction))

print("confusion matrix of Logistic Regression is:")
print(confusion_matrix(ytest,prediction))
print("Accuracy of Logistic Regression is:")
print(accuracy_score(ytest,prediction))

