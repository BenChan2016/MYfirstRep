# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 23:14:29 2016

@author: jacksiu
"""


import pandas as pd
import sys
import xlrd
import csv


def get_file():
    print('Please select a excel file')
    file_name = sys.stdin.readline()
    return file_name[:-1]


def csv_from_excel(file_name):##http://stackoverflow.com/questions/20105118/convert-xlsx-to-csv-correctly-using-python

    wb = xlrd.open_workbook(file_name)
    sh_name = wb.sheet_names()   ##http://stackoverflow.com/questions/12250024/how-to-obtain-sheet-names-from-xls-files-without-loading-the-whole-file
    sh = wb.sheet_by_name(sh_name[0])
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()




def analyse_csv():
    df = pd.read_csv('your_csv_file.csv')
    print(df)
    # Then, use pandas and other Machine Learning to analyse



file_name = get_file()
csv_from_excel(file_name)
analyse_csv()
