# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
from sklearn.linear_model import LinearRegression
import re   #regular expression
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt


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


def drop_non_digital(df):
    no_digit_df = df
    drop_row_list = []                                            # 
    column_length = df.shape[0]                                  #http://stackoverflow.com/questions/15943769/how-to-get-row-count-of-pandas-dataframe
    row_length = df.shape[1]
    print(df.iloc[2,2])
    print(column_length,row_length)
    for r in range(0,column_length):
        for c in range(1,row_length):
            try:
                float(no_digit_df.iloc[r,c])
            except ValueError:
                drop_row_list.append(r)
    print(drop_row_list)
    no_digit_df = no_digit_df.drop(no_digit_df.index[drop_row_list])    #http://stackoverflow.com/questions/15943769/how-to-get-row-count-of-pandas-dataframe
    no_digit_df = no_digit_df.dropna()                           #http://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-of-certain-column-is-nan
   # no_digit_df = no_digit_df.reset_index()
   # no_digit_df = no_digit_df.drop('index',1)
   # df = df.drop('column_name', 1)
    print(no_digit_df)
    #return(no_digit_df)
    
        
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
def get_predictor(linear_equation):
    print('Please enter the Xn in "X1,X2,X3...,Xn" format')
    print("In your case, your n is "+str(len(linear_equation.coef_)))
    usrinput = input(">>> Input: ")
    print("Your input is "+usrinput) 
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
    print("\n")
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
drop_non_digital(df)


#2. show menu for users to choose what they want

while menu_parameter:
    print("\n")
    print("A. Input your file again")
    print("B. Show your complete input file ")
    print("C. Show part of your input file ")
    print("D. Build your regression ")
    ans = input("Please input your choice    ")        
# Scope(local variable) http://stackoverflow.com/questions/7382638/python-variable-scope-in-if-statements
    if ans.lower()=="q":
        break
    
    if ans.lower()=="a":
        usrinput = user_input_file_location()
        df = system_input_file(usrinput) #This acts like a pointer and df is a global variable
    
    if ans.lower()=="b":
        print("\n")
        print(df)
        
    elif ans.lower()=="c":
        row_number = input("How many row would you like to display   ")
        row_number = int(row_number)
        print("\n")
        print(str(df[:row_number]))
        
    elif ans.lower()=="d":
        show_regression_statistic(df) # 3. show regression statistic
        data_frame, linear_equation = linear_regression(df)
        print_equation(data_frame,linear_equation)
        
        menu_parameter0 = input("Enter P to show matrix plot or anyother button to continue   ")
        if menu_parameter0.lower()=="p": # The graph doesn't show , i dont know why
            scatter_matrix(df,alpha=0.2, figsize=(6, 6), diagonal='kde')
            plt.show()
            
        menu_parameter1 = input("Enter Yes to make prediciton or No to exit the program or anyother button back to main menu   ")
        #Go into prediction section
        
        if menu_parameter1.lower()=="yes":
            print("\n")
            predictors = get_predictor(linear_equation)
            make_prediction(predictors,linear_equation,data_frame)
            print("\n")
        elif menu_parameter1.lower()=="no":
            menu_parameter = False
            exit()
            
        
        
        
"3. show null value of Y, X1, X2,.... i think we should ignore data quality"

"4. choose to ignore null value or not i think we should ignore data quality"

"5. based on answer of 4, build a regression model and calculate the basic regression statistic"


"6. ask usr to input X1,X2,X3,....."

"7. show predicited vlaue"

"8. exit"