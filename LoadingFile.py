import os
import pandas as pd
import numpy as np
import sys

class XlsLoading ( object ):
# Charging  the xls file

# Constructor
    def __init__ ( self):
        self.namefile = ""
        self.pandasxls = ""
        self.namesheetselectionned = ""
        self.yoursheet = ""
        self.xls_file = ""
        self.id = ""
        self.r = ""
        self.f = ""
        self.m = ""
           
# End of constructor
        
# Loading xls file 
    def LoadingXlsFile ( self ):
        while True:
            self.namefile = input("Name of the xls file to load (don't forget the extension) :")
            if os.path.isfile (self.namefile):
                print ( "the file is been loaded" )
                self.pandasxls = pd.ExcelFile(self.namefile)
                break
            else:
                print ( "the file don't exist" )
                continue
 # End of Loading xls file and transform into pandas dataframe    

# Select the good sheet
    def XlsSelectTheGoodSheet (self) :
        xls_file = pd.ExcelFile(self.namefile)
        self.sheets = xls_file.sheet_names
        print ("This is your worksheet in this document",self.sheets)
        while True :
            self.yoursheet = input("Please, select your worksheet : ")
            if self.yoursheet in self.sheets:
                print ("Your worksheet is been charged")
                break
                self.customersdf = xls_file.parse(self.yoursheet) # define as the principal dataframe for pandas
                print (self.customersdf)
            else:
                print("this worksheet don't exist")
                continue
# End Select the good sheet
 
# Select the features for clustering      
    def SelectFeaturesForClustering(self):
            print ("---------------------------------------------------------------------------")
            print ("It's time to select yours features for clustering, look the list on the top")
            print ("---------------------------------------------------------------------------")
            self.id = input("Please type de name of the customer id feature : ")
            self.r = input("Please type de name of recency  feature : ")
            self.f = input("Please type de name of the frequency  feature : ")
            self.m = input("Please type de name of the monetary  feature : ")
         
# End Select the features for clustering     


