import sys
import speech_recognition as sr
import datetime
import os
import webbrowser
import ssl
import instagram
import metaDataImages
import moodDetection
from googlesearch import search
import pywhatkit

ssl._create_default_https_context = ssl._create_unverified_context


def speak(audio):
    os.system(f"say {audio}")
    print(audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query

    except Exception as e:
        print("Please repeat...")
        speak("Please repeat")
        return takecommand()

def wish():
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("My name is PAARO Sir or Partially Active A.I Reeks Originality, how may I help you")

def tell_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    time_str = now.strftime("%I:%M %p")
    speak(f"The time right now is {time_str}")

def web_scraping(keyword):
    try:
        links = list(search(keyword, num=5, stop=5, pause=2))
        return links
    except Exception as e:
        print("An error occurred while searching online:", e)
        return []


def play_youtube(query):
    if  any(keyword in query for keyword in ["random", "anything", "your choice", "whatever you want", "whatever you like"]):
        speak("Sure sir, I hope you like my choice")
        pywhatkit.playonyt("")

    else:
        speak("What song would you like to listen to?")
        song_name = takecommand()
        speak(f"Playing {song_name} on YouTube.")
        pywhatkit.playonyt(song_name)


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        if "time" in query:
            tell_time()

        elif any(keyword in query for keyword in
                 ["search the internet for", "google", "what can you tell me about", "show me what you know about"]):
            links = web_scraping(query)

            if links:
                speak("Here are the top 5 most relevant links:")
                for i, link in enumerate(links[:5], 1):
                    print(f"{i}. {link}")
            else:
                speak("No relevant links found for the keyword")
            speak("Would you like me to open any of the links, sir?")

            response = takecommand().lower()
            if any(word in response for word in ["yes", "yeah", "sure", "why not"]):
                speak("Which one would you like, sir?")

                response = takecommand().lower()
                if any(word.isdigit() for word in response):

                    n = int(next(word for word in response.split() if word.isdigit()))
                    if 1 <= n <= len(links):
                        speak(f"Sure sir, opening link number {n}")
                        webbrowser.open(links[n - 1])

                    else:
                        speak("Invalid choice, sir. Please try again.")
                elif any(word in response for word in ["all", "everyone", "each one"]):
                    speak("Sure, sir. Opening them all in the browser right now.")

                    for link in links:
                        webbrowser.open(link)
                else:
                    speak("Sorry sir, I didn't understand your choice.")
            else:
                speak("Sure, sir. Not opening any link. What else may I help you with?")

        elif any(keyword in query for keyword in
                 ["instagram", "insta", "profile"]):
            speak("Sure sir, I will download, please type the username: ")
            username = input("Enter: ")
            speak("Downloading profile data")
            instagram.input(username)
            speak("Profile data downloaded successfully.")

        elif any(keyword in query for keyword in ["meta data", "image", "metadata"]):
            speak("Sure sir, I will download, please type the image path: ")
            path = input("Enter: ")
            speak("Downloading image metadata")
            metaDataImages.image(path)
            speak("Image metadata downloaded successfully.")


        elif any(keyword in query for keyword in ["mood","feeling","feel"]):
            speak("Sure sir, I will detect your mood")
            mood=moodDetection.mood()
            speak(f"You're feeling {mood} right now Sir")
            print(f"You're feeling {mood} right now Sir")


        elif (query == "are you up darling"):
            speak("For you sir, always. How may I help you today")

        elif any(keyword in query for keyword in ["play", "play youtube", "play video", "play song", "play music"]):
            speak("Sure sir, what should I play?")
            query = takecommand()
            play_youtube(query)


        elif any ( keyword in query for keyword in ["exit", "quit", "goodbye", "bye"]):
            speak("Goodbye sir. Have a nice day.")
            sys.exit(0)
