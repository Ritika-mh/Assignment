import numpy as np
import pandas 
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier():
    filename = 'PlayPredictor.csv'
    field = ['Whether','Temperature']
    Dataset = pandas.read_csv(filename)

    weather = Dataset.Whether
    temp=Dataset.Temperature
    data=Dataset[field]
    target = Dataset['Play']

    le = preprocessing.LabelEncoder()
    weather_encoded = le.fit_transform(weather)
    print(weather_encoded)

    temp_encoded = le.fit_transform(temp)
    print(temp_encoded)


    target_encoded=le.fit_transform(target)
    print(target_encoded)

    features=list(zip(weather_encoded,temp_encoded))

    data_train, data_test, target_train, target_test = train_test_split(features, target_encoded, test_size=0.5)

    Classifier = KNeighborsClassifier(n_neighbors=3)
    Classifier.fit(data_train,target_train)
    Prediction = Classifier.predict(data_test)
    Accuracy = accuracy_score(target_test, Prediction)
    return Accuracy


def main():
    ret = MarvellousKNeighborsClassifier()
    print("Accuracy by KNeighborsclassifier", ret*100,"%" )


if __name__ == "__main__":
    main()