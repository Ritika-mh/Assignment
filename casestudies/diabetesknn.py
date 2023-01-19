import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


#simplefilter(action='ignore',category=FutureWarning)

print("Marvellous Infosystem by Piyush Khairnar")
print("Diabetes using Random Forest")

diabetes=pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data: {}".format(diabetes.shape))

x_train,x_test,y_train,y_test=train_test_split(diabetes.loc[:,diabetes.columns!='Outcome'],diabetes['Outcome'],stratify=diabetes['Outcome'],random_state=66)

training_accuracy=[]
test_accuracy=[]


#try neighbors 1 to 10
neighbores_setting=range(1,11)

for n_neighbors1 in neighbores_setting:
    knn=KNeighborsClassifier(n_neighbors=n_neighbors1)
    knn.fit(x_train,y_train)
    #training accuracy
    training_accuracy.append(knn.score(x_train,y_train))
    #test accuracy
    test_accuracy.append(knn.score(x_test,y_test))

plt.plot(neighbores_setting,training_accuracy,label="training accuracy")
plt.plot(neighbores_setting,test_accuracy,label="testing accuracy")
plt.xlabel("n_neighbors")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig('knn_compare_model')
plt.show()

knn=KNeighborsClassifier(n_neighbors=9)
knn.fit(x_train,y_train)

print("Accuracy on training set:{:.2f}".format(knn.score(x_train,y_train)))
print("Accuracy on test set:{:.2f}".format(knn.score(x_test,y_test)))
