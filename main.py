from bs4 import BeautifulSoup
import requests

def check_state(state, city, fuel):
   
   state_full = short_to_full(state)

   city_p20 = ""
   for c in city:
       if c == " ":
           city_p20 += "%20"
       else:
           city_p20 += c

   fuel_type = fuel_to_id(fuel)

   #Getting gas price url for the given state and city
   gb_url = f"https://www.{state_full}gasprices.com/GasPriceSearch.aspx?fuel={fuel_type}&qsrch={city_p20},%20{state}"
   print(gb_url)
   #Assigning a User-Agent as not to be rejected for botting with requests lib
   headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

   #Creating a response object which the html text will be taken from and assigned to a BeautifulSoup object
   gb_response = requests.get(gb_url, headers=headers)
   gb_soup = BeautifulSoup(gb_response.text, "html.parser")

   #Storing every element with a "price_num" class in a list
   elements_with_price = gb_soup.find_all(class_="price_num")
   #Creating a new list that will hold only the sting values
   prices = []

   #Going through every element in "elements_with_price" and storing the string value in prior list "prices"
   for i in range(len(elements_with_price)):
       parent = elements_with_price[i].parent
       div = parent.find("div")
       prices.append(div.string)

   #elements_with_address = gb_soup.find_all(class_="address")
   #addresses = []
   


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

def fuel_to_id(fuel):
   if fuel == "Regular":
       return "A"
   elif fuel == "Midgrade":
       return "B"
   elif fuel == "Premium":
       return "C"
   elif fuel == "Diesel":
       return "D"