from bs4 import BeautifulSoup
import requests
import re

#Storing wanted artist
artist = input("Desired artist (eg. good-kid) >> ")

#Storing wanted month
month = input("First 3 letters of desired month (eg. OCT) >> ")

#Transforimg wanted artist into an html search term
artist_html_syntax = ""
for c in artist:
    if c == "-":
        artist_html_syntax += "%20"
    else:
        artist_html_syntax += c 

#Obtaining the search URL for wanted artist
prelim_url = "https://www.ticketmaster.com/search?q=" + artist_html_syntax

prelim_response = requests.get(prelim_url)
prelim_soup = BeautifulSoup(prelim_response.text, "html.parser")

url = ""
for links in prelim_soup.find_all('a'):
    check_link = links.get("href")
    if artist in check_link:
        url = "https://www.ticketmaster.com" + check_link
        break

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

months = soup.find_all(string=month)
print(months)