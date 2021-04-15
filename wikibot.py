import argparse
import pyttsx3
import wikipediaapi
wikia = wikipediaapi.Wikipedia('en')
parser = argparse.ArgumentParser()
parser.add_argument('t', help="the title you wanna search for", type=str)
parser.add_argument(
    '--f', '--full', help="if provided, it will read the entire wikipedia page", action='store_true')
parser.add_argument('--q','--quiet', help="if provided, the program will not speak the text on the page", action='store_true')
args = parser.parse_args()
page = wikia.page(args.t)
if not args.q:
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 185)
    speaker.say(page.summary)
    speaker.runAndWait()
    if args.f:
        art = wikia.article(args.t)
        speaker.say(art.text)
        speaker.runAndWait()
