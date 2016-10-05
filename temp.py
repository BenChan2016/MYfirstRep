# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
from sklearn.linear_model import LinearRegression
import re


"User task: Ask user to inputs a file location and return xlxs"
def user_input_file_location():
    usrinput = input(">>> Input: ")
    print("Your file location is "+usrinput)
    return usrinput;
    
"System task: read xlxs and turn it into dataframe"
def system_input_file(usrinput):
    xlsx = pd.ExcelFile(usrinput)
    excel_file = xlsx.parse(0)
    print("\n")
    print(excel_file.head())
    return excel_file
    

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
    
"Show number of null values and print it to users"    
def show_number_of_null_values():
    return
def clean_all_null():
    return
"Calculate the predicated value Y based on users' input and show the regression question"    
def get_predictor():
    print('Please enter the Xn in "X1,X2,X3...,Xn" format')
    usrinput = input(">>> Input: ")
    print("Your file location is "+usrinput) 
    Xn_pred = re.split(",", usrinput)     #http://stackoverflow.com/questions/10974932/python-split-string-based-on-regular-expression
    Xn_pred = [float(i) for i in Xn_pred] #float(i) for i in lst]
    #old fashion way: for i in range(0,len(a)) :
    #                     a[i] = float(a[i])
    print(Xn_pred)
    return Xn_pred


def make_prediction(Xn_pred, lr, df):
    result = 0
    for i in range(0,len(lr.coef_)):
        result += lr.coef_[i]*Xn_pred[i] 
    result += lr.intercept_
    print( str(df.columns.values[1])+' is predicted to be '+str(result) )
    
"Check which assumption is violated and print it to usrs"
def check_hypothesis():
    return
    
def print_line():
    print("================================================================")


"===============================================above is functions======================================================"

"===============================================below is implementation================================================="

#"1.ask usr to input the location of the file"
print("Welcome, this is the beta version of statsitcal model application")
print("\n")
print("Please Enter the absolute path of your .xlxs file")
print("\n")
print("The format of your file should be as followings")
print("    DATE    Y  X_1  X_2  X_3  ...  X_N")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")
print("YYYY/MM/DD  V   V    V    V   ...   V ")

menu_parameter = True


        
usrinput = user_input_file_location()
df = system_input_file(usrinput)



#2. show menu for users to choose what they want

while menu_parameter:
    print("\n")
    print("A. Show your complete input file ")
    print("B. Show part of your input file ")
    print("C. Build your regression ")
    ans = input("Please input your choice    ")        
    
    if ans.lower()=="a":
        print("\n")
        print(df)
        
    elif ans.lower()=="b":
        row_number = input("How many row would you like to display   ")
        row_number = int(row_number)
        print("\n")
        print(str(df[:row_number]))
        
    elif ans.lower()=="c":
        show_regression_statistic(df) # 3. show regression statistic
        data_frame, linear_equation = linear_regression(df)
        print_equation(data_frame,linear_equation)
        
        menu_parameter1 = input("Enter Yes to make prediciton or No to exit the program or anybutton back to main menu   ")
        #Go into prediction section
        if menu_parameter1.lower()=="yes":
            predictors = get_predictor()
            make_prediction(predictors,linear_equation,data_frame)
            print("\n")
        if menu_parameter1.lower()=="no":
            menu_parameter = False
            exit()
        
        
"3. show null value of Y, X1, X2,.... i think we should ignore data quality"

"4. choose to ignore null value or not i think we should ignore data quality"

"5. based on answer of 4, build a regression model and calculate the basic regression statistic"


"6. ask usr to input X1,X2,X3,....."

"7. show predicited vlaue"

"8. exit"