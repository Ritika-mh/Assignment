import numpy as np
import pandas
from sklearn import tree
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousKNeighborsClassifier(data_trainx, data_testx, target_trainx, target_testx ):

    Classifier = KNeighborsClassifier(n_neighbors=3)
    Classifier.fit(data_trainx, target_trainx)
    Prediction = Classifier.predict(data_testx)
    Accuracy = accuracy_score(target_testx, Prediction)
    return Accuracy
def MarvellousCalculateAccuracyDecisionTree(data_trainx, data_testx, target_trainx, target_testx):

    classifier=tree.DecisionTreeClassifier()
    classifier.fit(data_trainx,target_trainx)

    prediction=classifier.predict(data_testx)

    Accuracy=accuracy_score(target_testx,prediction)

    return Accuracy

def main():
    filename = 'Marvellouswine.csv'
    field = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
             'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
             'Proline']

    Dataset = pandas.read_csv(filename)

    Alcoholx = Dataset.Alcohol
    Malicacidx = Dataset['Malic acid']
    Ashx = Dataset.Ash
    Alcalinityofashx = Dataset['Alcalinity of ash']
    Magnesiumx = Dataset['Magnesium']
    Totalphenolsx = Dataset['Total phenols']
    Flavanoidsx = Dataset['Flavanoids']
    Nonflavanoidphenolsx = Dataset['Nonflavanoid phenols']
    Proanthocyaninsx = Dataset['Proanthocyanins']
    Colorintensityx = Dataset['Color intensity']
    Huex = Dataset.Hue
    OD280OD315ofdilutedwinesx = Dataset['OD280/OD315 of diluted wines']
    Prolinex = Dataset.Proline

    target = Dataset['Class']

    le = preprocessing.LabelEncoder()
    Alcoholx_encoded = le.fit_transform(Alcoholx)
    #print(Alcoholx_encoded)

    Malicacidx_encoded = le.fit_transform(Malicacidx)
    #print(Malicacidx_encoded)

    Ashx_encoded = le.fit_transform(Ashx)
    #print(Ashx_encoded)

    Alcalinityofashx_encoded = le.fit_transform(Alcalinityofashx)
    #print(Alcalinityofashx_encoded)

    Magnesiumx_encoded = le.fit_transform(Magnesiumx)
    #print(Magnesiumx_encoded)

    Proanthocyaninsx_encoded = le.fit_transform(Proanthocyaninsx)
    #print(Proanthocyaninsx_encoded)

    Totalphenolsx_encoded = le.fit_transform(Totalphenolsx)
    #print(Totalphenolsx_encoded)

    Flavanoidsx_encoded = le.fit_transform(Flavanoidsx)
    #print(Flavanoidsx_encoded)

    Nonflavanoidphenolsx_encoded = le.fit_transform(Nonflavanoidphenolsx)
    #print(Nonflavanoidphenolsx_encoded)

    Colorintensityx_encoded = le.fit_transform(Colorintensityx)
    #print(Colorintensityx_encoded)

    Huex_encoded = le.fit_transform(Huex)
    #print(Huex_encoded)

    OD280OD315ofdilutedwinesx_encoded = le.fit_transform(OD280OD315ofdilutedwinesx)
    #print(OD280OD315ofdilutedwinesx_encoded)

    Prolinex_encoded = le.fit_transform(Prolinex)
    #print(Prolinex_encoded)

    target_encoded = le.fit_transform(target)
    #print(target_encoded)

    features = list(zip(Alcoholx_encoded, Malicacidx_encoded, Ashx_encoded, Alcalinityofashx_encoded, Magnesiumx_encoded,Proanthocyaninsx_encoded, Totalphenolsx_encoded, Flavanoidsx_encoded, Nonflavanoidphenolsx_encoded,Colorintensityx_encoded, Huex_encoded, OD280OD315ofdilutedwinesx_encoded, Prolinex_encoded))

    data_train, data_test, target_train, target_test = train_test_split(features, target_encoded, test_size=2/3)

    ret=MarvellousKNeighborsClassifier(data_train, data_test, target_train, target_test )
    print("Accuracy of classification algorithm with K Neighbore classifier is:", ret*100,'%' )

    print("_______________")

    Accuracy = MarvellousCalculateAccuracyDecisionTree(data_train, data_test, target_train, target_test)
    print("Accuracy of classification algorithm with Dicision Tree classifier is: ", Accuracy * 100, "%")

if __name__ == "__main__":
    main()