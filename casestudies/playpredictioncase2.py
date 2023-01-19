import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):
    #step 1:Load data
    data=pd.read_csv(data_path,index_col=0)

    print("size of Actual dataset",len(data))

    #step2:clean,prrepare,manipulate data

    features_names=['Whether','Temperature']
    print("Names of features",features_names)

    wheather=data.Whether
    temp=data.Temperature
    play=data.Play

    #creating labelencoder
    le=preprocessing.LabelEncoder()
    #converting string labels into numbers
    wheather_encoded=le.fit_transform(wheather)
    print(wheather_encoded)

    #converting sttring label into number
    temp_encoded=le.fit_transform(temp)
    print(temp_encoded)

    label=le.fit_transform(play)

    #combining weather and temp into single list of tuples
    features=list(zip(wheather_encoded,temp_encoded))

    #step3:Train data
    model=KNeighborsClassifier(n_neighbors=3)

    #Train the model using the training sets
    model.fit(features,label)

    #step4:Test Data
    predicted=model.predict([[0,2]])# 0:overcasting,2:Mild
    print(predicted)

def main():
    print("____Marvellous Infosystem by Piyush Khairnar____")

    print("Machine Learning Application")

    print("Play predictor application using KNeighbors algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__=="__main__":
    main()






