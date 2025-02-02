from lib import *
import re

def open_app(instruction):
    app = instruction.replace("open", "").strip()
    if app:
        talk(f"Opening {app}")
        open(app, match_closest=True)
    else:
        talk("Please specify an application to open.")

def close_app(instruction):
    app = instruction.replace("close", "").strip()
    if app:
        talk(f"Closing {app}")
        close(app, match_closest=True)
    else:
        talk("Please specify an application to close.")

def play_youtube(instruction):
    song = instruction.replace("play", "").strip()
    talk(f"Playing {song} on YouTube")
    kit.playonyt(song)

def google_search(instruction):
    topic = re.sub(r"(search|google)", "", instruction).strip()
    if topic:
        talk(f"Searching for {topic}")
        kit.search(topic)
    else:
        talk("Please specify a topic to search for.")

def tell_time():
    time = datetime.now().strftime('%I:%M %p')
    talk(f"The current time is {time}")

def tell_date():
    date_ = datetime.now().strftime('%d %B %Y')
    day = calendar.day_name[datetime.now().weekday()]
    talk(f"Today is {day}, {date_}")

def respond_to_greeting():
    talk("I'm Aryan, your virtual assistant. How can I help you today?")

def terminate():
    talk("Sure. Have a nice day.")
    return "terminate"

def fetch_information(instruction):
    topic = re.sub(r"(what is|who is|provide info on|provide info about|provide information on|provide information about)", "", instruction).strip()
    if topic:
        try:
            talk(f"Collecting information about {topic}")
            info = wp.summary(topic, sentences=2)
            talk("here is what i found.")
            print(info)
        except wp.exceptions.DisambiguationError:
            talk("There are multiple articles related to this topic. Searching on google instead.")
            google_search(topic)
        except wp.exceptions.PageError:
            talk(f"I couldn't find information on {topic} from Wikipedia. Searching on Google instead.")
            google_search(topic)
    else:
        talk("Please specify a topic to get information about.")

COMMANDS = {
    "open": open_app,
    "close": close_app,
    "play": play_youtube,
    "search": google_search,
    "google": google_search,
    "time": lambda _: tell_time(),
    "date": lambda _:tell_date(),
    "how are you": lambda _: talk("I'm fine, thank you! How can I assist you?"),
    "what is your name": lambda _: respond_to_greeting(),
    "terminate": lambda _: terminate(),
    "what is": fetch_information,
    "who is": fetch_information,
    "provide info on": fetch_information,
    "provide info about": fetch_information,
    "provide information on": fetch_information,
    "provide information about": fetch_information,
}

def play_Aryan():
    instruction = input_instruction()

    if not instruction:
        talk("Please repeat.")
        return

    for command, action in COMMANDS.items():
        if command in instruction:
            result = action(instruction)
            if result == "terminate":
                return True
            return

    talk("Sorry, I didn't understand that command. Please try again.")