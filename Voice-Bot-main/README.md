A simple Python-based voice assistant that listens to your microphone, recognizes speech, and responds with voice output.
Customized with personal responses for Jasan Dhillon ✨.

🚀 Features
🎧 Listens to your voice via microphone

🗣️ Converts speech to text (using Google Speech Recognition)

🤖 Responds with basic text & voice using pyttsx3

👤 Personalized answers (e.g., introduction, name, greetings)

🔁 Continuous loop: listens → understands → responds

🛠️ Requirements
Make sure you have Python 3.10+ installed.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Typical requirements include:

speechrecognition – for speech to text

pyttsx3 – for text to speech

pyaudio – for microphone input (install via pipwin on Windows)

pyowm – (optional) for weather responses

If you face issues with pyaudio, install it like this (Windows):

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
▶️ How to Run
Run the bot with:

bash
Copy
Edit
python main.py
You’ll see:

yaml
Copy
Edit
Listening...
You said: hello
Bot: Hello Jasan Dhillon, how are you?
And the bot will also speak the response out loud.

⚡ Example Conversations
You: "Hello"
Bot: "Hello Jasan Dhillon, how are you?"

You: "What’s your name?"
Bot: "I’m your personal voice assistant, built for Jasan Dhillon."

You: "Tell me about yourself"
Bot: "I’m a simple Python voice bot that listens, understands, and responds."

📂 Project Structure
bash
Copy
Edit
Voice-Bot/
│── main.py # Main script
│── requirements.txt # Dependencies
│── README.md # Documentation
❗ Troubleshooting
Pyaudio install fails:
Use pipwin install pyaudio instead of pip install pyaudio.

Bot not speaking:
Ensure pyttsx3 is installed and engine.runAndWait() is present.

Microphone issues:
Check microphone permissions and default input device settings.

📌 Notes
You can customize responses inside main.py (e.g., greetings, personal info).

Currently supports English. Multi-language support can be added later.
