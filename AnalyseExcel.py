# -*- coding: utf-8 -*-

import pandas as pd
import sys
import xlrd
import csv
from sklearn.linear_model import LinearRegression
import re

def get_file():
    print('Please select a csv file')
    file_name = sys.stdin.readline()
    return file_name[:-1]



def linear_regression(file_name):
    df = pd.read_csv(file_name)
    #print(df)
    Y = df.ix[:,1]  ##http://stackoverflow.com/questions/11285613/selecting-columns
    Xn = df.ix[:,2:] 
    lr = LinearRegression()  ##http://stackoverflow.com/questions/19991445/run-an-ols-regression-with-pandas-data-frame
    lr.fit(Xn, Y)
    return df, lr
    

def print_equation(df, lr):
    print('coef is: '+str(lr.coef_))
    print('incpt is: '+str(lr.intercept_))
    header_list = df.columns.values
    #print(header_list)  ##http://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
    reg_equation = str(header_list[1])+ '='
    for i in range(0,len(lr.coef_)):
        reg_equation += (str(lr.coef_[i]))
        reg_equation += str(header_list[2+i])## 2 because the header_list include Date and y
        reg_equation += ' + '
    reg_equation += str(lr.intercept_)
    print(reg_equation)


def get_predictor():
    print('Please enter the Xn in "X1,X2,X3...,Xn" format')
    user_input = sys.stdin.readline()[:-1] 
    Xn_pred = re.split(",", user_input)     #http://stackoverflow.com/questions/10974932/python-split-string-based-on-regular-expression
    Xn_pred = [float(i) for i in Xn_pred] #float(i) for i in lst]
    print(Xn_pred)
    return Xn_pred
    

def make_prediction(Xn_pred, lr, df):
    result = 0
    for i in range(0,len(lr.coef_)):
        result += lr.coef_[i]*Xn_pred[i] 
    result += lr.intercept_
    print( str(df.columns.values[1])+' is predicted to be '+str(result) )
    
    

file_name = get_file()
df ,lr = linear_regression(file_name)
print_equation(df, lr)
Xn_pred =  get_predictor()
make_prediction(Xn_pred, lr, df)
##Check Assumption
##different type file support?
##different model support?
##plot graph? difficult for high dimension



