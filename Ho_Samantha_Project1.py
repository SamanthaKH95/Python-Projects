#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:06:13 2018

@author: sam (skh50)
"""

def main ():
    #welcome message 
    print("Welcome to Travel Agency's Hawaiian Airline airfare calculator! Seats to Hawaii begin at $2500.")
    print("There are different discounts and fees depending on your travel plans and personal information." )
    print("This program will help you calculate the final cost of your trip and decide whether to join Travel Agency's membership plan.")
    print("Please make sure to answer in all lower case letters and without any spaces")
    
    #asking for input of numbers of passengers flying economy, business, and first class and outputting total cost updates
    #if total passengers is 0, then program stops 

    num_econ = eval(input("Please enter the number of passengers flying Economy Class."))
    econ_cost = num_econ * 2500 
    if num_econ == 0:
        print("There are no passengers flying economy class.")
    else:
        print("Great! Your total cost is now $", econ_cost,".")
        
    num_business = eval(input("Please enter the number of passengers flying Business Class."))
    business_cost = (num_business * 2500) + (num_business * 300)
    if num_business ==0:
        print("There are no passengers flying Business class.")
        print("Your total cost is now $", econ_cost,".")
    else:
        print("Great! Your total cost is now $", econ_cost + business_cost,".")
    
    num_first = eval(input("Please enter the number of passengers flying First Class."))
    first_cost = (num_first * 2500) + (num_first * 600)
    if num_first ==0:
        print("There are no passengers flying First class.")
        print("Your total cost is now $", econ_cost + business_cost,".")
    if num_econ + num_business + num_first ==0:
        print("You cannot continue with 0 total passengers. Please exit and try again.")
    else:
        print("Great! Your total cost is now $", econ_cost + business_cost + first_cost,".")
        
    total_after_seats = econ_cost + business_cost + first_cost 
    total_passengers = num_econ+num_business+num_first 

     
    
    #calculating discounts depending on layover number, max 3
    layovers = eval(input("How many layovers would you add into your trip? (Each layover is $150 saved per passenger, maximum is 3)"))
    if layovers ==0:
        print("You have added 0 layovers to your trip, your savings is 0.")
    if layovers > 3:
        print ("You entered too many layovers, maximum is 3")
    else: 
        layover_savings = 150 * layovers * total_passengers
        print("Great! You saved", layover_savings, "dollars")
        print("Your total cost is now", total_after_seats-layover_savings,"dollars." )


    total_after_layover_savings = total_after_seats - layover_savings
  
#displaying menu with nested for/if loop and asking user to pick amongst choices, will terminate if none are chosen  
    print("Now we will show you the menu for your flights. Please enter yes or no for these choices. Choice applies to all passengers in booking")
    for mealchoice in ["Chicken", "Beef","lamb", "spam", "Tofu"]:
        print("Would you like", mealchoice, "& Rice?")
        response = input ("'yes' or 'no'?")
        if response == "yes":
                print ("You have chosen", mealchoice, "& Rice for your passengers")
                num_meals = eval(input("Each meal costs $30. Maximum amount of meals is 2 per customer. How many would you like?"))
                if num_meals <= 2 * total_passengers:
                        meal_cost = num_meals * 30
                        print("You have chosen to buy", num_meals, "meals. This costs", meal_cost, "dollars.")
                        total_after_meals = total_after_layover_savings + meal_cost
                        print("Your new total cost is", total_after_meals, "dollars.")
                        break
                else:
                        print("You have entered too many meals for your passengers. Max is 2 per passenger. Please retry.")
                        break
        if response == "no" and mealchoice == "Tofu":
                        print("We have reached the end of the menu. We apologize for lack of choices")
                        total_after_meals = total_after_layover_savings
                        
        else:
            continue 
        

#meals are free if user is a frequent flier of hawaiian air 
    frequent_flier = input("Are you a frequent flier of Hawaiian Air? Please enter yes or no.")
    if frequent_flier == "yes":
        print("Great! Meals are free for frequent fliers. Your new cost is now", total_after_meals - meal_cost, "dollars.")
        cost_after_frequent = total_after_meals - meal_cost 
        print("Your trip now costs", cost_after_frequent,"dollars.")
    else:
        print("Non frequent fliers do not get a meal discount")
        cost_after_frequent = total_after_meals 
        print ("Your cost is still", cost_after_frequent, "dollars.")
        

#evaluating group discount 
    if total_passengers > 5:
        print("Congratulations! You qualify for a 10% group discount from the travel agency.")
        cost_after_group_discount = cost_after_frequent * 0.9
        print ("Your total is now", cost_after_group_discount, "dollars.")
    else:
        print ("Sorry, you do not qualify for a group discount.")
        cost_after_group_discount = cost_after_frequent
        print ("Your total is now", cost_after_group_discount, "dollars.")
        
#evaluating military discount based on total before group discount
    military = input ("Are you a part of the military?")
    if military == "yes":
        print ("Congrats! You qualify for a 30% military discount.")
        cost_after_military = cost_after_frequent * 0.6
        print ("Your total is now", cost_after_military, "dollars.") 
    else:
        print ("You do not qualify for a military discount")
        cost_after_military = cost_after_group_discount
        print ("Your total is now", cost_after_military, "dollars.")

#evaluating whether the travel agency membership is worth it
    print ("If total cost after savings is more than $6000, then the membership with the agency will cost $300 but give a rebate of $350. If under $6000, then the membership will cost $400 but all meals would be free. ")
    if cost_after_military > 6000:
        print ("You will save $50 if you join the travel agency. Your new total cost will be", cost_after_military - 50, "dollars.")
        membership = input ("Would you like to join the membership? Yes or No")
        if membership == "yes":
            print ("Great! Your final cost for this trip is", cost_after_military - 50, "dollars.")
        else:
            print ("You chose not to join the membership. Your final cost for this trip is", cost_after_military, "dollars.")
    elif cost_after_military < 6000:
        print ("Travel agency membership costs $400 but all of your meals would be free.")
        post_travel_agency_cost = cost_after_military + 400 - meal_cost 
        if post_travel_agency_cost < cost_after_military:
            print ("You will save money from joining the travel agency membership")
            answer = input ("Do you want to join the membership?")
            if answer == "yes":
                print ("Great! Your final cost is", post_travel_agency_cost, "dollars.")
            else:
                print ("Your final cost is",cost_after_military, "dollars.")
        elif post_travel_agency_cost > cost_after_military:
            print ("You will not save money from joining the travel agency membership.")
            answer = input ("Do you want to join the membership?")
            if answer == "yes":
                print ("Your final cost is",post_travel_agency_cost, "dollars.")
            else:
                print ("your final cost is", cost_after_military, "dollars.")
            
#listing out the number of passengers in each seat class 
    print ("To summarize, these are the passengers you have in each seat class:")
    while num_econ > 0:
        print ("1 Economy Class Passenger")
        num_econ = num_econ - 1
        
    while num_business > 0:
        print ("1 Business Class Passenger")
        num_business = num_business - 1
        
    while num_first > 0:
        print ("1 First Class Passenger")
        num_first = num_first - 1

        
        
main()    