import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import subprocess
import datetime
import os
import pyjokes
import wikipedia
import pyautogui
from app_paths import applications

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print(sr.Microphone.list_microphone_names())


notes = ""

def speak(text):
    print(f"Speaking: {text}")

    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. Ready to help you!")

def open_application(app_name):
    app_path = applications.get(app_name.lower())
    if app_path:
        try:
            subprocess.run(app_path, check=True)
            speak(f"Opening {app_name}.")
        except Exception as e:
            speak(f"Sorry, I couldn't open {app_name}. Error: {e}")
    else:
        speak(f"Sorry, {app_name} is not in my list.")

def processCommand(c):
    global notes
    command = c.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        print("About to speak: Opening Google.") 
        speak("Opening Google.")

    elif "check" in command:
        speak("This is a test.")
        print("About to speak: This is a test.")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif "what time" in command or "tell me the time" in command:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {strTime}")

    elif "what date" in command:
        today = datetime.datetime.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    elif "tell me a joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "").strip()
        if topic:
            speak("Searching Wikipedia...")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            except:
                speak("Sorry, I couldn't find anything on that topic.")
        else:
            speak("Please tell me what to search on Wikipedia.")

    elif "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased.")
    elif "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased.")
    elif "mute volume" in command:
        pyautogui.press("volumemute")
        speak("Volume muted.")

    elif "shutdown" in command:
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif "restart" in command:
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    elif "sleep" in command:
        speak("Sleeping now.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "remember this" in command:
        notes = command.replace("remember this", "").strip()
        speak("I have noted that.")
    elif "what did you remember" in command:
        if notes:
            speak(f"You told me to remember: {notes}")
        else:
            speak("You haven't told me anything to remember.")

    elif "open folder" in command:
        folder_path = r"C:\Users\hp\Documents"  # ← customize this
        os.startfile(folder_path)
        speak("Opening your documents folder.")

    elif "search" in command:
        find = command.split("search", 1)[1]
        formatted_query = find.replace(" ", "+")
        search_url = f"https://www.google.com/search?q={formatted_query}"
        webbrowser.open(search_url)
        speak(f"Searching for {find}.")

    elif command.startswith("play"):
        song = command.split("play", 1)[1].strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I couldn't find {song} in your music library.")

    elif command.startswith("repeat"):
        speak(command.split("repeat", 1)[1].strip())

    elif command.startswith("open"):
        app_name = command.split("open", 1)[1].strip()
        open_application(app_name)

    else:
        speak("Sorry, I didn't get that command.")


if __name__ == "__main__":
    greet()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5 ,phrase_time_limit=None)
                word = recognizer.recognize_google(audio)
                print(word)

                if word.lower() == "Jarvis":
                    speak("Yes sir!")
                    print("Jarvis Activated...")

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

        except Exception as e:
            print("Error:", e)
