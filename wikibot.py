import wikipediaapi
import pyttsx3


class wikia:
    def __init__(self):
        self.speaker = pyttsx3.init()
        self.speaker.setProperty('rate', 185)  # personally i prefer 185

    def speak(self, name):
        self.wiki = wikipediaapi.Wikipedia('en')
        self.page = self.wiki.page(name)
        self.speaker.say(self.page.summary)
        self.speaker.runAndWait()


stuff = wikia()
stuff.speak("Reddit")
