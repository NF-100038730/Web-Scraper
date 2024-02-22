from bs4 import BeautifulSoup
import requests

artist = input("Enter artist (eg. taylor swift) >> ")
month = input("Enter month (eg. Oct) >> ")

artist_p20 = ""
artist_d = ""

for c in artist:
    if c == " ":
        artist_p20 += "%20" 
        artist_d += "-"
    else:
        artist_p20 += c
        artist_d += c

tm_url = f"https://www.ticketmaster.com/search?q={artist_p20}"
sh_url = f"https://www.stubhub.com/secure/search?q={artist_p20}"

#print(tm_url)
#print(sh_url)

tm_response = requests.get(tm_url)
tm_soup = BeautifulSoup(tm_response.text, "html.parser")

sh_response = requests.get(sh_url)
sh_soup = BeautifulSoup(sh_response.text, "html.parser")

for links in tm_soup.find_all("a"):
    if artist_d in links.get("href"):
        tm_url = "https://www.ticketmaster.com" + links.get("href")
        break

print(tm_url)
    
for links in sh_soup.find_all("a"):
    if artist_d in links.get("href"):
        sh_url = links.get("href")
        break

print(sh_url)