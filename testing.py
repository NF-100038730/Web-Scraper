from bs4 import BeautifulSoup
import requests

artist = input("Enter artist (eg. taylor swift) >> ")
month = input("Enter month (eg. 10 for Oct) >> ")

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
sh_url = f"https://www.stubhub.com/secure/search?q={artist_p20}&sellSearch=false"

tm_prelim_response = requests.get(tm_url)
tm_prelim_soup = BeautifulSoup(tm_prelim_response.text, "html.parser")

for links in tm_prelim_soup.find_all("a"):
    if artist_d in links.get("href"):
        tm_url = "https://www.ticketmaster.com" + links.get("href")
        break

tm_response = requests.get(tm_url)
tm_soup = BeautifulSoup(tm_response.text, "html.parser")

# dates = tm_soup.find_all(string=month)
# parent = dates[0].parent
# print(parent)

# sh_response = requests.get(sh_url)
# sh_soup = BeautifulSoup(sh_response.content, "html.parser")
    
# for links in sh_soup.find_all("a"):
#     if artist_d in links.get("href"):
#         sh_url = links.get("href")
#         break

# print(sh_url)