from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
def eud(a,b):
    return distance.euclidean(a,b)
class MarvellousKNeighborsClassifier :
    def fit(self,trainingdata,trainingtarget):
        self.TrainingData=trainingdata
        self.TrainingTarget=trainingtarget

    def closest(self,row):
        minimumdistance=eud(row,self.TrainingData[0])
        minimumindex=0

        for i in range(1,(len(self.TrainingData))):
            Distance=eud(row,(self.TrainingData[i]))
            if Distance<minimumdistance:
                minimumdistance=Distance
                minimumindex=i

        return self.TrainingTarget[minimumindex]

    def predict(self,TestData):
        predictions=[]
        for value in TestData:
            result=self.closest(value)
            predictions.append(result)
        return predictions


def MarvellousML():

    Dataset = load_iris()  # load data

    data = Dataset.data
    target = Dataset.target
    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.5)
    Classifier = MarvellousKNeighborsClassifier()
    Classifier.fit(data_train, target_train)
    Prediction = Classifier.predict(data_test)
    Accuracy = accuracy_score(target_test, Prediction)
    return Accuracy


def main():
    ret = MarvellousML()
    print("Accuracy by KNeighborsclassifier", ret * 100, "% ")


if __name__ == "__main__":
    main()