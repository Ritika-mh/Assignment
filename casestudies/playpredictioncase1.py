import numpy as np
import pandas 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousKNeighborsClassifier():
    filename = 'PlayPredictor.csv'
    field = ['Whether','Temperature']
    Dataset = pandas.read_csv(filename)

    weather = Dataset.Whether
    temp=Dataset.Temperature
    target = Dataset['Play']

    le = preprocessing.LabelEncoder()
    weather_encoded = le.fit_transform(weather)
    print(weather_encoded)

    temp_encoded = le.fit_transform(temp)
    print(temp_encoded)


    target_encoded=le.fit_transform(target)
    print(target_encoded)

    features=list(zip(weather_encoded,temp_encoded))

    Classifier = KNeighborsClassifier(n_neighbors=3)
    Classifier.fit(features, target_encoded)
    Prediction = Classifier.predict([[0,2]])
    return Prediction


def main():
    ret = MarvellousKNeighborsClassifier()
    print("Accuracy by KNeighborsclassifier", ret )


if __name__ == "__main__":
    main()