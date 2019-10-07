#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:29:03 2018

@author: sam
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


def main():
    datafile="StockValues(1).csv"
    stockdata=pd.read_csv(datafile)
    pd.options.display.max_rows = 30 #modifying display so all the columns would display
    pd.options.display.max_columns = 7
    
    #prints stock data
    print("\nThis is the current stock data gathered for 20 stocks:\n")
    print(stockdata)
    
    #prints ticker symbols
    print("\nThis is the ticker symbols for those 20 stocks:\n")
    print(stockdata.iloc[:,0])
    
    #printing specific data corresponding to one stock 
    print("\nThis is the data for the stock on the third row:\n")
    print(stockdata.iloc[2,:])
    
    #specific values for cell
    print("\nThis is the value in row 0, column 4:\n")
    print(stockdata.iloc[0,4])
    
    #prints out specific values 
    print("\nThese are the values for the stocks on rows 2,3,6 for columns 1 and 4:\n")
    print(stockdata.iloc[[1,2,5],[0,3]])
    
    #prints out mean data for 3 numerical columns
    print("\nMean Data:")
    print("The mean yearly-high for all stocks is:", np.round(np.mean(stockdata.iloc[:,2]),2))
    print("The mean yearly-low for all stocks is:", np.round(np.mean(stockdata.iloc[:,3]),2))
    print("The mean MarketCap for all stocks is:", np.round(np.mean(stockdata.iloc[:,4]),2))
    
    #prints out variance data for 3 numerical columns 
    print("\nVarience Data:")
    print("The varience for yearly-high for all stocks is:", np.round(np.var(stockdata.iloc[:,2]),2))
    print("The varience for yearly-low for all stocks is:", np.round(np.var(stockdata.iloc[:,3]),2))
    print("The varience for MarketCap for all stocks is:", np.round(np.var(stockdata.iloc[:,4]),2))
    
    #prints out min data for 3 numerical columns
    print("\nMin Data:")
    print("The min for yearly-high for all stocks is:", np.round(np.min(stockdata.iloc[:,2]),2))
    print("The min for yearly-low for all stocks is:", np.round(np.min(stockdata.iloc[:,3]),2))
    print("The min for MarketCap for all stocks is:", np.round(np.min(stockdata.iloc[:,4]),2))
    
    #prints out max data for 3 numerical columns 
    print("\nMax Data:")
    print("The max for yearly-high for all stocks is:", np.round(np.max(stockdata.iloc[:,2]),2))
    print("The max for yearly-low for all stocks is:", np.round(np.max(stockdata.iloc[:,3]),2))
    print("The max for MarketCap for all stocks is:", np.round(np.max(stockdata.iloc[:,4]),2))
    
    #prints out median data for 3 numerical columns
    print("\nMedian Data:")
    print("The median for yearly-high for all stocks is:", np.round(np.median(stockdata.iloc[:,2]),2))
    print("The median for yearly-low for all stocks is:", np.round(np.median(stockdata.iloc[:,3]),2))
    print("The median for MarketCap for all stocks is:", np.round(np.median(stockdata.iloc[:,4]),2))

    
    #writes specific additional data onto output file
    with open("output.txt", "w") as MyFile:
        
        #writing everything from number 3 onto output file, no need to close MyFile because using with open auto-closes
        #The write method will only write strings, have to change into string
        MyFile.write(str(stockdata.StockTicker))
        MyFile.write("\n")
        MyFile.write(str(stockdata.iloc[2,:]))
        MyFile.write("\n")
        MyFile.write(str(stockdata.iloc[0,4]))
        MyFile.write("\n")
        MyFile.write(str(stockdata.iloc[[1,2,5],[0,3]]))
        MyFile.write("\n") #writing number 3 values end
        
        #writing values from number 5 onto output file: mean
        MyFile.write("\n The following are the mean values for 3 pieces of numerical data:\n")
        
        value1 = np.round(np.mean(stockdata.iloc[:,2]),2) 
        value1 = str(value1)
        MyFile.write("The mean yearly-high for all stocks is:")
        MyFile.write(value1)
        MyFile.write("\n")
        
        value2 = np.round(np.mean(stockdata.iloc[:,3]),2)
        value2 = str(value2)
        MyFile.write("The mean yearly-low for all stocks is:")
        MyFile.write(value2)
        MyFile.write("\n")
        
        value3 = np.round(np.mean(stockdata.iloc[:,4]),2)
        value3 = str(value3)
        MyFile.write("The mean marketcap for all stocks is:")
        MyFile.write(value3)
        MyFile.write("\n")
        
        #writing values from number 5 onto output file: variance
        MyFile.write("\n The following are the variance values for 3 pieces of numerical data:\n")
        
        value4 = np.round(np.var(stockdata.iloc[:,2]),2) 
        value4 = str(value4)
        MyFile.write("The variance yearly-high for all stocks is:")
        MyFile.write(value4)
        MyFile.write("\n")
        
        value5 = np.round(np.var(stockdata.iloc[:,3]),2)
        value5 = str(value5)
        MyFile.write("The variance yearly-low for all stocks is:")
        MyFile.write(value5)
        MyFile.write("\n")
        
        value6 = np.round(np.var(stockdata.iloc[:,4]),2)
        value6 = str(value6)
        MyFile.write("The variance marketcap for all stocks is:")
        MyFile.write(value6)
        MyFile.write("\n")
        
        #writing values from number 5 onto output file: min
        MyFile.write("\n The following are the min values for 3 pieces of numerical data:\n")
        
        value7 = np.round(np.min(stockdata.iloc[:,2]),2) 
        value7 = str(value7)
        MyFile.write("The min yearly-high for all stocks is:")
        MyFile.write(value7)
        MyFile.write("\n")
        
        value8 = np.round(np.min(stockdata.iloc[:,3]),2)
        value8 = str(value8)
        MyFile.write("The min yearly-low for all stocks is:")
        MyFile.write(value8)
        MyFile.write("\n")
        
        value9 = np.round(np.min(stockdata.iloc[:,4]),2)
        value9 = str(value9)
        MyFile.write("The min marketcap for all stocks is:")
        MyFile.write(value9)
        MyFile.write("\n")
        
        #writing values from number 5 onto output file: max
        MyFile.write("\n The following are the max values for 3 pieces of numerical data:\n")
        
        value10 = np.round(np.max(stockdata.iloc[:,2]),2) 
        value10 = str(value10)
        MyFile.write("The max yearly-high for all stocks is:")
        MyFile.write(value10)
        MyFile.write("\n")
        
        value11 = np.round(np.max(stockdata.iloc[:,3]),2)
        value11 = str(value11)
        MyFile.write("The max yearly-low for all stocks is:")
        MyFile.write(value11)
        MyFile.write("\n")
        
        value12 = np.round(np.max(stockdata.iloc[:,4]),2)
        value12 = str(value12)
        MyFile.write("The max marketcap for all stocks is:")
        MyFile.write(value12)
        MyFile.write("\n")
        
        #writing values from number 5 onto output file: median
        MyFile.write("\n The following are the median values for 3 pieces of numerical data:\n")
        
        value13 = np.round(np.median(stockdata.iloc[:,2]),2) 
        value13 = str(value13)
        MyFile.write("The median yearly-high for all stocks is:")
        MyFile.write(value13)
        MyFile.write("\n")
        
        value14 = np.round(np.median(stockdata.iloc[:,3]),2)
        value14 = str(value14)
        MyFile.write("The median yearly-low for all stocks is:")
        MyFile.write(value14)
        MyFile.write("\n")
        
        value15 = np.round(np.median(stockdata.iloc[:,4]),2)
        value15 = str(value15)
        MyFile.write("The median marketcap for all stocks is:")
        MyFile.write(value15)
        MyFile.write("\n")
        
        
    #writing number 5 values end 
        
    #calling summary stats function
    summarystats(stockdata)
        
    #calling append function
    list_of_chars_ineachline = []
    total_chars = 0
        
    total_chars = appendfunction("output.txt", stockdata, list_of_chars_ineachline, total_chars)
    print("\nThe total number of characters within the output file is", total_chars)
    print("\nThe following displays the number of characters within each line of the output file,:\n", list_of_chars_ineachline)
        
        
        
    #calling the function to make the graphs with the dataframe 
    MakeGraphs(stockdata)
    
    #calling the function to print out variables 

    printing_out_variable_names(stockdata, "output.txt")
        
    
    #makes and displays summary statistics for the entire dataframe
def summarystats(dataframe):
    print(dataframe.describe().transpose())
    pd.options.display.max_rows = 50 #modifying display so all the columns would display
    pd.options.display.max_columns = 30
 
    #appends entire dataframe onto output file without deleting anything, counts the number of characters in output and displays
def appendfunction (filename, dataframe, listofchars_ineachline, totalchars):
    
    with open(filename, "a") as MyFile:
        dataframe.to_csv(MyFile, sep=',', mode='a', header='false')
    

    # counting the number of characters in each line and storing to list to return to main    
    with open(filename, "r") as infile:
        totalchars = 0
        for line in infile:
            characters = len(line)
            totalchars = totalchars + characters
            listofchars_ineachline.append(characters) #use sum instead to get totalchars
            
    
    return totalchars
    print ("The total number of characters in the output file is", totalchars)
    print(listofchars_ineachline)
    return listofchars_ineachline 
    
def MakeGraphs(dataframe):
    
    
    #scatterplot
    imagefilename = "Project3GRAPH1.jpg"
    fig = plt.figure


    plt.scatter(dataframe["YearHigh"], dataframe["YearLow"])
    title ="Scatterplot for YearHigh and YearLow"
    plt.suptitle(title, fontsize=20)
    plt.xlabel("Year High", fontsize=18)
    plt.ylabel("Year Low", fontsize=16)
    plt.savefig(imagefilename)
    plt.show()
    
    #boxplots
    imagefilename2 = "Project3GRAPH2.jpg"
    dataframe.boxplot(by="StockTicker")
    title4 = "Boxplots for Numerical Info By StockTicker"
    plt.suptitle(title4, fontsize=20)
    plt.show()
    plt.savefig(imagefilename2)
    
    #lineplot
    imagefilename3 = "Project3GRAPH3.jpg"
    dataframe.plot.line(x="StockTicker",y=None)
    title2 = "Line Plots Based on StockTicker"
    plt.suptitle(title2, fontsize=20)
    plt.show()
    plt.savefig(imagefilename3)

    #BarGraph
    imagefilename4 = "Project3GRAPH4.jpg"
    dataframe.plot.bar(x="StockTicker", y="YearHigh")
    title3 = "Bar Graph by Stockticker"
    plt.suptitle(title3, fontsize=20)
    plt.show()
    plt.savefig(imagefilename4)
    
#function to print out variable names from data    
def printing_out_variable_names(dataframe, outputfile):
    print("The variable names in the dataframe are: ", dataframe.columns.values)
    inputvariable = input("Please choose one variable that represents numerical data")
    print("\nThe following are the min, max, median, mean, and variance for:", inputvariable, ":\n")
    
    #use if statements to assess and print out corresponding values for input variable column 
    if inputvariable== "YearHigh":
        print("Mean:", np.round(np.mean(dataframe.YearHigh),2))
        print("Standard Deviation:", np.round(np.std(dataframe.YearHigh),2))
        print("Max:", np.round(np.max(dataframe.YearHigh),2))
        with open(outputfile, "a") as MyFile:
            MyFile.write("Mean:")
            MyFile.write(str(np.round(np.mean(dataframe.YearHigh),2)))
            MyFile.write("\nStandard Deviation:")
            MyFile.write(str(np.round(np.std(dataframe.YearHigh),2)))
            MyFile.write("\nMax:")
            MyFile.write(str(np.round(np.max(dataframe.YearHigh),2)))
    if inputvariable == "YearLow":
        print("Mean:", np.round(np.mean(dataframe.YearLow),2))
        print("Standard Deviation:", np.round(np.std(dataframe.YearLow),2))
        print("Max:", np.round(np.max(dataframe.YearLow),2))
        with open(outputfile, "a") as MyFile:
            MyFile.write("Mean:")
            MyFile.write(str(np.round(np.mean(dataframe.YearLow),2)))
            MyFile.write("\nStandard Deviation:")
            MyFile.write(str(np.round(np.std(dataframe.YearLow),2)))
            MyFile.write("\nMax:")
            MyFile.write(str(np.round(np.max(dataframe.YearLow),2)))
    if inputvariable == "MarketCapBillions":
        print("Mean:", np.round(np.mean(dataframe.MarketCapBillions),2))
        print("Standard Deviation:", np.round(np.std(dataframe.MarketCapBillions),2))
        print("Max:", np.round(np.max(dataframe.MarketCapBillions),2))
        with open(outputfile, "a") as MyFile:
            MyFile.write("Mean:")
            MyFile.write(str(np.round(np.mean(dataframe.MarketCapBillions),2)))
            MyFile.write("\nStandard Deviation:")
            MyFile.write(str(np.round(np.std(dataframe.MarketCapBillions),2)))
            MyFile.write("\nMax:")
            MyFile.write(str(np.round(np.max(dataframe.MarketCapBillions),2)))
    if inputvariable == "Volatility_IndexBeta":
        print("Mean:", np.round(np.mean(dataframe.Volatility_IndexBeta),2))
        print("Standard Deviation:", np.round(np.std(dataframe.Volatility_IndexBeta),2))
        print("Max:", np.round(np.max(dataframe.Volatility_IndexBeta),2))
        with open(outputfile, "a") as MyFile:
            MyFile.write("Mean:")
            MyFile.write(str(np.round(np.mean(dataframe.Volatility_IndexBeta),2)))
            MyFile.write("\nStandard Deviation:")
            MyFile.write(str(np.round(np.std(dataframe.Volatility_IndexBeta),2)))
            MyFile.write("\nMax:")
            MyFile.write(str(np.round(np.max(dataframe.Volatility_IndexBeta),2)))
    
  
    
    
        
    imagefilename5 = "UserGraph.jpg"
    plt.boxplot(dataframe[inputvariable])
    title5 = "Box Plot For" + inputvariable
    plt.suptitle(title5, fontsize =20)
    plt.show()
    plt.savefig(imagefilename5)
    
    
    
    
    
    
main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

