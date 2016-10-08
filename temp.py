# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import functions # I think this is better than from functions import * when coming to maintance cost

"You should put functions.py and temp.py under same directory"

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


        
usrinput = functions.user_input_file_location()
df = functions.system_input_file(usrinput)



#2. show menu for users to choose what they want

while menu_parameter:
    print("\n")
    print("A. Input your file again")
    print("B. Show your complete input file ")
    print("C. Show part of your input file ")
    print("D. Build your regression ")
    print("E. Drop Space and Drop Null  ")
    print("F. Enter Data Science kit too  ")
    ans = input("Please input your choice    ")        
# Scope(local variable) http://stackoverflow.com/questions/7382638/python-variable-scope-in-if-statements
    if ans.lower()=="q":
        break
    
    elif ans.lower()=="a":
        usrinput = functions.user_input_file_location()
        df = functions.system_input_file(usrinput) #This acts like a pointer and df is a global variable
        
    elif ans.lower()=="b":
        start = functions.time.time()
        print("\n")
        print(df)
        end = functions.time.time()
        print(" ")
        print("Time needed to implement this function: "+str(end - start))
        
    elif ans.lower()=="c":
        start = functions.time.time()
        row_number = input("How many row would you like to display   ")
        row_number = int(row_number)
        print("\n")
        print(str(df[:row_number]))
        end = functions.time.time()
        print(" ")
        print("Time needed to implement this function: "+str(end - start))
        
    elif ans.lower()=="d":
        
        print("non:")
        start = functions.time.time()
        functions.show_regression_statistic(df) # 3. show regression statistic
        data_frame, linear_equation = functions.linear_regression(df)
        functions.print_equation(data_frame,linear_equation)
        end = functions.time.time()
        print(" ")
        print("Time needed to implement this function: "+str(end - start))
        
        menu_parameter0 = input("Enter P to show matrix plot or anyother button to continue   ")
        if menu_parameter0.lower()=="p": # The graph doesn't show , i dont know why
            start = functions.time.time()
            functions.scatter_matrix(df,alpha=0.2, figsize=(6, 6), diagonal='kde')
            functions.plt.show()
            
        menu_parameter1 = input("Enter <Yes> to make prediciton or <No> to exit the program or anyother button back to main menu   ")
        #Go into prediction section
        
        if menu_parameter1.lower()=="yes":
            start = functions.time.time()
            print("\n")
            predictors = functions.get_predictor(linear_equation)
            functions.make_prediction(predictors,linear_equation,data_frame)
            print("\n")
            end = functions.time.time()
            print(" ")
            print("Time needed to implement this function: "+str(end - start))
            
        elif menu_parameter1.lower()=="no":
            menu_parameter = False
            
            
    elif ans.lower()=="e":
            start = functions.time.time()
            data_frame_no_space_null = functions.drop_space_nondigital(df)
            menu_parameter2 = input("Enter <Yes> to save the change to your program or anyother button to cancel ")
            if menu_parameter2.lower() == "yes":
                df = data_frame_no_space_null      #save the dataframe without any null to the previous dataframe, applying to the whole program
            end = functions.time.time()
            print(" ")
            print("Time needed to implement this function: "+str(end - start))
            
    elif ans.lower()=="f":
        print("1.Time series analysis")
        print("2.Decision Tree")
        
        menu_parameter3 = input("Enter <Quit> to quit the program")
        if menu_parameter3.lower() == "quit":
            menu_parameter = False
            
            
        
     
        
"3. show null value of Y, X1, X2,.... i think we should ignore data quality"

"4. choose to ignore null value or not i think we should ignore data quality"

"5. based on answer of 4, build a regression model and calculate the basic regression statistic"


"6. ask usr to input X1,X2,X3,....."

"7. show predicited vlaue"

"8. exit"
