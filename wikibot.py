import argparse
import pyttsx3
import wikipediaapi
speaker = pyttsx3.init()
speaker.setProperty('rate', 185)
wikia = wikipediaapi.Wikipedia('en')
parser = argparse.ArgumentParser()
parser.add_argument('t', help="the title you wanna search for", type=str)
parser.add_argument(
    '--f', '--full', help="if provided, it will read the entire wikipedia page", action='store_true')
args = parser.parse_args()
page = wikia.page(args.t)
speaker.say(page.summary)
speaker.runAndWait()
if args.f:
    art = wikia.article(args.t)
    speaker.say(art.text)
    speaker.runAndWait()
