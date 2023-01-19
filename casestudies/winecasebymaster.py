from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    #load dataset
    wine=datasets.load_wine()

    #print the name of featurs
    print(wine.feature_names)

    #print the label species(class_0,class_1,class_2)
    print(wine.target_names)

    #print the wine data(top 5 records)
    print(wine.data[0:5])

    #print the wine labels(0:class_0,1:class_1,2:class_2)
    print(wine.target)

    #split dataset into training set and test set
    x_train,x_test,y_train,y_test=train_test_split(wine.data,wine.target,test_size=0.3)#70% training and 30% testing data split

    #creat KNN classifier
    knn=KNeighborsClassifier(n_neighbors=3)

    #Train the model using the training sets
    knn.fit(x_train,y_train)

    #predict the response for test dataset
    y_pred=knn.predict(x_test)

    #model Accuracy,how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test,y_pred))


def main():
    print("Marvellous Infosystem by piyush khairnar")
    print("Wine predictor application using K Nearest Knighbor algorithm")

    WinePredictor()
if __name__=="__main__":
    main()






