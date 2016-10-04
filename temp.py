# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd


"User task: Ask user to inputs a file location and return xlxs"
def user_input_file_location():
    usrinput = input(">>> Input: ")
    print("Your file location is "+usrinput)
    return usrinput;
    
"System task: read xlxs and turn it into dataframe"
def system_input_file(usrinput):
    xlsx = pd.ExcelFile(usrinput)
    excel_file = xlsx.parse(0)
    print(excel_file.head())
    return excel_file
    

"Show basic regression_statistic and print it to users" 
def show_regression_statistic(excel_file):
    df = pd.DataFrame(excel_file)
    df = df.drop(df.columns[0],axis=1)
    print("The means for each column are:" )
    print(df.mean())
    print_line()
    print("The standard deviation for each column are:")
    print(df.std())
    print_line()
    print("The Maximun deviation for each column are:")
    print(df.max())
    print_line()
    print("The Mimnium deviation for each column are:")
    print(df.min())
    print_line()
    

    
"Show number of null values and print it to users"    
def show_number_of_null_values():
    return
def clean_all_null():
    return
"Calculate the predicated value Y based on users' input and show the regression question"    
def predicated_value():
    return
"Check which assumption is violated and print it to usrs"
def check_hypothesis():
    return
    
def print_line():
    print("================================================================")


"===============================================above is functions======================================================"

"===============================================below is implementation================================================="

"1.ask usr to input the location of the file"
print("Welcome, this is the beta version of statsitcal model application")
print("\n")
print("Please Enter the absolute path of your .xlxs file")
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


usrinput = user_input_file_location()
df = system_input_file(usrinput)
print_line()


"2.show basic regression statistic"

show_regression_statistic(df)




"3. show null value of Y, X1, X2,....   <======ignore Data quality for a moment"

"4. choose to ignore null value or not <======ignore Data quality for a moment "


"5. ask usr to input X1,X2,X3,....."


"6. based on answer of 4, build regression model and calculate the basic regression statistic"


"7. show predicited vlaue"

"8. exit"
