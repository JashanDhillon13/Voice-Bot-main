This is a small Python voice assistant project. The bot listens to your microphone, converts your speech to text, and replies back using text-to-speech.
I’ve also added some basic custom responses related to me (Jasan Dhillon).

What it does
Listens from mic

Converts voice → text (Google speech recognition)

Replies in voice using pyttsx3

Has some personalized answers (like name, intro, etc.)

Setup
Make sure you have Python 3.10 or higher.

Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
If pyaudio fails to install on Windows, do this:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
Run
Start the bot with:

bash
Copy
Edit
python main.py
You should see something like:

yaml
Copy
Edit
Listening...
You said: hello
Bot: Hello Jasan Dhillon, how are you?
And the bot will also speak the response.

Example
You: "hello"
Bot: "Hello Jasan Dhillon, how are you?"

You: "what is your name"
Bot: "I’m your voice bot, made for Jasan Dhillon."

Notes
If the mic doesn’t work, check Windows mic permissions.

All responses are inside main.py, you can edit them easily.

Only supports English right now.

Pretty basic, but does the job.
