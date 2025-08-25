import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
import pyowm
from pygame import mixer
import speech_recognition as sr

# -------------------
# Initialize Speech Engine
# -------------------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('volume', 1.0)          # 0.0 to 1.0
engine.setProperty('rate', 150)            # normal speaking speed

# -------------------
# Helper Function
# -------------------
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# -------------------
# Commands & Responses
# -------------------
greetings = ['hey there', 'hello', 'hi', 'hey', 'hi there']
questions = ['how are you', 'how are you doing']
responses = ['I am fine', "Doing well, thank you!"]

who_made = ['who made you', 'who created you']
who_made_ans = ['I was created by Jashan Dhillon, right on his computer.',
                'Jashan Dhillon is my creator.',
                'I was built by Jashan Dhillon.']

time_cmds = ['what time is it', 'what is the time', 'time']
identity_cmds = ['who are you', 'what is your name']
identity_ans = ['I am your personal AI assistant, built by Jashan Dhillon.']

open_browser = ['open browser', 'open google']
play_music = ['play music', 'play songs', 'play a song', 'open music player']
joke_cmds = ['tell a joke', 'tell me a joke', 'say something funny']
jokes = [
    'Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.',
    'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.',
    'Doctor: I’m sorry but you suffer from a terminal illness and have only 10 to live. '
    'Patient: What do you mean, 10 what? Months? Weeks?!" Doctor: Nine.'
]

youtube_cmds = ['open youtube', 'i want to watch a video']
weather_cmds = ['tell me the weather', 'weather', 'what about the weather']
exit_cmds = ['exit', 'close', 'goodbye', 'nothing']
color_cmds = ['what is your color', 'what is your colour']
fav_color_cmds = ['what is your favourite colour', 'what is your favourite color']
thank_cmds = ['thank you']
thank_resp = ['You’re welcome!', 'Glad I could help you.']

colors = ['Right now it’s rainbow.', 'Currently it’s transparent.', 'It’s non-chromatic.']

# -------------------
# Weather Setup (replace with your API key)
# -------------------
owm = pyowm.OWM('YOUR_API_KEY')
mgr = owm.weather_manager()

# -------------------
# Main Loop
# -------------------
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("\nListening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio).lower()
            print("You said:", text)
        except sr.UnknownValueError:
            speak("I didn’t get that. Please repeat.")
            continue

    # Greetings
    if text in greetings:
        speak(random.choice(greetings))

    # Questions
    elif text in questions:
        speak(random.choice(responses))

    # Who made you
    elif text in who_made:
        speak(random.choice(who_made_ans))

    # Thank you
    elif text in thank_cmds:
        speak(random.choice(thank_resp))

    # Colors
    elif text in color_cmds or text in fav_color_cmds:
        speak(random.choice(colors))
        speak("It keeps changing every micro second.")

    # Play Music
    elif text in play_music:
        try:
            mixer.init()
            mixer.music.load("music/song1.mp3")  # put your songs in a 'music' folder
            mixer.music.play()
            speak("Playing music for you.")
        except Exception as e:
            speak("I couldn’t play the music. Please check the file path.")

    # Identity
    elif text in identity_cmds:
        speak(random.choice(identity_ans))

    # Open YouTube
    elif text in youtube_cmds:
        webbrowser.open('https://www.youtube.com')
        speak("Opening YouTube.")

    # Open Browser
    elif text in open_browser:
        webbrowser.open('https://www.google.com')
        speak("Opening Google.")

    # Exit
    elif text in exit_cmds:
        speak("See you later, Jashan!")
        break

    # Weather
    elif text in weather_cmds:
        try:
            observation = mgr.weather_at_place("Bangalore,IN")
            w = observation.weather
            temp = w.temperature('celsius')
            weather_report = f"The temperature is {temp['temp']}°C, humidity is {w.humidity}% and wind speed is {w.wind()['speed']} meters per second."
            speak(weather_report)
        except Exception as e:
            speak("Sorry, I couldn’t fetch the weather right now.")

    # Time
    elif text in time_cmds:
        now = datetime.datetime.now().strftime("The time is %H:%M")
        speak(now)

    # Joke
    elif text in joke_cmds:
        speak(random.choice(jokes))

    # Wikipedia Fallback
    else:
        try:
            summary = wikipedia.summary(text, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("That’s too broad, can you be more specific?")
        except wikipedia.exceptions.PageError:
            speak("I couldn’t find anything on that.")
