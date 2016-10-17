# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import functions # I think this is better than from functions import * when coming to maintance cost
import numpy as np
import re
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

menu_para_first_level= True
menu_para_A_1 = True
menu_para_B_1 = True
menu_para_B_1_1 = True
menu_para_B_2_1 = True
menu_para_C_3_1 = True
menu_para_B_1_1_1 = True
menu_para_B_2_1_1 = True
menu_para_C_3_1_1 = True
model_built = False


#This menu is actioned by <n> to exit or <any button> to continue#
#This menu is classified by three levels, where A,B are first, so on and so forth.
#Lesson to learn when creating this menu: #
#1. should create functions without any dependency with other functions#
#2. Framework should be created first, e.g menu#
#3. all variable naming standard should be done at the very first stage of a development process#
#4. Class vs Function. Decisison should be made


while(menu_para_first_level==True):
    
    print("A. Data Preparation")
    print("   1. Drop non-digiral row")
    print("   2  Swap columns")
    print("   3. Show non-digital row")
    print("")
    print("B. Data Science tool kit")
    print("   1. Regression")
    print("      1.1 Show input")
    print("      1.2 Make prediction")
    print("      1.3 Plot graph")
    print("      1.4 Regression diagonsis")
    print("   2. Decision Tree")
    print("      2.1 Show input")
    print("      2.2 Make prediction")
    print("      2.3 Plot graph")
    print("      2.4 Decision Tree diagonsis")
    print("   3. Time Series")
    print("      3.1 Show input")
    print("      3.2 Make prediction")
    print("      3.3 Plot graph")
    print("      3.4 Time Series diagonsis")
    print("C. Re-input your file")
    print("First level")
    print("   Second level")
    print("      Third level")
    user_choice_first = input("First level: Please input choice to enter Data Preparartion or Data Science tool kit, or <n> to exit ")
    print("")
    if user_choice_first.lower()== "a":
        print("   1. Drop non-digiral row")
        print("   2  Swap columns")
        print("   3. Show non-digital row")
        print("   Second level")
        user_choice = input("Please input choice to enter second level ")
        
        if user_choice.lower()== "1":
            print("Enter 1")
            while(menu_para_A_1==True):
                # implementation
                data_frame_no_space_null = functions.drop_space_nondigital(df)
                menu_parameter2 = input("Enter <Yes> to save the change to your program or anyother button to cancel ")
                if menu_parameter2.lower() == "yes":
                    
                    df = data_frame_no_space_null      #save the dataframe without any null to the previous dataframe, applying to the whole program
                print(" ")
                user_choice = input("Press <n> to go back one level or <any button> to repeat process")
                if user_choice.lower()== "n":
                    print("break")
                    break
                
            
        elif user_choice.lower()== "2":
            while(menu_para_A_1==True):
                # implementation
                print("Please input two columns name that you would like to switch and is sperated by comma, e.g. X1,X2 " )
                column_name = input("Please Enter   ") #string
                column_name = str(column_name)
                column_name = column_name.replace(" ","")         
                column_name_array = re.split(",",column_name)
                print(column_name_array[0],column_name_array[1])
                df = functions.swap_columns_index(column_name_array[0],column_name_array[1],df)
                print("")
                print("Your changed file ")
                print("")
                #print(df.head())
                print("")
                user_choice = input("Press <n> to go back one level or <any button> to repeat process")
                if user_choice.lower()== "n":
                    break
                
            
        elif user_choice.lower()== "3":
            while(menu_para_A_1==True):
                # implementation
                user_choice = input("Press <n> to go back one level or <any button> to repeat process")
                if user_choice.lower()== "n":
                    break
                
            
        else :
            continue
        
    elif user_choice_first.lower()== "b":
        print("   1. Regression")
        
        print("   2. Decision Tree")

        print("   3. Time Series")
        
        print("   Second level")

        user_choice = input("Please input choice to enter second level ")
        
        if user_choice.lower()=="1":
            #1.1
            print("\n")
            print("Please how much data you want for validating a model, e.g. 0.2")
            testing_percentage = input("Please Enter    ")
            print("")
            training_data, testing_data = functions.data_frame_split_for_training(df, testing_percentage)
            linear_equation = functions.linear_regression(training_data)
            while(menu_para_B_1_1==True):
                print("      1.1 Show input")
                print("      1.2 Make prediction")
                print("      1.3 Plot graph")
                print("      1.4 Regression diagonsis")
                print("      Third level")
                user_choice = input("Please input choice to enter third level ")
                # implementation
                if user_choice.lower()== "1.1":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        print("\n")
                        print(df)
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                        
                if user_choice.lower()== "1.2":
                    # implementation
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        user_input_predictor = functions.get_predictor_one_D(linear_equation)
                        prediciton_for_user = functions.make_prediciton_beta(user_input_predictor,linear_equation)
                        print("Your prediciton value is "+str(prediciton_for_user)+" in array-like format")
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "1.3":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        functions.scatter_matrix(training_data,alpha=0.2, figsize=(6, 6), diagonal='kde')
                        functions.plt.show()
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "1.4":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        
                        predicted_result_from_training_data = functions.transform_DFpredicition_to_array(training_data,linear_equation)

                        predicted_result_from_testing_data = functions.transform_DFpredicition_to_array(testing_data,linear_equation)
                        
                        dfListY = testing_data.iloc[:,1].tolist()
                        dfListY_training = training_data.iloc[:,1].tolist()
            
                        print("The median absolute error for testing data is " + str(functions.median_absolute_error(dfListY,predicted_result_from_testing_data)))
                        print("")
                        print("The median absolute error for training data is " + str(functions.median_absolute_error(dfListY_training, predicted_result_from_training_data)))
                        print("")
                        print("The R^2 score for testing data is " + str(functions.r2_score(dfListY,predicted_result_from_testing_data)))
                        print("")
                        print("The R^2 score for training data is " + str(functions.r2_score(dfListY_training, predicted_result_from_training_data)))
            
                       
                        
                        print(" ")
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                    
                user_choice = input("Press  <any button> to stay on this regresion manual or <n> to first level main manual ")
                if user_choice.lower()== "n":
                    break
                else:
                    continue
                
                
                       
        elif user_choice.lower()=="2":
            while(menu_para_B_2_1==True):
                print("Please how much data you want for validating a model, e.g. 0.2")
                testing_percentage = input("Please Enter    ")
                print("")
                training_data, testing_data = functions.data_frame_split_for_training(df, testing_percentage)
                clf_fitted = functions.classification_model_building(training_data)
                print("      2.1 Show input")
                print("      2.2 Make prediction")
                print("      2.3 Plot graph")
                print("      2.4 Decision Tree diagonsis")
                print("      Third level")
                
                user_choice = input("Please input choice to enter third level ")
                # implementation
                if user_choice.lower()== "2.1":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        print("\n")
                        print(df)
                        print(" ")
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                        
                if user_choice.lower()== "2.2":
                    # implementation
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        usrinput = input("Please input predictor    ")
                        #clf_fit here is dummy and never used
                        # need to fix classification_tree_prediciton_for_training function to make it more efficient
                        
                        tree_prediction_training, clf_fit = functions.classification_tree_prediciton_for_training(training_data,usrinput)
                        print("Your predition for predicitor "+str(usrinput)+ " is "+ str(tree_prediction_training)+str("\n"))
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "2.3":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "2.4":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        tree_prediciton_testing = functions.classification_tree_prediciton_for_testing(testing_data,clf_fitted)
                        testing_data_2d_array = functions.transform_DFY_to_2d_array(testing_data)
                        normalized, non_normalized = functions.classification_tree_score(testing_data_2d_array,tree_prediciton_testing)
                        #print(tree_prediciton_testing_2d_array,tree_prediciton_testing)
                        print("The accuracy percentage is "+str(normalized)+" and the accuracy number is "+ str(non_normalized))
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                    
                user_choice = input("Press  <any button> to stay on this decision tree manual or <n> to first level main manual ")
                if user_choice.lower()== "n":
                    break
                else:
                    continue
            
        elif user_choice.ljust()=="3":
            print("      3.1 Show input")
            print("      3.2 Make prediction")
            print("      3.3 Plot graph")
            print("      3.4 Time Series diagonsis")
            print("      Third level")
            while(menu_para_C_3_1==True):
                # implementation
                user_choice = input("Please input choice to enter third level  ")
                # implementation
                if user_choice.lower()== "3.1":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        
                        print("\n")
                        print(df)
                        print(" ")
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                        
                if user_choice.lower()== "3.2":
                    # implementation
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "3.3":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                if user_choice.lower()== "3.4":
                    while(menu_para_B_1_1_1==True):
                        # implementation
                        user_choice = input("Press <n> to go back one level or <any button> to repeat")
                        if user_choice.lower()== "n":
                            break
                        else:
                            continue
                    
                    
                user_choice = input("Press  <any button> to stay on this Time Series manual or <n> to first level main manual ")
                if user_choice.lower()== "n":
                    break
                else:
                    continue
    
    elif user_choice_first.lower()== "c":
        usrinput = functions.user_input_file_location()
        df = functions.system_input_file(usrinput) #This acts like a pointer and df is a global variable
        
    elif user_choice_first.lower()== "n":
        break
    else:
        continue
