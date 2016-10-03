# -*- coding: utf-8 -*-

import pandas as pd
import sys
import xlrd
import csv


def get_file():
    print('Please select a excel file')
    file_name = sys.stdin.readline()
    return file_name[:-1]



def analyse_excel(file_name):
    df = pd.read_excel(file_name)
    print(df)
    # Then, use pandas and other Machine Learning to analyse



file_name = get_file()
analyse_excel(file_name)
