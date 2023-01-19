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
    rain_data=pd.read_csv('rainfall in kokan.csv')

    plot_columns = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    for column in plot_columns:
        # Set the size of the figure
        plt.figure(figsize=(10, 6))

        # Plot the column as a bar chart
        rain_data[column].plot(kind='bar')

        # Set the title and labels
        plt.title(column)
        plt.xlabel('months')
        plt.ylabel('rain in mm')

        # Show the plot
    #    plt.show()
    rain_data.plot(y=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'], figsize=(10,5))
    # Add a title and axis labels
    plt.title('Rain in all months')
    plt.xlabel('Months')
    plt.ylabel('Rain in mm')
    # Show the plot
    plt.show()
    x = rain_data.drop("ANNUAL", axis=1)

    y = rain_data["ANNUAL"]

    # step4:Data training
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.5)
    print("xtrain",xtrain)
    print("xtest", xtest)
    print("ytrain", ytrain)
    print("ytest", ytest)
    logmodel = LogisticRegression()

    logmodel.fit(xtrain, ytrain)

    # step4:data test
    prediction = logmodel.predict(xtest)

    # step5:cal Accuracy
    print("Classification report of Logistic Regression is:")
    print(classification_report(ytest, prediction))

    print("confusion matrix of Logistic Regression is:")
    print(confusion_matrix(ytest, prediction))

    print("Accuracy of Logistic Regression is:")
    print(accuracy_score(ytest, prediction))
    
def main():
        print("Marvellous Infosystem by Piyush Khairnar")
        print("Supervised Ml")
        print("Logistic Regression on Titanic data set")

        MarvellousTitanicLogistic()

if __name__=="__main__":
    main()




