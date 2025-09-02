Jarvis - Python Voice Assistant

Jarvis ek simple Python-based voice assistant hai jo aapki commands sun kar kaam karta hai. Ye aapko music play kar ke dega, Google/Youtube open karega, Wikipedia search karega, time/date batayega, aur WhatsApp pe message bhejega.

✨ Features

🎶 Random music play from YouTube

⏰ Current time and date check

🌐 Open websites like Google, YouTube, Facebook, Instagram

📖 Wikipedia search and result read aloud

🔎 Google search by voice

💬 Send WhatsApp message automatically

📦 Requirements

Ensure that you have Python installed. Then install the following dependencies:

pip install pyttsx3
pip install SpeechRecognition
pip install wikipedia
pip install pywhatkit
pip install pyaudio


⚠ Note: pyaudio installation can sometimes give errors. Use this if normal installation fails:

pip install pipwin
pipwin install pyaudio

▶️ How to Run

Clone or download this repository.

Open the project folder in your terminal/IDE.

Run the script:

python jarvis.py


Speak into your microphone and say commands like:

"Jarvis play music"

"Jarvis show time"

"Jarvis show date"

"Jarvis open YouTube"

"Jarvis search Wikipedia Albert Einstein"

"Jarvis search Google Python tutorial"

"Jarvis send WhatsApp"

⚙️ Example WhatsApp Usage

In the code, update the number and time according to your need:

pywhatkit.sendwhatmsg("+923xxxxxxxxx", "Hello from Jarvis!", 16, 35, 10)


+923xxxxxxxxx → Your WhatsApp number (with country code)

"Hello from Jarvis!" → Message to send

16, 35 → Time (24-hour format, 16:35 = 4:35 PM)

10 → Wait time before sending

📌 Notes

Internet connection required for Google, YouTube, Wikipedia, and WhatsApp features.

WhatsApp message scheduling requires your WhatsApp Web to be open.

Make sure your microphone is working properly.
