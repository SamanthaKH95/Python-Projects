#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:57:46 2018

@author: sam
"""
import re
import requests
import string
import numpy as np

#introduction 
print("\nHello! This program will help you find the number of times a word appears on a webpage. You can search for as many words on as many web pages as you'd like.\n") 

#the main function allows for ease of nesting the other two main functions - one for getting the source code and one for
#inputting and processing the keyword search. This main function allows the user to enter a website and search as many
#keywords as they'd like, and do that for as many websites as they'd wish via nested loops. 
#If they want to terminate, they can do so  after the first keyword search by inputting "n" for the 
#decision structure to terminate, or at any point after that.
def main():    
    start = True 
    while start == True:
        words = main1()
        main2(words)
        response = input("Would you like to search another keyword on this page? input y for yes and n for no")
        while response == "y":
            main2(words)
            response = input("Would you like to search another keyword on this page? input y for yes and n for no")
        if response == "n":
            startover = input(print("Would you like to search on another website? y for yes and n for no"))
            if startover == "y":
                main()
            if startover == "n":
                print("Thank you so much for using this program! We hope it was helpful. Have a nice day.")
                start = False
                break
        
#this function gathers and stores the website's source code into a list and prints out the first 10 html elements 
#it also returns the list to be used by main2 and all consequent functions
def main1():
    
    website = get_website() #calls another function to get and store website
    response= requests.get(website)
    txt=response.text
    words=txt.split()
    print("\nThe following are the first 10 elements in the source code:\n")
    print(words[0:10])
    return words

#this function inputs the keyword the user is searching for. It calls multiple other functions to manipulate the data, 
# in order to standardize the list so the keyword count accurately counts all instances of the keyword even if it is 
#punctuated, capitalized, or tagged. It outputs the number of times the keyword appears on the website at the end.
def main2(words):
    keyword = input("Please enter the keyword you are looking for:")
    lowercaselist = making_everything_lowercase(words) #calls function to make all words within list lowercase
    listwithoutpunctuation = removing_punctuation(lowercaselist)#calls function to remove all punctuation
    listwithouttags = removing_tags(listwithoutpunctuation)#calls function to remove all tags 
    print("\nThis is how many times", keyword, "appears on this website.\n")
    print(listwithouttags.count(keyword.lower())) #<- makes the keyword lowercase as well before counting from the list and outputting
    
    
#function to prompt user input of a website - also makes sure the format is correct - returns website url 
def get_website():
    add = input("Please enter a website using this format: http://www.website.domain. ie: http://www.georgetown.edu: ")
    if "http://" not in add:
        add = ''.join(["http://", add])
    return add

#makes everything within the list lowercase as a part of standardizing the list - returns new lowercase list
def making_everything_lowercase(words):
    lowercaselist = []
    for item in words:
        lowercaselist.append(item.lower())
    return (lowercaselist)
    #print(lowercaselist) 
    
# removes all punctuation - returns new list without punctuation as part of standardizing list
def removing_punctuation (words):
    
    nopunctuationlist= []
    for item in words:
        intab = string.punctuation
        white_list = list(np.repeat(' ', len(intab)))
        outtab = ''.join(white_list)
        tran_tab = str.maketrans(intab, outtab)
        x = item.translate(tran_tab)
        x = x.split(' ')
        nopunctuationlist.extend(x)
    return (nopunctuationlist)
    
#Words with tags attached (ie <h1>word) don't seem to be counted, so I have to remove all tags associated with <>
#Found the solution to do so online, via importing regex 
#This function cleans all the tags and replaces it with an empty character, then stores the words individually into a list
#The cleaned list is then returned to main
def removing_tags(words):  
    notagslist= []
    for item in words:
        useless_stuff = re.compile("/<td>[^<]*<([^>]*)><\/td>/" )
        x = re.sub(useless_stuff, ' ' , item)
        #x = re.sub(re.compile('<.*?>|</.*?>'), ' ' , item)
        #x = useless_stuff.sub(' ' , item)
        notagslist.append(x)
    return (notagslist)
    

main ()