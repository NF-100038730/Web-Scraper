from argparse import ArgumentParser, Namespace

from main import *

parser = ArgumentParser()
parser.usage = "Ticketmaster Web Scraper"
parser.add_argument("--location", type=str, help="str >> Approximate location of event (eg. 77002, Houston, TX)")
parser.add_argument("--date", type=str, help="str >> Approximate date of event (eg. 01/01/2024)")
parser.add_argument("--artist", type=str, help="str >> Name of artist (eg. Taylor Swift)")
args: Namespace = parser.parse_args()

checkShows(args.location, args.date, args.artist)