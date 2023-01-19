from sklearn import tree
Featurs=[[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]
Lables=["Tennies","Tennies","cricket","Tennies","cricket","Tennies","cricket","Tennies","Tennies","Tennies","cricket","Tennies","cricket","Tennies","cricket"]
obj=tree.DecisionTreeClassifier()
obj=obj.fit(Featurs,Lables)
print(obj.predict([[97,"Smooth"]]))