
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

iris=dataset.load_iris()


x=iris.data#label
y=iris.target#Pixel

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

abc=AdaBoostClassifier(n_estimators=100,learning_rate=1)
model=abc.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))