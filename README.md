# 🤖 Jarvis - Python Voice Assistant

Jarvis is a Python-based voice assistant that listens for a wake word and performs various tasks using voice commands. It can search the web, tell jokes, control system volume, open apps or websites, fetch information from Wikipedia, and more!

---

## 📌 Features

- ✅ **Wake Word Activation**: Say `"Jarvis"` to activate Jarvis and give your command.
- 🔊 **Text-to-Speech**: Jarvis responds using natural voice via `pyttsx3`.
- 🎤 **Voice Recognition**: Understands and processes voice input using `speech_recognition`.
- 🌐 **Web Searching**:
  - Open popular websites like **Google**, **YouTube**, **Facebook**, **LinkedIn**, etc.
  - Perform custom **Google search** queries.
  - Fetch Wikipedia summaries.
- 🎵 **Play Songs**: Search for songs from a predefined `musicLibrary`.
- ⏰ **Time & Date**: Ask for current time or date.
- 🎭 **Jokes**: Get a random funny joke using `pyjokes`.
- 🧠 **Notes Memory**: Tell Jarvis something to remember, and it can recall it later.
- 🔊 **Volume Control**: Increase, decrease, or mute system volume.
- 💻 **System Commands**: Shutdown, restart, or put the system to sleep.
- 📁 **Open Folders**: Open pre-defined system folders.
- 💬 **Repeat Feature**: Ask Jarvis to repeat any statement.

---

## 🚀 How It Works

1. Jarvis runs in an infinite loop listening for the **wake word**: `"equation"`.
2. On detecting the wake word:
   - It activates and listens for a voice command.
   - It matches your command with supported features and executes the corresponding action.

---

## 🧠 Technologies & Libraries Used

- `speech_recognition` – for voice input
- `pyttsx3` – for text-to-speech
- `webbrowser` – for opening websites
- `wikipedia` – for Wikipedia summaries
- `pyautogui` – for system-level key presses (volume control)
- `pyjokes` – for jokes
- `subprocess` – for launching applications
- `os`, `datetime` – for system operations and timestamps
- `musicLibrary.py` – a custom module to store and fetch song links
- `app_paths.py` – stores paths of apps to open via command

---

## 📁 Project Structure

```
Jarvis-Voice-Assistant/
│
├── main.py               # Your main voice assistant script
├── app_paths.py          # Python dictionary containing paths of your system apps
├── musicLibrary.py       # Dictionary of song names and their YouTube links
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

---

## 🔧 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/jarvis-voice-assistant.git
   cd jarvis-voice-assistant
   ```

2. **Install Dependencies:**
   First, ensure Python 3 is installed.

   ```bash
   pip install -r requirements.txt
   ```

   **Required modules (if `requirements.txt` is not available):**
   ```bash
   pip install SpeechRecognition pyttsx3 wikipedia pyjokes pyautogui
   ```

3. **Configure paths:**
   - Open `app_paths.py` and update the dictionary with full paths of applications on your system.
   - In `musicLibrary.py`, add your favorite songs and YouTube links like this:

     ```python
     music = {
         "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
         "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
     }
     ```

4. **Run the assistant:**
   ```bash
   python main.py
   ```

---

## 💡 Tips

- Test microphone input separately if Jarvis doesn't respond.
- Adjust timeout and `phrase_time_limit` in `recognizer.listen()` if needed.
- Replace `"Jarvis"` with any other custom wake word you prefer.
- If no voice input is working, add a keyboard fallback mode (optional improvement).

---

## 🧪 Example Commands

- `"Jarvis"` → Wake Jarvis  
- `"open youtube"` → Opens YouTube in browser  
- `"tell me a joke"` → Responds with a funny joke  
- `"what's the time"` → Tells current time  
- `"remember this I have a meeting at 5"` → Jarvis stores the note  
- `"what did you remember"` → Recalls stored notes  
- `"shutdown"` → Shuts down the computer

---
