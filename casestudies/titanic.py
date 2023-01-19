import math
import numpy as np
import pandas as pd
import seaborn as sns
from seaborn import countplot
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def MarvellousTitanicLogistic():
    #step1:Load data
    titanic_data=pd.read_csv('MarvellousTitanicDataset.csv')

    print("First 5 entries from loaded dataset")
    print(titanic_data.head())

    print("Number of passengers are"+str(len(titanic_data)))

    #step2:Analyze data
    print("Visualisation:Survived and non survived passengers")
    figure()
    target="Survived"

    countplot(data=titanic_data,x=target,hue ="Sex").set_title("Marvellous Infosystem:Survived and non survived passenger")
    show()

    print("Visualisation:Survived and non survived passenger based on gender")
    figure()
    target="Survived"

    countplot(data=titanic_data, x=target, hue="Sex").set_title(
        "Marvellous Infosystem:Survived and non survived passenger based on gender")
    show()

    print("Visualisation:Survived and non survived passenger based on the Passenger class")
    figure()
    target="Survived"

    countplot(data=titanic_data, x=target, hue="Sex").set_title("Marvellous Infosystem:Survived and non survived passenger based on Passenger class")
    show()

    print("Visualisation:Survived and non survived passenger based on the Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Marvellous Infosystem :Survived and non survived passenger based  on Age")
    show()

    print("Visualisation:Survived and non survived passenger based on fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Marvellous Infosystem :Survived and non survived passenger based  on Fare")
    show()

    #spet3: Data cleaning
    titanic_data.drop("zero",axis=1,inplace=True)

    print("First 5 entris from loade dataset after removing zero column")
    print(titanic_data.head())

    print("Value of sex colunm")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Value of Sex column after removing one field")
    Sex=pd.get_dummies(titanic_data["Sex"],drop_first=True)
    print(Sex.head(5))

    print("Value of Pclass column after removing one field")
    Pclass=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
    print(Pclass.head(5))

    print("Values of dataset after concatenating new columns")
    titanic_data=pd.concat([titanic_data,Sex,Pclass],axis=1)
    print(titanic_data.head(5))

    print("Values of data set after removing irrelevent columns")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"],axis=1,inplace=True)
    print(titanic_data.head(5))

    x=titanic_data.drop("Survived",axis=1)
    print("dddd",x)
    y=titanic_data["Survived"]

    #step4:Data training
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

def main():
        print("Marvellous Infosystem by Piyush Khairnar")
        print("Supervised Ml")
        print("Logistic Regression on Titanic data set")

        MarvellousTitanicLogistic()

if __name__=="__main__":
    main()




