import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

data=pd.read_csv('mnist.csv')

df_x=data.iloc[:,1:]#label
df_y=data.iloc[:,0:]#Pixel

x_train,x_test,y_train,y_test=train_test_split(df_y,df_x,test_size=0.2,random_state=4)

obj=DecisionTreeClassifier(__,__,__)
adb=AdaBoostClassifier(obj,n_estimators=__,learning_rate=__)
adb=AdaBoostClassifier(DecisionTreeClassifier(),n_estimators=100,learning_rate=1)
adb.fit(x_train,y_train)

print("Testing accuracy using Bagging classifier:",adb.score(x_test,y_test)*100)
print("Testing accuracy using Bagging classifier:",adb.score(x_train,y_train)*100)