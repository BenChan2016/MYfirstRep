# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import xlrd, pandas as pd

"User task: Ask user to inputs a file location and return xlxs"
def user_input_file_location():
    usrinput = input(">>> Input: ")
    print("Your file location is "+usrinput)
    return usrinput
    
"System task: read xlxs and return the file o"
def system_input_file(usrinput):
    excel_file = pd.ExcelFile(usrinput)
    return excel_file
    
"Show basic regression_statistic and print it to users" 
def show_regression_statistic():
 
"Show number of null values and print it to users"    
def show_number_of_null_values():
    
def clean_all_null():

"Calculate the predicated value Y based on users' input and show the regression question"    
def predicated_value():

"Check which assumption is violated and print it to usrs"
def check_hypothesis():
    
    
    
"1.ask usr to input the location of the file"

"2.show basic regression statistic"

"3. show null value of Y, X1, X2,...."

"4. choose to ignore null value or not"

"5. based on answer of 4, recalculate the basic regression statistic"

"6. ask usr to input X1,X2,X3,....."

"7. show predicited vlaue"

"8. exit"