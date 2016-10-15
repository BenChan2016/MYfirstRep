#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 09:44:28 2016

@author: ben
"""
if __name__== '__main__':
    print("<functons.py is beinf run standalone>"+str("\n"))
else: 
    print("<functons.py is imported and being used>"+str("\n"))
    
    

import pandas as pd
from sklearn.linear_model import LinearRegression
import re   #regular expression
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
import time # to measure performance
from sklearn import tree
import pydotplus
from os import system
from sklearn.cross_validation import train_test_split
from sklearn.metrics import median_absolute_error,r2_score, accuracy_score





"User task: Ask user to inputs a file location and return xlxs"
def user_input_file_location():
    usrinput = input(">>> Input: ")
    print("Your file location is "+usrinput)
    return usrinput;
    
"System task: read xlxs and turn it into dataframe"
def system_input_file(usrinput):
    file_extension = detect_file_extension(usrinput)
    
    if(file_extension.lower()=="xlsx"):
        file_input_to_system = pd.read_excel(usrinput)
    if(file_extension.lower()=="csv"):
        file_input_to_system = pd.read_csv(usrinput)
    
    
    print("\n")
    print(file_input_to_system.head())
    return file_input_to_system
    
def detect_file_extension(usrinput):
    file_extension = re.split("\.",usrinput) #get the extension name
    return file_extension[1]


def drop_space_nondigital(df):
    data_frame = df.replace('\s+', np.nan, regex=True)   #http://stackoverflow.com/questions/26837998/pandas-replace-nan-with-blank-empty-string
    data_frame = df.replace('[^\d]', np.nan, regex=True) #change the field to null when the first digital is not digital
    ### You can add the regular expression you like
    return data_frame.dropna()  # drop null
    
        
"Show basic regression_statistic and print it to users" 
def show_regression_statistic(excel_file):
    df_regression = pd.DataFrame(excel_file)
    df_regression = df_regression.drop(df_regression.columns[0],axis=1)
    print("\n")
    print_line()
    print("The means for each column are:" )
    print(df_regression.mean())
    print_line()
    print("The standard deviation for each column are:")
    print(df_regression.std())
    print_line()
    print("The Maximun deviation for each column are:")
    print(df_regression.max())
    print_line()
    print("The Mimnium deviation for each column are:")
    print(df_regression.min())
    print_line()
    
"Build regression model"
def linear_regression(excel_file):
    df = pd.DataFrame(excel_file)
    #print(df)
    #http://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation/31593712#31593712
    Y = df.iloc[:,1]  ##http://stackoverflow.com/questions/11285613/selecting-columns
    #print(Y)
    Xn = df.iloc[:,2:] 
    # print(Xn)
    lr = LinearRegression()  ##http://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame
    lr.fit(Xn, Y)
    return df, lr
    
def print_equation(df, lr):
    print('coef is:  '+str(lr.coef_))
    print('incpt is: '+str(lr.intercept_))
    header_list = df.columns.values
    #print(header_list)  ##http://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    print("\n")
    print("The regression question is:")
    reg_equation = str(header_list[1])+ '='
    for i in range(0,len(lr.coef_)):
        reg_equation += (str(lr.coef_[i]))
        reg_equation += str(header_list[2+i])## 2 because the header_list include Date and y
        reg_equation += ' + '
    reg_equation += str(lr.intercept_)
    print(reg_equation)
    
    
def classification_tree_prediciton_for_training(df,usrinput):
    #http://stackoverflow.com/questions/13730468/from-nd-to-1d-arrays
    #http://stackoverflow.com/questions/7745562/appending-to-2d-lists-in-python
    dfListY = df.iloc[:,1].tolist()
    #dfListX = df.iloc[:,2:].tolist() 
    num_of_row = df.shape[0]
    listy   = [[]]*num_of_row
    for i in range(0,num_of_row):      # turn row into a 2d list
        listy[i] =df.iloc[i,2:].tolist()
        #print(listy[i])
    
    #print(dfListY)
    #print(listy)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(listy,dfListY)
    
    print("")
    Xn_pred = re.split(",", usrinput)     #http://stackoverflow.com/questions/10974932/python-split-string-based-on-regular-expression
    Xn_pred = [float(i) for i in Xn_pred] #float(i) for i in lst]
    #print(Xn_pred)
    reshaped_Xn_pred = np.reshape(Xn_pred,(1,-1)) # need to review the reshape parameter!!!
    predicition = clf.predict(reshaped_Xn_pred)
    return predicition, clf# the following can export a dot file. But at this stage, im
    #not sure how to parse it to png
    #dotfile = open("/home/ben/Desktop/dtree10","w")
    #tree.export_graphviz(clf,out_file = dotfile)
    #dotfile.close()
    #system("-o /home/ben/Desktop/dtree10.png")
    
def classification_tree_prediciton_for_testing (df,clf_fitted):
    #dfListX = df.iloc[:,2:].tolist() 
    num_of_row = df.shape[0]
    listy   = [[]]*num_of_row
    for i in range(0,num_of_row):      # turn testing row into a 2d list
        listy[i] =df.iloc[i,2:].tolist()
        #print(listy[i])
    
    prediciton_testing = clf_fitted.predict(listy) # get prediciton from testing data
    return prediciton_testing
    
    
    
def classification_tree_score(y_true, y_pred ):
    score_normalized = accuracy_score(y_true, y_pred, normalize=True)
    score = accuracy_score(y_true, y_pred, normalize=False)
    return score_normalized, score
    
    
"Show number of null values and print it to users"    
def show_number_of_null_values():
    return
def clean_all_null():
    return

def show_strange_character():
    return
    
def data_frame_split_for_training(df,percentage):
    train, test = train_test_split(df, test_size = float(percentage))
    return train, test
    
    
"Calculate the predicated value Y based on users' input and show the regression question"    
def get_predictor_one_D(linear_equation):
    print('Please enter the Xn in "X1,X2,X3...,Xn" format')
    print("In your case, your n is "+str(len(linear_equation.coef_)))
    usrinput = input(">>> Input: ")
    print("Your input is "+usrinput) 
    Xn_pred = re.split(",", usrinput)     #http://stackoverflow.com/questions/10974932/python-split-string-based-on-regular-expression
    Xn_pred = [float(i) for i in Xn_pred] #float(i) for i in lst]
    #old fashion way: for i in range(0,len(a)) :
    #                     a[i] = float(a[i])
    return Xn_pred
    
def transform_DFpredicition_to_array(data_frame,lr_fitted):
    #turn a dataframe inro 2d list
    num_of_row = data_frame.shape[0]
    listy   = [[]]*num_of_row
    
    for i in range(0,num_of_row):      # turn row into a 2d list
        listy[i] =data_frame.iloc[i,2:].tolist()
        
    prediction_array = make_prediciton_beta(listy,lr_fitted)
    return prediction_array
    
def transform_DFXn_to_2d_array(data_frame):
    num_of_row = data_frame.shape[0]
    listy   = [[]]*num_of_row
    
    for i in range(0,num_of_row):      # turn row into a 2d list
        listy[i] =data_frame.iloc[i,2:].tolist()
    return listy
    
def transform_DFY_to_2d_array(data_frame):
    dfListY = data_frame.iloc[:,1].tolist()
    return dfListY
    
def make_prediciton_beta(Xn_pred,lr_fitted):      # Xn_pred can be a 2d array-like
    array = lr_fitted.predict(Xn_pred)            # the input for predic argument can be 2d array
    return array
    
 
    
"Check which assumption is violated and print it to usrs"
def check_hypothesis():
    return
    
def print_line():
    print("================================================================")
