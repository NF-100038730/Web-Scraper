from bs4 import BeautifulSoup
import requests
from s_to_f import *

def check_state(state, city):
    
    state_full = short_to_full(state)

    city_p20 = ""
    for c in city:
        if c == " ":
            city_p20 += "%20"
        else:
            city_p20 += c

    #Getting gas price url for the given state and city
    gb_url = f"https://www.{state_full}gasprices.com/{city_p20}/GasPriceSearch.aspx"
    print(gb_url)
    #Assigning a User-Agent as not to be rejected for botting with requests lib
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    #Creating a response object which the html text will be taken from and assigned to a BeautifulSoup object
    #gb_response = requests.get(gb_url, headers=headers)
    #gb_soup = BeautifulSoup(gb_response.text, "html.parser")
    #print(gb_soup.prettify())
        
