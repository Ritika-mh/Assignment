####################################
#Requred python packages
###################################
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
####################################
#Files path
###################################
input_path="breast-cancer-wisconsin.data"
output_path="breast-cancer-wisconsin.csv"
####################################
#Headers
###################################
Headers=["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"
]

####################################
#Function name:read_data
#Description:Read the data into pandas dataframe
#input:path of csv
#output:Gives the data#
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def read_data(path):
    data=pd.read_csv(path)
    return data
####################################
#Function name:get_headers
#Description:Dataset headers
#input:dataset
#output:Return headers
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def get_headers(dataset):
    return dataset.column.values
####################################
#Function name:add_headers
#Description:Add headers to the dataset
#input:dataset
#output:update headers
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def add_headers(dataset,headers):
    dataset.column=headers
    return dataset
####################################
#Function name:data_file_to_csv
#input:nothing
#output:write data to csv
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def data_file_to_csv():
    #Headers
    headers=["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape","MarginalAdhesion","SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses","CancerType"
]
    #load data into pandas datafrrame
    dataset=read_data(input_path)
    #Add headers to loaded dataset
    dataset=add_headers(dataset,headers)
    #save loaded dataset into csv format
    dataset_to_csv(output_path,index=False)
    print("File saved..!")
####################################
#Function name:split the dataset
#Description:split data set into training percentage
#input:Dataset with related information
#output:write data after splitting
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def split_dataset(dataset,train_percentage,feature_header,target_header):
    #split data into train and test dataset
    x_train,x_test,y_train,y_test=train_test_split(dataset[feature_header],dataset[target_header],train_size=train_percentage)
    return x_train,x_test,y_train,y_test
####################################
#Function name:handle_missing_values
#Description:Filter missing value from dataset
#input:Dataset with missing value
#output:Dataset by remocing missing values
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def handle_missing_values(dataset,missing_value_header,missing_label):
    return dataset[dataset[missing_value_header]!=missing_label]
####################################
#Function name:random_forest_classifier
#Description:To train the random forest classifier with features and target data
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def random_forest_classifier(features,target):
    clf=RandomForestClassifier()
    clf.fit(features,target)
    return clf
####################################
#Function name:dataset_statistics
#Description:Basic statistics of dataset
#input:Dataset
#output:Discription of Dataset
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def dataset_statistics(dataset):
    print(dataset.describe())
####################################
#Function name:main
#Description:main function from where execution starts
#Author:Piyush manohar khairnar
#Date:1/02/2022
###################################
def main():
    #load the csv file into pandas dataframe
    dataset=pd.read_csv(output_path)
    # get Basic statistics of dataset
    dataset_statistics(dataset)
    #filter missing values
    dataset=handle_missing_values(dataset,Headers[6],'?')
    x_train,x_test,y_train,y_test=split_dataset(dataset,0.7,Headers[1:-1],Headers[-1])

    #Train and Test size details
    print("X_train_shape",x_train.shape)
    print("Y_train_shape", y_train.shape)
    print("X_test_shape",x_test.shape)
    print("Y_test_shape",y_test.shape)

    #Creat Random forest classifier instance
    trained_model=random_forest_classifier(x_train,y_train)
    print("Trained model::",trained_model)
    prediction=trained_model.predict(x_test)

    for i in range(0,205):
        print("Actual outcome::{} and Predicted outcome::{} ".format(list(y_test)[i],prediction[i]))
    print("Train Accuracy::",accuracy_score(y_train,trained_model.predict(x_train)))
    print("Test Accuracy::",accuracy_score(y_test,prediction))
    print("Confusion matrics::",confusion_matrix(y_test,prediction))

#########################
#Application stater
########################
if __name__=="__main__":
    main()
