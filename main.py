#bs4 import for navigation/manipulation of html docs
from bs4 import BeautifulSoup

#requests import for getting links that are used to make soups (html docs that reflect the response)
import requests

#os imports for pathways of files
import os
from os import getcwd

#time import for auto updates of data via using a timer
import time

#Collecting data from the received html doc and 
def check_state(state, city, fuel):

   #Calling a function to transform short state names into full length state names
   state_full = short_to_full(state)

   #Creating a variable with spaces within the given city name as %20 for html usage
   city_p20 = ""
   for c in city:
       if c == " ":
           city_p20 += "%20"
       else:
           city_p20 += c

   #Caloing a function that encodes the given fuel type based upon GasBuddy's search field
   fuel_type = fuel_to_id(fuel)

   #Getting gas price url for the given state and city
   gb_url = f"https://www.{state_full}gasprices.com/GasPriceSearch.aspx?fuel={fuel_type}&qsrch={city_p20},%20{state}"

   #Assigning a User-Agent as not to be rejected for botting with requests lib
   headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

   #Creating a response object which the html text will be taken from and assigned to a BeautifulSoup object
   gb_response = requests.get(gb_url, headers=headers)
   gb_soup = BeautifulSoup(gb_response.text, "html.parser")

   #Storing every element with "price_num" class in a list
   elements_with_price = gb_soup.find_all(class_="price_num")
   #Creating a new list that will hold only the sting values of the "price_num" classes
   prices = []
   #Going through every element in "elements_with_price" and storing the string value in prior list "prices"
   for i in range(len(elements_with_price)):
       parent = elements_with_price[i].parent
       div = parent.find("div")
       prices.append(div.string)

   #Storing every element with "address" class in a list
   elements_with_address = gb_soup.find_all(class_="address")
   #Creating a new list that will hold only the string values of the "address" classes
   addresses = []
   #Going through every element in "elements_with_address" and storing the string value in prior list "addresses"
   for i in range(len(elements_with_address)):
       parent = elements_with_address[i].parent
       dd = parent.find("dd")
       addresses.append(dd.string)

   #Storing every element with "tm" class in a list
   elements_with_tm = gb_soup.find_all(class_="tm")
   #Creating a new list that will hold only the string values of the "tm" classes
   times = []
   #Going through every element in "elements_with_tm" and storing the string value in prior list "times"
   for i in range(len(elements_with_tm)):
       div = elements_with_tm[i]
       times.append(div.string)
    
   #Getting pathway of the txt file that updates will be posted to
   notif_path = os.path.join(getcwd(), 'result.txt')

   #Calling a function that takes the given lists of data and outputs them into a formated record in our txt file
   update_data(notif_path, prices, addresses, times)
   
#Transforming short state names to full versions for html usage  
def short_to_full(state):
   if state == "AL":
       return "alabama"
   elif state == "AK":
       return "alaska"
   elif state == "AZ":
       return "arizona"
   elif state == "AR":
       return "arkansas"
   elif state == "CA":
       return "california"
   elif state == "CO":
       return "colorado"
   elif state == "CT":
       return "connecticut"
   elif state == "DE":
       return "delaware"
   elif state == "FL":
       return "florida"
   elif state == "GA":
       return "georgia"
   elif state == "HI":
       return "hawaii"
   elif state == "ID":
       return "idaho"
   elif state == "IL":
       return "illinois"
   elif state == "IN":
       return "indiana"
   elif state == "IA":
       return "iowa"
   elif state == "KS":
       return "kansas"
   elif state == "KY":
       return "kentucky"
   elif state == "LA":
       return "louisiana"
   elif state == "ME":
       return "maine"
   elif state == "MD":
       return "maryland"
   elif state == "MA":
       return "massachusetts"
   elif state == "MI":
       return "michigan"
   elif state == "MN":
       return "minnesota"
   elif state == "MS":
       return "mississippi"
   elif state == "MO":
       return "missouri"
   elif state == "MT":
       return "montana"
   elif state == "NE":
       return "nebraska"
   elif state == "NV":
       return "nevada"
   elif state == "NH":
       return "newhampshire"
   elif state == "NJ":
       return "newjersey"
   elif state == "NM":
       return "newmexico"
   elif state == "NY":
       return "newyork"
   elif state == "NC":
       return "northcarolina"
   elif state == "ND":
       return "northdakota"
   elif state == "OH":
       return "ohio"
   elif state == "OK":
       return "oklahoma"
   elif state == "OR":
       return "oregon"
   elif state == "PA":
       return "pennsylvania"
   elif state == "RI":
       return "rhodeisland"
   elif state == "SC":
       return "southcarolina"
   elif state == "SD":
       return "southdakota"
   elif state == "TN":
       return "tennessee"
   elif state == "TX":
       return "texas"
   elif state == "UT":
       return "utah"
   elif state == "VT":
       return "vermont"
   elif state == "VA":
       return "virginia"
   elif state == "WA":
       return "washington"
   elif state == "WV":
       return "westvirginia"
   elif state == "WI":
       return "wisconsin"
   elif state == "WY":
       return "wyoming"

#Encoding the given fuel type to a specific letter as determined by GasBuddy
def fuel_to_id(fuel):
   if fuel == "Regular":
       return "A"
   elif fuel == "Midgrade":
       return "B"
   elif fuel == "Premium":
       return "C"
   elif fuel == "Diesel":
       return "D"

#Writing all data from the "prices" + "addresses" + "times" lists into our txt file the "path" of it
def update_data(path, prices, addresses, times):
   f = open(path, 'w')
   for i in range(len(prices)):
       price = "Price: $" + prices[i] + " as of" + times[i]
       lay = 40 - len(price)
       for j in range(lay):
           if j == lay-1:
               price += " | "
           else:
               price += " "
       f.write(price + "Address: " + addresses[i] + "\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
   f.close()