#argparse imports for command line opperation
from argparse import ArgumentParser, Namespace

#main import for utilization of functions
from main import *

parser = ArgumentParser()
parser.usage = "Ticketmaster Web Scraper"
parser.add_argument("--state", type=str, help="str >> State that contains the wanted city (e.g. TX)")
parser.add_argument("--city", type=str, help="str >> City that will be price checked (e.g. 'College Station')")
parser.add_argument("--fuel", type=str, help="str >> Type of fuel (Regular, Midgrade, Premium, and Diesel)")
args: Namespace = parser.parse_args()

check_state(args.state, args.city, args.fuel)