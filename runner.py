from argparse import ArgumentParser, Namespace

from main import *

parser = ArgumentParser()
parser.usage = "Ticketmaster Web Scraper"
parser.add_argument("--state", type=str, help="str >> State that contains the wanted city (e.g. TX)")
parser.add_argument("--city", type=str, help="str >> City that will be price checked (e.g. College Station)")
args: Namespace = parser.parse_args()

check_state(args.state, args.city)