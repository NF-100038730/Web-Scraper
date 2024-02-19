from bs4 import BeautifulSoup
import requests
import re

#Storing wanted artist
artist = input("Desired artist >> ")

#Transforimg wanted artist into an html search term
artist_html_syntax = ""
for c in artist:
    if c == " ":
        artist_html_syntax += "%20"
    else:
        artist_html_syntax += c 

#Obtaining the search URL for wanted artist
preliminary_url = "https://www.ticketmaster.com/search?q=" + artist_html_syntax

response = requests.get(preliminary_url)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all('a'):
    print(link.get("href"))

#search = soup.find_all("input", class_="Search-input")